#!/usr/bin/env python3
"""Fetch pinned upstream binary STL files and convert metres to millimetres.
No third-party Python dependencies. No hardware access. Not a mesh repair tool.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import struct
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def convert_stl(data):
    if len(data) < 84:
        raise ValueError('Not a binary STL')
    count = struct.unpack_from('<I', data, 80)[0]
    if len(data) != 84 + count * 50 or count == 0:
        raise ValueError('Unsupported ASCII or malformed/empty binary STL')
    out = bytearray(data)
    lo, hi = [math.inf] * 3, [-math.inf] * 3
    for i in range(count):
        for j in range(3):
            offset = 84 + 50 * i + 12 + 12 * j
            xyz = struct.unpack_from('<3f', data, offset)
            if not all(math.isfinite(v) for v in xyz):
                raise ValueError('Non-finite vertex')
            scaled = [v * 1000 for v in xyz]
            struct.pack_into('<3f', out, offset, *scaled)
            for k, v in enumerate(scaled):
                lo[k] = min(lo[k], v)
                hi[k] = max(hi[k], v)
    return bytes(out), [round(hi[k] - lo[k], 4) for k in range(3)], count


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--list', action='store_true', help='List candidates, no network')
    ap.add_argument('--download', action='store_true', help='Fetch and convert selected candidates')
    ap.add_argument('--only', nargs='+', help='Exact stem names from the manifest')
    args = ap.parse_args()
    manifest = json.loads((ROOT / 'data/print-manifest.json').read_text())
    candidates = {x['name']: x for x in manifest['assets'] if x['category'] == 'print_candidate'}
    names = args.only or list(candidates)
    unknown = set(names) - set(candidates)
    if unknown:
        ap.error('Not print candidates: ' + ', '.join(sorted(unknown)))
    if not args.download:
        for name in names:
            x = candidates[name]
            print(f'{name}.stl\tqty={x["quantity"]}\t{x["material_suggestion"]}')
        print(f'{len(names)} types; {sum(candidates[n]["quantity"] for n in names)} pieces')
        return
    target = ROOT / 'build/prints'
    for sub in ['original', 'mm']:
        (target / sub).mkdir(parents=True, exist_ok=True)
    report_path = target / 'report.json'
    old = json.loads(report_path.read_text()) if report_path.exists() else {}
    reports = {r['name']: r for r in old.get('files', [])} if old.get('commit') == manifest['commit'] else {}
    for name in names:
        x = candidates[name]
        original = target / 'original' / (name + '.stl')
        if original.exists():
            data = original.read_bytes()
        else:
            req = urllib.request.Request(x['source_url'], headers={'User-Agent': 'MicroDuckDIY/0.1'})
            with urllib.request.urlopen(req, timeout=60) as response:
                data = response.read()
        digest = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        if digest != x['git_blob_sha'] or len(data) != x['size_bytes']:
            raise ValueError(f'{name}: source hash/size mismatch; remove corrupt local cache and retry')
        converted, dimensions, triangles = convert_stl(data)
        original.write_bytes(data)
        (target / 'mm' / (name + '.stl')).write_bytes(converted)
        reports[name] = dict(name=name,quantity=x['quantity'],dimensions_mm=dimensions,
                            triangles=triangles,source_git_blob_sha=digest,
                            output_sha256=hashlib.sha256(converted).hexdigest(),
                            units='mm',physical_fit_verified=False,mesh_manifold_verified=False)
        report_path.write_text(json.dumps(dict(commit=manifest['commit'],
                              files=list(reports.values())), indent=2) + '\n')
        print(f'{name}: {dimensions} mm, qty {x["quantity"]}, hash OK', flush=True)
    (target / 'SOURCE-NOTICE.txt').write_text(
        'Original authors: Pollen Robotics and upstream contributors.\n'
        f'Source: https://github.com/{manifest["repository"]}/tree/{manifest["commit"]}\n'
        + manifest['license_note'] + '\n'
        + 'mm/ derivatives: vertex coordinates scaled x1000; no geometry repair.\n'
        + 'Material suggestions and physical fit are NOT validated.\n')
    print(f'Finished: {target}. Slicer scale 100%; use manifest quantities.')


if __name__ == '__main__':
    main()
