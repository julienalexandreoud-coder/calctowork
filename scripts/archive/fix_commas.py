from pathlib import Path
p = Path('scripts/tools_config.py')
lines = p.read_text(encoding='utf-8').splitlines()
start = None
end = None
for i, line in enumerate(lines):
    if '"id": "110"' in line:
        start = i
    if '"id": "512"' in line:
        end = i
        break

if start and end:
    for i in range(start, end):
        stripped = lines[i].rstrip()
        if stripped.endswith('}}') and not stripped.endswith('}},'):
            lines[i] = stripped + ','
    p.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'Fixed lines {start+1} to {end}')
else:
    print('Range not found')
