import json
calcs = json.load(open('src/calculators/calculators.json', encoding='utf-8'))['calculators']
for c in calcs:
    if c['id'] in ('200', '400', '500', '210', '300', '700', '800', '900', '100', '600'):
        print("ID %s: %s (%s)" % (c['id'], c['slug'], c['block_slug']))
        print("  Inputs: %s" % [i['id'] for i in c.get('inputs', [])])
        print("  Outputs: %s" % [o['id'] for o in c.get('outputs', [])])
        print("  Formula: %s..." % c.get('formula', '')[:60])
        print()
