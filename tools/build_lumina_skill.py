#!/usr/bin/env python3
"""Bundle the complete style specifications for Lumina's text-file importer.

Run from anywhere: python3 tools/build_lumina_skill.py [--check] [--zip PATH]
The uploaded skill contains data and instructions only; this maintainer script
stays outside it. Style fragments are byte-verifiable against the library.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
LIB = ROOT / 'xianlin-lu'
SKILL = ROOT / 'skills' / 'lumina-canvas-film'
CAP = 19000  # UTF-16 code units, below both importer limits shown by the user
TAIL = '\n<!-- END STYLE PAGE -->\n'
REPO = 'https://github.com/XianlinLu/Code-Cinema-Atlas'


def units(text):
    return len(text.encode('utf-16-le')) // 2


def blocks(text):
    """Keep paragraphs and fenced examples together, preserving all characters."""
    block = []
    fence = None
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        mark = re.match(r'(`{3,}|~{3,})', stripped)
        if mark:
            if fence is None:
                fence = mark.group(1)
            elif mark.group(1)[0] == fence[0] and len(mark.group(1)) >= len(fence):
                fence = None
        block.append(line)
        if not line.strip() and fence is None:
            yield ''.join(block)
            block = []
    if block:
        yield ''.join(block)


def generate():
    order = re.findall(r'\[`([^`]+)`\]\([^)]*STYLE\.md\)', (LIB / 'styles/README.md').read_text())
    assert len(order) == len(set(order)) == 51, 'Review catalog changes before changing the bundled style count'
    assert set(order) == {p.parent.name for p in (LIB / 'styles').glob('*/STYLE.md')
                          if not p.parent.name.startswith('_')}, 'Index and source styles differ'
    revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    workflow_sources = {name: hashlib.sha256((LIB / name).read_bytes()).hexdigest()
                        for name in ('AGENTS.md', 'DIRECTOR.md', 'TECHNIQUE.md')}
    old_manifest = SKILL / 'references/style-manifest.json'
    # Keep the pinned library revision stable across unrelated skill-only commits.
    if old_manifest.exists():
        previous = json.loads(old_manifest.read_text())
        same = all(hashlib.sha256((LIB / f'styles/{slug}/STYLE.md').read_bytes()).hexdigest()
                   == previous.get('styles', {}).get(slug, {}).get('sha256') for slug in order)
        if same and previous.get('workflow_sources') == workflow_sources:
            revision = previous['library_revision']
    manifest = {'format': 1, 'library_repository': REPO, 'library_revision': revision,
                'style_count': len(order), 'offsets': 'Unicode code points; end-exclusive; fragments concatenate in listed order',
                'workflow_sources': workflow_sources, 'styles': {}}
    generated = {}
    page_no = 1
    page = '# Complete style specifications 01\n\n'
    active = None
    for slug in order:
        raw = (LIB / f'styles/{slug}/STYLE.md').read_text()
        entry = {'sha256': hashlib.sha256(raw.encode()).hexdigest(), 'parts': []}
        manifest['styles'][slug] = entry
        for block in blocks(raw):
            marker = f'\n<!-- STYLE: {slug} -->\n\n' if active != slug else ''
            if units(page + marker + block + TAIL) > CAP:
                generated[f'references/style-specs-{page_no:02}.md'] = page + TAIL
                page_no += 1
                page = f'# Complete style specifications {page_no:02}\n\n'
                active = None
                marker = f'\n<!-- STYLE: {slug} -->\n\n'
            assert units(page + marker + block + TAIL) <= CAP, f'Atomic block too large: {slug}'
            page += marker
            file = f'references/style-specs-{page_no:02}.md'
            start = len(page)
            page += block
            if active == slug:
                entry['parts'][-1][2] = len(page)
            else:
                entry['parts'].append([file, start, len(page)])
            active = slug
    generated[f'references/style-specs-{page_no:02}.md'] = page + TAIL
    for slug, entry in manifest['styles'].items():
        restored = ''.join(generated[file][start:end] for file, start, end in entry['parts'])
        assert restored == (LIB / f'styles/{slug}/STYLE.md').read_text(), slug
        assert hashlib.sha256(restored.encode()).hexdigest() == entry['sha256'], slug
    generated['references/style-manifest.json'] = json.dumps(manifest, ensure_ascii=False, separators=(',', ':')) + '\n'
    lines = ['# Style index / 风格索引', '',
             'All 51 styles are included with their full specifications. Names and categories below are canonical.',
             'When the style is unknown, show ALL categories and names in the user\'s language, recommend 2–3, then use the native style picker.',
             'For the selected slug, read EVERY listed spec file and extract its `<!-- STYLE: slug -->` segment in file order.',
             'A segment ends at the next STYLE marker or END STYLE PAGE marker. Join its pieces without dropping any section.',
             'Do not load the other styles. `style-manifest.json` records exact fragment offsets and SHA-256 checksums.',
             'Paths inside specifications (`demo/`, `DEMO.md`, etc.) are relative to that style in the library, not this import package.',
             f'Library: {REPO}/tree/{revision}/xianlin-lu',
             'Gallery source: the library\'s `styleboard/` folder. Link a playable gallery only if it is available and verified; label a source-directory link as source.',
             'Style metadata below omits demo story descriptions so treatments can be written independently.', '']
    last_category = None
    for slug in order:
        meta = json.loads((LIB / f'styles/{slug}/style.json').read_text())
        category = (meta['category_en'], meta['category_cn'])
        if category != last_category:
            if last_category is not None:
                lines.append('')
            lines += [f'## {category[0]} / {category[1]}', '',
                      '| English | 中文 | Slug | Fits / use cases | Full specification files |',
                      '|---|---|---|---|---|']
        parts = manifest['styles'][slug]['parts']
        files = ', '.join(f'[{Path(file).name}]({Path(file).name})' for file, _, _ in parts)
        uses = '; '.join(meta.get('uses', [])).replace('|', '/')
        lines.append(f"| {meta['en']} | {meta['cn']} | {slug} | {uses} | {files} |")
        last_category = category
    generated['references/style-index.md'] = '\n'.join(lines) + '\n'
    generated['references/director.md'] = (LIB / 'DIRECTOR.md').read_text()
    generated['references/technique.md'] = (LIB / 'TECHNIQUE.md').read_text()
    for name, text in generated.items():
        assert units(text) <= CAP, (name, units(text))
    return generated


def validate(generated, check):
    for relative, content in generated.items():
        path = SKILL / relative
        if check:
            assert path.exists() and path.read_text() == content, f'Out of date: {relative}'
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
    expected = {SKILL / p for p in generated}
    for stale in (SKILL / 'references').glob('style-specs-*.md'):
        if stale not in expected:
            if check:
                raise AssertionError(f'Stale style shard: {stale}')
            stale.unlink()
    files = sorted(p for p in SKILL.rglob('*') if p.is_file())
    assert len(files) <= 50, f'Import has {len(files)} files'
    for path in files:
        assert path.suffix in {'.md', '.txt', '.json', '.yaml', '.yml'}, path
        for part in path.relative_to(SKILL).parts:
            assert len(part) <= 64 and re.fullmatch(r'[A-Za-z0-9_-]+(?:\.[a-z]+)?', part), part
        assert units(path.read_text()) <= CAP, (path, units(path.read_text()))
    print(f'{len(files)} files; 51 complete styles; maximum {max(units(p.read_text()) for p in files)} UTF-16 units/file; hashes verified')
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--zip', type=Path)
    args = parser.parse_args()
    files = validate(generate(), args.check)
    if args.zip:
        args.zip.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(args.zip, 'w', zipfile.ZIP_DEFLATED) as archive:
            for path in files:
                archive.write(path, path.relative_to(SKILL).as_posix())
        print(f'Import package: {args.zip}')


if __name__ == '__main__':
    main()
