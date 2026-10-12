# Führt die Alt-Texte aus tools/alt/out-*.json zu src/data/alts.json zusammen: {slug: [de, en]}
import json, glob, os
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(os.path.dirname(H))
A = {}
for f in sorted(glob.glob(os.path.join(H, 'out-*.json'))):
    A.update(json.load(open(f, encoding='utf-8')))
json.dump(A, open(os.path.join(R, 'src/data/alts.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
print(len(A))
