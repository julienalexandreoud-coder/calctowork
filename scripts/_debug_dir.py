from pathlib import Path
p = Path(r'C:\Microsaas\obra\src\calculators')
print(f'exists={p.exists()}')
if p.exists():
    files = list(p.glob('*.json'))
    print(f'files={len(files)}')
    if files:
        print(f'first={files[0].name}')
    else:
        # Check if there are any files at all
        all_files = list(p.iterdir())
        print(f'all entries={len(all_files)}')
        for e in all_files[:5]:
            print(f'  {e.name} is_file={e.is_file()}')
