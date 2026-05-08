import csv, os
os.chdir(r'c:\Microsaas\obra')

with open('scripts/mismatch_report.csv', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

with_signals = [r for r in rows if r['wrong_signals']]
without = [r for r in rows if not r['wrong_signals']]
score0_no_signal = [r for r in without if float(r['match_score']) == 0.0]

print(f'Total mismatches: {len(rows)}')
print(f'With wrong signals (definite): {len(with_signals)}')
print(f'Vocabulary mismatch only: {len(without)}')
print(f'Score=0 but no wrong signal: {len(score0_no_signal)}')
print()
print('Sample wrong_signals:')
for r in with_signals[:8]:
    print(f'  [{r["calc_id"]}] {r["lang"]}: {r["wrong_signals"][:80]}')
print()
print('Unique IDs with wrong signals:', len(set(r["calc_id"] for r in with_signals)))

# Write filtered IDs for Phase 4
genuine_ids = sorted(set(r["calc_id"] for r in with_signals))
with open('scripts/mismatch_ids.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(genuine_ids))
print(f'\nUpdated mismatch_ids.txt with {len(genuine_ids)} genuine mismatches.')
