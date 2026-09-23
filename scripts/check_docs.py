#!/usr/bin/env python3
"""Check local Markdown links and pinned manifest consistency; no network."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
errors=[]
for f in [ROOT/'README.md', *sorted((ROOT/'docs').glob('*.md'))]:
    for link in re.findall(r'\]\(([^)]+)\)', f.read_text()):
        if '://' in link or link.startswith('#'):
            continue
        if not (f.parent / link.split('#')[0]).exists():
            errors.append(f'{f.name}: missing {link}')
m=json.loads((ROOT/'data/print-manifest.json').read_text())
p=[x for x in m['assets'] if x['category']=='print_candidate']
assert len(m['assets'])==38 and sum(x['quantity'] for x in m['assets'])==70
assert len(p)==30 and sum(x['quantity'] for x in p)==36
assert len({x['name'] for x in m['assets']})==len(m['assets'])
for x in m['assets']:
    assert re.fullmatch('[0-9a-f]{40}',x['git_blob_sha'])
    assert m['commit'] in x['source_url']
    assert x['scale']==1000
    assert x['quantity']>0
if errors:
    raise SystemExit('\n'.join(errors))
print('PASS: local Markdown links; 38 types/70 visual instances; 30 print types/36 pieces; pinned asset hashes.')
f=json.loads((ROOT/'data/fange-print-inventory.json').read_text())
lock=json.loads((ROOT/'data/fange-lock.json').read_text())
assert f['commit']==lock['commit']
assert f['unit']=='millimeter' and f['build_items']==67
assert [len(p['instances']) for p in f['plates']]==[4,5,19,34,3]
assert len(f['unassigned_objects'])==2
assert f['sha256']==lock['files'][f['path']]
assert all(re.fullmatch('[0-9a-f]{64}',v) for v in lock['files'].values())
assert re.fullmatch('[0-9a-f]{64}',lock['image_sha256_published'])
print('PASS: FanGe pinned source, 5 plates/65 assigned + 2 unassigned objects, file hashes.')
