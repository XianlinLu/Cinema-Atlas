#!/usr/bin/env python3
"""Validate normalized Lumina production state; never submits media jobs.

python3 tools/lumina_preflight.py request request.json --profile profile.json
python3 tools/lumina_preflight.py project manifest.json --stage video
python3 tools/lumina_preflight.py completion manifest.json

The agent maps the REAL host schema to this normalized representation. Profiles
must come from that endpoint's current contract. This helper stays outside the
text-only import folder and cannot enable unavailable Lumina tools.
"""
import argparse
import json
import math
from pathlib import Path


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def approved(record):
    approval = record.get('approval', {})
    return (approval.get('status') == 'approved' and record.get('version') is not None
            and approval.get('version') == record.get('version'))


def validate_request(request, profile):
    issues = []
    if not profile.get('model_id') or request.get('model_id') != profile.get('model_id'):
        issues.append('model_profile: request must match the inspected runtime model')
    mode = request.get('operation')
    if profile.get('operations') and mode not in profile['operations']:
        issues.append('operation: unsupported task kind')
    duration = request.get('duration_seconds')
    minimum, maximum = profile.get('video_min_seconds'), profile.get('video_max_seconds')
    if not number(duration) or duration <= 0:
        issues.append('duration: missing, non-finite or non-positive')
    elif not number(minimum) or not number(maximum):
        issues.append('duration_profile: inspect the real endpoint limits')
    else:
        if not minimum <= duration <= maximum:
            issues.append('duration: outside runtime video limits')
        if profile.get('integer_durations') and int(duration) != duration:
            issues.append('duration: this profile requires integer seconds')
    adaptive_modes = profile.get('adaptive_ratio_modes', [])
    if mode in adaptive_modes:
        ratio = request.get('ratio')
        if ratio is None:
            if not profile.get('ratio_omission_allowed', False):
                issues.append('ratio: required adaptive value was omitted')
        elif not profile.get('adaptive_ratio_value') or ratio != profile['adaptive_ratio_value']:
            issues.append('ratio: this task requires adaptive/inherited ratio, not a forced ratio')
    elif profile.get('ratios') and request.get('ratio') not in profile['ratios']:
        issues.append('ratio: unsupported or missing ordinary-generation ratio')
    if mode == 'extend':
        source = request.get('source_video', {})
        if not source.get('asset_id') or not source.get('usable'):
            issues.append('extension_source: real checked predecessor is required')
        if not source.get('ratio') or source.get('ratio') != request.get('target_ratio'):
            issues.append('extension_ratio: source must already have the intended project ratio')
        if not all(source.get(k) is True for k in ('same_scene', 'same_time', 'same_costume', 'continuous_action')):
            issues.append('extension_continuity: scene/time/costume/action must all match')
    refs = request.get('audio_refs', [])
    if refs:
        keys = ('audio_min_seconds', 'audio_max_seconds', 'audio_total_max_seconds', 'audio_max_count')
        if not all(number(profile.get(k)) and profile[k] > 0 for k in keys):
            issues.append('audio_profile: inspect per-file/count/total constraints')
        else:
            if len(refs) > profile['audio_max_count']:
                issues.append('audio_count: too many attached audio references')
            total = 0.0
            measured = True
            for i, ref in enumerate(refs):
                d = ref.get('duration_seconds')
                if not ref.get('asset_id') or ref.get('ready') is not True:
                    issues.append(f'audio_ref[{i}]: missing or unready actual asset')
                if not number(d) or d <= 0:
                    issues.append(f'audio_ref[{i}]: duration must be measured and finite')
                    measured = False
                else:
                    total += d
                    if not profile['audio_min_seconds'] <= d <= profile['audio_max_seconds']:
                        issues.append(f'audio_ref[{i}]: duration outside per-file bounds')
                if profile.get('audio_formats') and ref.get('format') not in profile['audio_formats']:
                    issues.append(f'audio_ref[{i}]: unsupported or unknown audio format')
            margin = profile.get('audio_budget_margin_seconds', 0.5)
            if not number(margin) or margin < 0:
                issues.append('audio_margin: must be finite and nonnegative')
            elif measured and total > profile['audio_total_max_seconds'] - margin + 1e-9:
                issues.append('audio_budget: aggregate audio exceeds the measured safe budget')
    return issues


def validate_project(plan, stage='video'):
    issues = []
    script = plan.get('script', {})
    if not approved(script):
        issues.append('script_approval: exact current script version must be approved')
    if stage == 'characters':
        return issues
    characters, voices = plan.get('characters', {}), plan.get('voices', {})
    for cid, character in characters.items():
        sheet = character.get('sheet', {})
        if not approved(sheet) or not sheet.get('asset_id') or sheet.get('ratio') != '16:9':
            issues.append(f'character[{cid}]: approved real 16:9 sheet required')
    if stage == 'auditions':
        for vid, voice in voices.items():
            if voice.get('profile_approved') is not True:
                issues.append(f'voice[{vid}]: native voice-profile decision required')
        return issues
    for vid, voice in voices.items():
        if not approved(voice) or not voice.get('asset_id'):
            issues.append(f'voice[{vid}]: approved actual audition/voice asset required')
        if voice.get('owner') not in characters and voice.get('owner') != 'NARRATOR':
            issues.append(f'voice[{vid}]: unknown owner')
    table = plan.get('table', {})
    if not approved(table) or table.get('script_version') != script.get('version'):
        issues.append('table_approval: exact current table for this script must be approved')
    shots = plan.get('shots', [])
    if not shots:
        issues.append('shots: complete production queue is missing')
    ids = [s.get('shot_id') for s in shots]
    if any(not x for x in ids) or len(ids) != len(set(ids)):
        issues.append('shot_ids: nonempty and unique IDs required')
    previous_end = 0
    script_lines = script.get('lines', {})
    for shot in shots:
        sid = shot.get('shot_id', '?')
        d, start, end = shot.get('duration_seconds'), shot.get('start'), shot.get('end')
        if not number(d) or d <= 0 or int(d) != d or not number(start) or not number(end):
            issues.append(f'{sid}: positive integer shot duration and numeric boundaries required')
        else:
            if abs(start - previous_end) > 1e-6 or abs(end - start - d) > 1e-6:
                issues.append(f'{sid}: timeline gap/overlap or duration mismatch')
            previous_end = end
        if shot.get('script_version') != script.get('version') or shot.get('table_version') != table.get('version'):
            issues.append(f'{sid}: stale script/table dependency')
        refs = {r.get('character_id'): r for r in shot.get('character_refs', [])}
        for cid in shot.get('characters_present', []):
            sheet = characters.get(cid, {}).get('sheet', {})
            ref = refs.get(cid, {})
            if not sheet or ref.get('asset_id') != sheet.get('asset_id') or ref.get('sheet_version') != sheet.get('version'):
                issues.append(f'{sid}: wrong/missing current character reference for {cid}')
        on_screen_speakers = set()
        for line in shot.get('dialogue', []):
            owner, vid = line.get('speaker_id'), line.get('voice_id')
            voice = voices.get(vid, {})
            if voice.get('owner') != owner or line.get('voice_version') != voice.get('version'):
                issues.append(f'{sid}: speaker/voice ownership or version mismatch')
            source = script_lines.get(line.get('line_id'), {})
            if not source or source.get('text') != line.get('text') or source.get('speaker_id') != owner:
                issues.append(f'{sid}: dialogue does not match the approved script line')
            audio_duration = line.get('audio_duration_seconds')
            offset = line.get('offset_seconds', 0.3)
            tail = line.get('tail_seconds', 0.4)
            if not line.get('audio_asset_id') or not number(audio_duration) or audio_duration <= 0:
                issues.append(f'{sid}: exact shot speech needs actual audio and measured duration')
            elif (not number(offset) or not number(tail) or offset < 0 or tail < 0 or not number(d)
                  or offset + audio_duration + tail > d + 1e-9):
                issues.append(f'{sid}: measured speech and handles do not fit')
            if line.get('kind', 'dialogue') == 'dialogue' and owner in shot.get('characters_present', []):
                on_screen_speakers.add(owner)
            if line.get('kind') == 'narration' and owner != 'NARRATOR':
                issues.append(f'{sid}: narrator must have separate ownership')
        if len(on_screen_speakers) > 1:
            issues.append(f'{sid}: split changes of on-screen speaker into atomic shots')
        for cid in shot.get('characters_present', []):
            expected = 'speaking' if cid in on_screen_speakers else 'closed'
            if shot.get('mouth_rules', {}).get(cid) != expected:
                issues.append(f'{sid}: mouth rule mismatch for {cid}')
        for ref in shot.get('audio_refs', []):
            if ref.get('purpose') in ('voice_reference', 'speech_driver'):
                voice = voices.get(ref.get('voice_id'), {})
                if not voice or voice.get('owner') != ref.get('owner'):
                    issues.append(f'{sid}: audio reference is bound to the wrong voice owner')
    return issues


def classify_error(message):
    s = message.lower()
    if 'policyviolation' in s or 'sensitivecontentdetected' in s:
        return 'policy_stop'
    if 'ratio' in s and ('extension' in s or 'tasktypeconstraint' in s):
        return 'fix_task_ratio'
    if 'audio' in s and 'duration' in s and ('invalidparameter' in s or 'must be' in s):
        return 'fix_measured_audio'
    if any(token in s for token in ('429', '503', '502', 'timeout', 'temporarily unavailable')):
        return 'query_then_bounded_retry'
    return 'inspect_and_recover'


def validate_completion(plan):
    issues = validate_project(plan)
    shots = plan.get('shots', [])
    for shot in shots:
        if shot.get('status') not in ('checked', 'approved') or not shot.get('output_asset_id'):
            issues.append(f"{shot.get('shot_id', '?')}: no checked real video output")
    for job in plan.get('jobs', []):
        if job.get('required_for_final', True) and job.get('status') not in ('checked', 'approved', 'succeeded'):
            issues.append('pending_job: required asynchronous work is not complete')
    output = plan.get('final_video', {})
    if not output.get('asset_id') or not output.get('ready') or not output.get('playback_checked'):
        issues.append('final_video: playable checked export required')
    if not output.get('ratio') or output.get('ratio') != plan.get('film_ratio'):
        issues.append('final_ratio: exported metadata does not match approved film ratio')
    expected = plan.get('table', {}).get('expected_duration_seconds')
    actual = output.get('duration_seconds')
    if not number(expected) or not number(actual) or expected <= 0 or abs(expected - actual) > 0.15:
        issues.append('final_duration: measured export must match the locked edit timeline')
    if output.get('shot_ids') != [s.get('shot_id') for s in shots]:
        issues.append('final_order: each required shot must appear once in approved order')
    if output.get('audio_verified') is not True:
        issues.append('final_audio: approved speech, narration and synchronization must be checked')
    return issues


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('kind', choices=['request', 'project', 'completion'])
    p.add_argument('input', type=Path)
    p.add_argument('--profile', type=Path)
    p.add_argument('--stage', choices=['characters', 'auditions', 'video'], default='video')
    args = p.parse_args()
    data = json.loads(args.input.read_text())
    if args.kind == 'request':
        if args.profile is None:
            p.error('--profile is required for request validation')
        issues = validate_request(data, json.loads(args.profile.read_text()))
    elif args.kind == 'project':
        issues = validate_project(data, args.stage)
    else:
        issues = validate_completion(data)
    print(json.dumps({'valid': not issues, 'issues': issues}, ensure_ascii=False, indent=2))
    raise SystemExit(bool(issues))


if __name__ == '__main__':
    main()
