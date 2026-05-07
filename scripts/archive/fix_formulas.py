#!/usr/bin/env python3
"""Fix all 54 calculators with runtime formula errors."""

import json, os, glob, re

CALC_DIR = r"C:\Microsaas\obra\src\calculators"

def fix_formula(calc):
    """Fix common formula bugs."""
    formula = calc.get("formula", "")
    if not formula:
        return formula
    
    inputs = calc.get("inputs", [])
    input_ids = {i.get("id", "") for i in inputs}
    
    fixed = formula
    
    # Fix 1: Replace bare variable names with inputs.xxx
    # Variables that look like they should be inputs (Spanish/English words matching input IDs)
    for iid in sorted(input_ids, key=len, reverse=True):  # Longest first to avoid partial matches
        # Only replace if the variable appears as a standalone word (not after . or as part of longer name)
        # Pattern: not preceded by 'inputs.' or '.' 
        pattern = r'(?<!inputs\.)(?<!\.)(?<!\w)' + re.escape(iid) + r'(?!\w)'
        # Check if this bare variable name appears
        if re.search(pattern, fixed):
            # Only replace if it's not already inputs.xxx
            if f"inputs.{iid}" not in fixed:
                # Replace bare variable with inputs.xxx
                fixed = re.sub(pattern, f"inputs.{iid}", fixed)
    
    # Fix 2: lowercase 'math' -> 'Math'
    fixed = re.sub(r'\bmath\.', 'Math.', fixed)
    
    # Fix 3: 'erf' -> custom implementation, or 'Math.erf' -> approximation
    fixed = re.sub(r'\berf\b(?!\s*\()', 'erf', fixed)  # Don't touch if already in Math.erf
    if 'Math.erf' in fixed or re.search(r'\berf\s*\(', fixed):
        erf_polyfill = "var erf=function(x){var sign=x>=0?1:-1;x=Math.abs(x);var a1=0.254829592,a2=-0.284496736,a3=1.421413741,a4=-1.453152027,a5=1.061405429,p=0.3275911;var t=1/(1+p*x);var y=1-(((((a5*t+a4)*t)+a3)*t+a2)*t+a1)*t*Math.exp(-x*x);return sign*y;};"
        if erf_polyfill not in fixed:
            fixed = erf_polyfill + fixed
    
    # Fix 4: 'len' -> '.length'
    if re.search(r'\blen\b', fixed) and 'length' not in fixed:
        fixed = re.sub(r'\blen\b', 'length', fixed)
    
    # Fix 5: 'mmHg' as string literal, escape properly
    if 'mmHg' in fixed and "'mmHg'" not in fixed and '"mmHg"' not in fixed:
        fixed = fixed.replace('mmHg', "'mmHg'")
    
    # Fix 6: 'pi' -> 'Math.PI' (if not inputs.pi)
    if 'pi' not in input_ids and re.search(r'(?<!Math\.)(?<![\w.])pi(?![\w])', fixed):
        fixed = re.sub(r'(?<!Math\.)(?<![\w.])pi(?![\w])', 'Math.PI', fixed)
    
    # Fix 7: 'sqrt' -> 'Math.sqrt' (if not local var)
    if re.search(r'(?<!Math\.)(?<![\w.])sqrt\s*\(', fixed):
        fixed = re.sub(r'(?<!Math\.)(?<![\w.])sqrt\s*\(', 'Math.sqrt(', fixed)
    
    # Fix 8: Fix .toFixed on boolean
    fixed = re.sub(r'\(([^)]+)\s*>\s*([^)]+)\)\.toFixed', r'(Number(\1 > \2)).toFixed', fixed)
    
    return fixed


def main():
    updated = 0
    for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
        name = os.path.basename(fp)
        if "bak" in fp or "monolithic" in fp or name == "calculators.json":
            continue
        
        with open(fp, "r", encoding="utf-8-sig") as f:
            calc = json.load(f)
        
        formula = calc.get("formula", "")
        if not formula:
            continue
        
        new_formula = fix_formula(calc)
        
        if new_formula != formula:
            calc["formula"] = new_formula
            with open(fp, "w", encoding="utf-8", newline="\n") as f:
                json.dump(calc, f, ensure_ascii=False, indent=2)
            updated += 1
            print(f"  Fixed {calc['id']} {name}")
    
    print(f"\nFixed {updated} calculator formulas")


if __name__ == "__main__":
    main()
