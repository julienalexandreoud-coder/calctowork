import json, os, glob
CALC = r'C:\Microsaas\obra\src\calculators'
REPLS = [('Obtener','Obter'),('obtener','obter'),('herramienta','ferramenta'),
    ('herramientas','ferramentas'),('hormigon','betao'),('hormig\u00f3n','betao'),
    ('seg\u00fan','segundo'),('segun','segundo'),('donde','onde'),('Donde','Onde'),
    ('desperdicio','desperdicio'),('Desperdicio','Desperdicio'),
    ('merma','quebra'),('Merma','Quebra')]
upd=0
for fp in sorted(glob.glob(os.path.join(CALC, '*.json'))):
    if 'bak' in fp or 'monolithic' in fp: continue
    with open(fp,'r',encoding='utf-8-sig') as f: c=json.load(f)
    pt=c.setdefault('i18n',{}).setdefault('pt',{}); changed=False
    for field in ['steps','mistakes']:
        val=pt.get(field,[])
        if isinstance(val,list):
            new=[]
            for s in val:
                t=str(s)
                for old,new_s in REPLS: t=t.replace(old,new_s)
                new.append(t)
            if new!=val: pt[field]=new; changed=True
    for field in ['result_context','example_label','formula_display']:
        val=pt.get(field,'')
        if isinstance(val,str) and val:
            new=val
            for old,new_s in REPLS: new=new.replace(old,new_s)
            if new!=val: pt[field]=new; changed=True
    if changed:
        with open(fp,'w',encoding='utf-8',newline='\n') as f: json.dump(c,f,ensure_ascii=False,indent=2)
        upd+=1
print(f'Fixed {upd}')
