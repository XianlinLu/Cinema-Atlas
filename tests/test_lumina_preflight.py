import copy
import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location('preflight', Path(__file__).parents[1] / 'tools/lumina_preflight.py')
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def locked(asset, owner=None):
    r = {'asset_id': asset, 'version': 1, 'approval': {'status': 'approved', 'version': 1}}
    if owner:
        r['owner'] = owner
    return r


def profile():
    return {'model_id': 'inspected-test-route', 'operations': ['independent', 'extend', 'first_frame'],
            'video_min_seconds': 4, 'video_max_seconds': 30, 'integer_durations': True,
            'ratios': ['16:9', '9:16'], 'adaptive_ratio_modes': ['extend', 'first_frame'],
            'adaptive_ratio_value': 'adaptive', 'ratio_omission_allowed': True,
            'audio_min_seconds': 2, 'audio_max_seconds': 30, 'audio_total_max_seconds': 30,
            'audio_max_count': 10, 'audio_formats': ['wav', 'mp3']}


def request():
    return {'model_id': 'inspected-test-route', 'operation': 'independent', 'ratio': '16:9',
            'target_ratio': '16:9', 'duration_seconds': 8,
            'audio_refs': [{'asset_id': 'voice-sample-A', 'duration_seconds': 4.5, 'ready': True, 'format': 'wav'}]}


def project():
    sheet = locked('sheet-A'); sheet['ratio'] = '16:9'
    script = locked('script'); script['lines'] = {'L1': {'speaker_id': 'CH1', 'text': 'A newly written line.'}}
    table = locked('table'); table['script_version'] = 1
    return {'script': script, 'characters': {'CH1': {'sheet': sheet}},
            'voices': {'VO1': locked('audition-A', 'CH1')}, 'table': table,
            'shots': [{'shot_id': 'SC01_SH01', 'script_version': 1, 'table_version': 1,
                       'duration_seconds': 8, 'start': 0, 'end': 8, 'characters_present': ['CH1'],
                       'character_refs': [{'character_id': 'CH1', 'asset_id': 'sheet-A', 'sheet_version': 1}],
                       'mouth_rules': {'CH1': 'speaking'},
                       'dialogue': [{'line_id': 'L1', 'speaker_id': 'CH1', 'text': 'A newly written line.',
                                     'voice_id': 'VO1', 'voice_version': 1, 'audio_asset_id': 'line-audio-A',
                                     'audio_duration_seconds': 3.2}],
                       'audio_refs': [{'purpose': 'voice_reference', 'voice_id': 'VO1', 'owner': 'CH1'}]}]}


class RequestChecks(unittest.TestCase):
    def test_valid_request(self):
        self.assertEqual(M.validate_request(request(), profile()), [])

    def test_screenshot_audio_minimum(self):
        r = request(); r['audio_refs'][0]['duration_seconds'] = 1.79
        self.assertTrue(any('per-file' in x for x in M.validate_request(r, profile())))

    def test_full_auditions_exceed_total(self):
        r = request(); r['audio_refs'] *= 2
        r['audio_refs'][0] = dict(r['audio_refs'][0], duration_seconds=25)
        r['audio_refs'][1] = dict(r['audio_refs'][1], duration_seconds=25)
        self.assertTrue(any('aggregate' in x for x in M.validate_request(r, profile())))

    def test_near_limit_has_margin(self):
        r = request(); r['audio_refs'][0]['duration_seconds'] = 29.9
        self.assertTrue(M.validate_request(r, profile()))

    def test_20_route_uses_15_second_budget(self):
        p = profile(); p.update(audio_max_seconds=15, audio_total_max_seconds=15, audio_max_count=3)
        r = request(); r['audio_refs'] = [dict(r['audio_refs'][0], duration_seconds=8) for _ in range(2)]
        self.assertTrue(any('aggregate' in x for x in M.validate_request(r, p)))

    def test_nan_and_unready_assets_rejected(self):
        r = request(); r['audio_refs'][0].update(duration_seconds=float('nan'), ready=False)
        self.assertGreaterEqual(len(M.validate_request(r, profile())), 2)

    def test_extension_ratio_fixed_then_adaptive(self):
        r = request(); r.update(operation='extend', source_video={
            'asset_id': 'prior-video', 'usable': True, 'ratio': '16:9', 'same_scene': True,
            'same_time': True, 'same_costume': True, 'continuous_action': True})
        self.assertTrue(any('ratio:' in x for x in M.validate_request(r, profile())))
        r['ratio'] = 'adaptive'
        self.assertEqual(M.validate_request(r, profile()), [])
        del r['ratio']
        self.assertEqual(M.validate_request(r, profile()), [])
        p = profile(); p['ratio_omission_allowed'] = False
        self.assertTrue(any('omitted' in x for x in M.validate_request(r, p)))

    def test_extension_cannot_change_scene_or_source_ratio(self):
        r = request(); r.update(operation='extend', ratio='adaptive', source_video={
            'asset_id': 'prior-video', 'usable': True, 'ratio': '9:16', 'same_scene': False,
            'same_time': True, 'same_costume': True, 'continuous_action': True})
        self.assertGreaterEqual(len(M.validate_request(r, profile())), 2)


class ProjectChecks(unittest.TestCase):
    def test_complete_valid_project(self):
        self.assertEqual(M.validate_project(project()), [])

    def test_ignored_gate_does_not_approve(self):
        p = project(); p['script']['approval']['status'] = 'ignored'
        self.assertTrue(any('script_approval' in x for x in M.validate_project(p)))

    def test_artifact_edit_invalidates_old_approval(self):
        p = project(); p['characters']['CH1']['sheet']['version'] = 2
        self.assertTrue(any('character[' in x for x in M.validate_project(p)))

    def test_incorrect_voice_owner(self):
        p = project(); p['voices']['VO1']['owner'] = 'NARRATOR'
        self.assertTrue(any('ownership' in x for x in M.validate_project(p)))

    def test_wrong_dialogue_and_voice_revision(self):
        p = project(); p['shots'][0]['dialogue'][0].update(text='Unapproved new text.', voice_version=2)
        issues = M.validate_project(p)
        self.assertTrue(any('approved script line' in x for x in issues))
        self.assertTrue(any('ownership or version' in x for x in issues))

    def test_audio_handles_must_fit(self):
        p = project(); p['shots'][0]['dialogue'][0]['audio_duration_seconds'] = 7.5
        self.assertTrue(any('do not fit' in x for x in M.validate_project(p)))

    def test_narration_does_not_drive_visible_mouth(self):
        p = project(); p['voices']['VO1']['owner'] = 'NARRATOR'
        p['script']['lines']['L1']['speaker_id'] = 'NARRATOR'
        p['shots'][0]['dialogue'][0].update(speaker_id='NARRATOR', kind='narration')
        p['shots'][0]['audio_refs'][0]['owner'] = 'NARRATOR'
        self.assertTrue(any('mouth rule' in x for x in M.validate_project(p)))
        p['shots'][0]['mouth_rules']['CH1'] = 'closed'
        self.assertEqual(M.validate_project(p), [])

    def test_timeline_overlap_and_duplicate_shot(self):
        p = project(); p['shots'].append(copy.deepcopy(p['shots'][0]))
        issues = M.validate_project(p)
        self.assertTrue(any('shot_ids' in x for x in issues))
        self.assertTrue(any('gap/overlap' in x for x in issues))

    def test_audition_requires_voice_profile_choice(self):
        p = project()
        self.assertTrue(any('profile' in x for x in M.validate_project(p, 'auditions')))
        p['voices']['VO1']['profile_approved'] = True
        self.assertEqual(M.validate_project(p, 'auditions'), [])


class RecoveryChecks(unittest.TestCase):
    def test_policy_is_not_a_retry(self):
        self.assertEqual(M.classify_error('OutputAudioSensitiveContentDetected.PolicyViolation timeout'), 'policy_stop')
        self.assertEqual(M.classify_error('InputImageSensitiveContentDetected.PolicyViolation'), 'policy_stop')
        self.assertEqual(M.classify_error('OutputVideoSensitiveContentDetected.PolicyViolation'), 'policy_stop')

    def test_observed_parameter_errors_are_distinct(self):
        self.assertEqual(M.classify_error('InvalidParameter audio total duration must be <=30.2'), 'fix_measured_audio')
        self.assertEqual(M.classify_error('InvalidParameter.TaskTypeConstraint ratio video extension'), 'fix_task_ratio')
        self.assertEqual(M.classify_error('503 temporarily unavailable'), 'query_then_bounded_retry')


class CompletionChecks(unittest.TestCase):
    def complete_project(self):
        p = project(); p['film_ratio'] = '16:9'; p['table']['expected_duration_seconds'] = 8
        p['shots'][0].update(status='checked', output_asset_id='real-shot-video')
        p['jobs'] = [{'status': 'succeeded'}]
        p['final_video'] = {'asset_id': 'real-final-video', 'ready': True, 'playback_checked': True,
                            'ratio': '16:9', 'duration_seconds': 8, 'shot_ids': ['SC01_SH01'],
                            'audio_verified': True}
        return p

    def test_checked_final_film(self):
        self.assertEqual(M.validate_completion(self.complete_project()), [])

    def test_submitting_first_job_is_not_completion(self):
        p = project(); p['jobs'] = [{'status': 'running'}]
        issues = M.validate_completion(p)
        self.assertTrue(any('pending_job' in x for x in issues))
        self.assertTrue(any('final_video' in x for x in issues))

    def test_extension_prefix_must_not_duplicate_shots(self):
        p = self.complete_project(); p['final_video']['shot_ids'] *= 2
        self.assertTrue(any('final_order' in x for x in M.validate_completion(p)))

    def test_audio_and_duration_are_real_delivery_checks(self):
        p = self.complete_project(); p['final_video'].update(audio_verified=False, duration_seconds=5)
        issues = M.validate_completion(p)
        self.assertTrue(any('final_audio' in x for x in issues))
        self.assertTrue(any('final_duration' in x for x in issues))


if __name__ == '__main__':
    unittest.main()
