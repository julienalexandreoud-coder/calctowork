#!/usr/bin/env python3
"""Fix Python-syntax formulas to valid JavaScript."""

import json, os, glob, re

CALC_DIR = r"C:\Microsaas\obra\src\calculators"

FIXES = {
    "1054": 'var n=parseFloat(inputs.n)||0,r=parseFloat(inputs.r)||0;function fact(x){var f=1;for(var i=2;i<=x;i++)f*=i;return f;}return{combinaciones:Math.floor(fact(n)/(fact(r)*fact(n-r))),permutaciones:Math.floor(fact(n)/fact(n-r))};',
    "1091": 'var t=inputs.texto||"";return{con_espacios:t.length,sin_espacios:t.replace(/ /g,"").length,palabras:t.trim()?t.trim().split(/\\s+/).length:0};',
    "1092": 'var d=parseFloat(inputs.dias_totales)||0,f=parseFloat(inputs.festivos)||0;var w=Math.floor(d/7)*2;return{dias_habiles:Math.max(0,d-w-f)};',
    "1090": 'var L=parseFloat(inputs.longitud)||0,C=parseFloat(inputs.conjunto_caracteres)||1;var e=L*Math.log2(C);var fuerza=e<40?"D\\u00e9bil":e<60?"Media":"Fuerte";return{entropia:e,fuerza:fuerza};',
    "1060": 'var s=inputs.sexo||"",c=parseFloat(inputs.cintura)||0,cu=parseFloat(inputs.cuello)||0,ca=parseFloat(inputs.cadera)||0,alt=parseFloat(inputs.altura_cm)||0;var gc;if(s=="hombre")gc=495/(1.0324-0.19077*Math.log10(c-cu)+0.15456*Math.log10(alt))-450;else gc=495/(1.29579-0.35004*Math.log10(c+ca-cu)+0.22100*Math.log10(alt))-450;return{grasa_corporal:+gc.toFixed(1)};',
    "1089": 'var pr=parseFloat(inputs.punto_rocio)||0,t=parseFloat(inputs.temperatura)||0;var hr=100*(Math.exp(17.625*pr/(243.04+pr))/Math.exp(17.625*t/(243.04+t)));return{humedad_relativa:+hr.toFixed(1)};',
    "1067": 'var pv=parseFloat(inputs.precio_venta)||0,pc=parseFloat(inputs.precio_compra)||0,ti=parseFloat(inputs.tasa_impuesto)||0;var g=pv-pc;return{ganancia:+g.toFixed(2),impuesto:+Math.max(0,g*ti/100).toFixed(2)};',
    "1070": 'var f=inputs.formula_quimica||"";var parts=f.split("+");var s=0;for(var i=0;i<parts.length;i++){var v=parseFloat(parts[i]);if(!isNaN(v))s+=v;}return{masa_molar:+s.toFixed(2)};',
    "1071": 'var h=parseFloat(inputs.concentracion_h)||0;var ph=-Math.log10(h);return{ph:+ph.toFixed(2),poh:+(14-ph).toFixed(2)};',
    "1050": 'var n=parseFloat(inputs.n)||3,l=parseFloat(inputs.lado)||1;var a=(n*l*l)/(4*Math.tan(Math.PI/n));return{area:+a.toFixed(2),perimetro:+(n*l).toFixed(1)};',
    "1064": 'var p=parseFloat(inputs.peso)||70,obj=inputs.objetivo||"mantener";var f=1.2;if(obj=="ganar_musculo")f=1.6;else if(obj=="perder_peso")f=2.0;return{proteina_min:+(p*0.8).toFixed(1),proteina_max:+(p*2.2).toFixed(1),proteina_recomendada:+(p*f).toFixed(1)};',
    "1053": 'var a1=parseFloat(inputs.a1)||1,r=parseFloat(inputs.r)||1,n=parseFloat(inputs.n)||1;var suma;if(Math.abs(r-1)<1e-10)suma=a1*n;else suma=a1*(1-Math.pow(r,n))/(1-r);return{suma:+suma.toFixed(2),termino_n:+(a1*Math.pow(r,n-1)).toFixed(2)};',
    "1061": 'var p=parseFloat(inputs.peso)||70,alt=parseFloat(inputs.altura_cm)||170,ed=parseFloat(inputs.edad)||30,s=inputs.sexo||"hombre";var tmb;if(s=="hombre")tmb=10*p+6.25*alt-5*ed+5;else tmb=10*p+6.25*alt-5*ed-161;return{tmb:+tmb.toFixed(0)};',
}

# Fix "from math import" Python patterns
def fix_python_formula(formula):
    # Remove Python imports
    formula = re.sub(r'from math import \w+\s*', '', formula)
    # log10 -> Math.log10
    formula = re.sub(r'(?<!Math\.)(?<![\w.])log10\s*\(', 'Math.log10(', formula)
    # exp -> Math.exp
    formula = re.sub(r'(?<!Math\.)(?<![\w.])exp\s*\(', 'Math.exp(', formula)
    # log2 -> Math.log2
    formula = re.sub(r'(?<!Math\.)(?<![\w.])log2\s*\(', 'Math.log2(', formula)
    # tan -> Math.tan
    formula = re.sub(r'(?<!Math\.)(?<![\w.])tan\s*\(', 'Math.tan(', formula)
    # Python // -> JS Math.floor
    formula = re.sub(r'(\w+)\s*//\s*(\d+)', r'Math.floor(\1/\2)', formula)
    formula = re.sub(r'(\w+)\s*//\s*(\w+)', r'Math.floor(Number(\1)/Number(\2))', formula)
    # sum() -> manual
    # max( -> Math.max(
    formula = re.sub(r'(?<!Math\.)(?<![\w.])max\s*\(', 'Math.max(', formula)
    # Python conditional expression -> JS ternary
    # Already handled by direct replacements above
    # length( -> .length
    formula = re.sub(r'length\(inputs\.(\w+)\)', r'inputs.\1.length', formula)
    # Remove empty imported lines
    formula = re.sub(r'\n\s*\n', '\n', formula)
    formula = formula.strip()
    return formula


def main():
    updated = 0
    for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
        name = os.path.basename(fp)
        if "bak" in fp or "monolithic" in fp or name == "calculators.json":
            continue
        
        with open(fp, "r", encoding="utf-8-sig") as f:
            calc = json.load(f)
        
        cid = calc.get("id", "")
        formula = calc.get("formula", "")
        
        if cid in FIXES:
            calc["formula"] = FIXES[cid]
            with open(fp, "w", encoding="utf-8", newline="\n") as f:
                json.dump(calc, f, ensure_ascii=False, indent=2)
            updated += 1
            print(f"  Fixed {cid} {name}")
            continue
        
        if not formula:
            continue
        
        new_formula = fix_python_formula(formula)
        if new_formula != formula:
            calc["formula"] = new_formula
            with open(fp, "w", encoding="utf-8", newline="\n") as f:
                json.dump(calc, f, ensure_ascii=False, indent=2)
            updated += 1
            print(f"  Patched {cid} {name}")
    
    print(f"\nFixed {updated} formulas")


if __name__ == "__main__":
    main()
