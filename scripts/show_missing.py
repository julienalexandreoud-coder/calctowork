import json

calcs = json.load(open('src/calculators/calculators.json', encoding='utf-8'))['calculators']
for c in calcs:
    if c['id'] in ('700', '800', '802', '900'):
        print("ID %s: %s" % (c['id'], c['slug']))
        inputs = [i['id'] for i in c.get('inputs', [])]
        outputs = [o['id'] for o in c.get('outputs', [])]
        print("  Inputs: %s" % inputs)
        print("  Outputs: %s" % outputs)
        print("  Formula: %s..." % c.get('formula', '')[:80])
        print()
