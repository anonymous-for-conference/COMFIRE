#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

import mutation_pipeline as mp

RUN = Path('/data/zlyuaj/coding_agent/EviFuzz_SWE_live/RIPPLE/mutation_result/live-relational-20260928-g')
ROW = {'agent': 'SWE_Agent', 'instance_id': 'deepset-ai__haystack-8799',
       'repo': 'deepset-ai/haystack', 'base_commit': '503d275ade85e04efed787ec421bdc55a5a77abf'}


def main() -> None:
    clusters, docs = mp.clusters_for(ROW, 3, 20260932)
    # Choose only ordinary prose units. Replacements keep directive names,
    # indentation, line count, and Python tokens unchanged.
    choices = [
        (clusters[0], clusters[0]['items'][0], 'R3',
         ' Make sure all the values contained in\n            this dictionary can be serialized by `PipelineTemplate` and deserialized by `PipelineBase` if you wish to save this `Pipeline` to file.\n'),
        (clusters[1], clusters[1]['items'][0], 'R1',
         "        It's `PipelineTemplate`'s responsibility to make sure this method can be called at every `Pipeline.run()`\n        without re-initializing everything.\n"),
        (clusters[2], clusters[2]['items'][1], 'R2',
         '            How many times the `Pipeline` can run different Components.\n'),
    ]
    target = RUN / 'patches' / ROW['agent'] / ROW['instance_id']
    target.mkdir(parents=True, exist_ok=True)
    mirror = mp.BIG_REPOS / (ROW['repo'].replace('/', '__') + '.git')
    with tempfile.TemporaryDirectory(prefix='manual-relational-', dir=RUN / 'staging') as td:
        repo = Path(td) / 'repo'
        subprocess.run(['git', 'clone', '--shared', '-q', str(mirror), str(repo)], check=True)
        subprocess.run(['git', 'checkout', '--detach', '-q', ROW['base_commit']], cwd=repo, check=True)
        changes = []
        by_doc = {}
        for cluster, item, operator, replacement in choices:
            doc = docs[item['documentation_id']]
            path = repo / item['file']
            source = doc['documentation_source']
            file_text = path.read_text()
            lines = file_text.splitlines(keepends=True)
            start = sum(len(x) for x in lines[:int(doc['documentation_start_line']) - 1])
            assert file_text[start:start + len(source)] == source
            assert source[item['source_start_offset']:item['source_end_offset']] == item['unit_source']
            by_doc.setdefault((path, start, source), []).append((item, replacement, operator, cluster))
        for (path, start, source), edits in by_doc.items():
            updated = source
            for item, replacement, operator, cluster in sorted(edits, key=lambda x: x[0]['source_start_offset'], reverse=True):
                a, b = item['source_start_offset'], item['source_end_offset']
                updated = updated[:a] + replacement + updated[b:]
                changes.append({'cluster_id': cluster['cluster_id'], 'operator': operator,
                    'unit_id': item['unit_id'], 'documentation_id': item['documentation_id'],
                    'file': item['file'], 'qualname': item['qualname'], 'line': item['file_line_start'],
                    'original': item['unit_text'], 'replacement': replacement.strip(),
                    'original_source': item['unit_source'], 'replacement_source': replacement,
                    'source_start_offset': a, 'source_end_offset': b})
            value = file_text[:start] + updated + file_text[start + len(source):]
            path.write_text(value)
        files = sorted({str(x['file']) for x in changes})
        patch = subprocess.run(['git', 'diff', '--binary', '--', *files], cwd=repo,
                               check=True, text=True, capture_output=True).stdout
    patch_path = target / 'mutation.patch'
    patch_path.write_text(patch)
    meta = {'case': ROW, 'clusters': [{'cluster_id': c['cluster_id'], 'operator': op,
             'applicable_operators': [op]} for c, item, op, rep in choices],
            'changes': changes, 'files': files, 'patch': str(patch_path),
            'sha256': hashlib.sha256(patch.encode()).hexdigest(), 'status': 'manual_structured_fallback'}
    (target / 'mutation.json').write_text(json.dumps(meta, indent=2) + '\n')
    flat = RUN / 'worker_patches' / 'swe-agent' / ROW['instance_id']
    flat.mkdir(parents=True, exist_ok=True)
    shutil.copy2(patch_path, flat / 'mutation.patch')
    shutil.copy2(target / 'mutation.json', flat / 'mutation.json')
    subprocess.run(['git', 'apply', '--check', str(patch_path)], cwd=repo if False else mp.BIG_REPOS / (ROW['repo'].replace('/', '__') + '.git'), check=False)
    print(json.dumps({'patch': str(patch_path), 'bytes': patch_path.stat().st_size,
                      'sha256': meta['sha256'], 'changes': len(changes)}, indent=2))


if __name__ == '__main__':
    main()
