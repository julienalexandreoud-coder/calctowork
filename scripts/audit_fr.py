# -*- coding: utf-8 -*-
import json, os, glob
CALC = r'C:\Microsaas\obra\src\calculators'
ES = ['Multiplicar','Calcular','Determinar','Introducir','Obtener','Verificar','Usar','Los ','Las ',
      'gratis','gratuita','herramienta','necesario','desperdicio','merma','calcula','calcular',
      'introduce','resultado','unidad','utilizando','usando','este ','esta ','tiene','tienen',
      'puede','pueden','cada ','cuando ','como ','donde','para ','seg\u00fan','mismo','peque\u00f1o']
total=0;issues=0
for fp in sorted(glob.glob(os.path.join(CALC, '*.json'))):
    if 'bak' in fp or 'monolithic' in fp: continue
    with open(fp,'r',encoding='utf-8-sig') as f: calc=json.load(f)
    total+=1
    fr=calc.get('i18n',{}).get('fr',{})
    allt=''
    for field in ['steps','mistakes']:
        val=fr.get(field,[])
        if isinstance(val,list):
            for s in val:
                if isinstance(s,dict):
                    for k,v in s.items():
                        if isinstance(v,str): allt+=v+' '
                elif isinstance(s,str): allt+=s+' '
    for field in ['result_context','example_label','formula_display','description']:
        v=fr.get(field,'')
        if isinstance(v,str): allt+=v+' '
    found=[p for p in ES if p in allt]
    if found: issues+=1
print(f'{issues}/{total} have Spanish words in French')
