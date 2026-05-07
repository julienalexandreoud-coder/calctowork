from pathlib import Path
d = Path(r'C:\Microsaas\obra\src\content\en')
missing = ['402','403','200','201','203','210','500','501','700','800','802','600','900']
for mid in missing:
    f = d / f'{mid}.html'
    print(f'{mid}.html: exists={f.exists()}')
