"""Rebuilds data.js from the CSVs in ../data.

Run from the repo root:  python3 scripts/build_data.py
Edit or extend the CSVs (same column headers) and re-run; index.html reads data.js at load.
"""
import csv, glob, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = []
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'gamelog_*.csv'))):
    rows += list(csv.DictReader(open(f)))
keys = ['seasonEnd','type','date','team','opp','home','result','teamScore','oppScore','ot','min','pts',
        'oreb','dreb','reb','ast','stl','blk','tov','pf','fgm','fga','tpm','tpa','ftm','fta']
TEXT = {'type','date','team','opp','result'}
games = [[r[k] if k in TEXT else int(r[k]) for k in keys] for r in rows]
games.sort(key=lambda g: g[2])
comps = {}
for c in csv.DictReader(open(os.path.join(ROOT, 'data', 'comps.csv'))):
    comps.setdefault(c['player'], {'height': c['height']})
    comps[c['player']][c['type']] = {k: (float(c[k]) if c[k] != '' else None)
                                     for k in ['games','mpg','ppg','rpg','apg','spg','bpg','topg','fgp','tpp','ftp']}
ranks = {}
for r in csv.DictReader(open(os.path.join(ROOT, 'data', 'iverson_ranks.csv'))):
    ranks.setdefault(r['type'], {})[r['category']] = {'value': r['value'], 'rank': r['rank']}
out = {'keys': keys, 'games': games, 'comps': comps, 'ranks': ranks,
       'seasons': [{'end': y, 'label': f"{y-1}-{str(y)[2:]}"} for y in range(1997, 2011)],
       'source': 'landofbasketball.com game logs, career stats and all-time rankings (fetched 2026-10-14)'}
js = ('// Allen Iverson career data — generated from landofbasketball.com game logs.\n'
      '// keys = column order for each row in games.\n'
      'window.AI_DATA = ' + json.dumps(out, separators=(',', ':')) + ';\n')
open(os.path.join(ROOT, 'data.js'), 'w').write(js)
print(f'wrote data.js: {len(games)} games, {len(comps)} comparison players')
