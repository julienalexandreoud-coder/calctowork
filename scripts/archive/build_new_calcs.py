#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CALCS_FILE = ROOT / 'src' / 'calculators' / 'calculators.json'
I18N_DIR = ROOT / 'src' / 'i18n'
LANGS = ['es','en','fr','pt','de','it']

with open(CALCS_FILE, 'r', encoding='utf-8') as fp:
    data = json.load(fp)
calcs = data.get('calculators', data)

next_id = max(int(c['id']) for c in calcs) + 1

print(f'Next ID: {next_id}')
print(f'Current count: {len(calcs)}')

def make_calc(cid, slug, block, block_slug, inputs, formula, outputs, related=None):
    return {
        'id': str(cid).zfill(3),
        'slug': slug,
        'block': block,
        'block_slug': block_slug,
        'inputs': inputs,
        'formula': formula,
        'outputs': outputs,
        'related': related or []
    }

def num_input(key, label, minv=0, maxv=99999, step=1, default=0, unit=''):
    return {'id': key, 'type': 'number', 'min': minv, 'max': maxv, 'step': step, 'default': default, 'unit': unit}

def select_input(key, label, options, default=''):
    return {'id': key, 'type': 'select', 'options': options, 'default': default}

def out(key, unit='', highlight=False):
    return {'id': key, 'unit': unit, 'highlight': highlight}

new_calcs = []

# === MATH - BASIC ===
f1 = "var n=parseFloat(inputs.numerador)||0,d=parseFloat(inputs.denominador)||1;if(d==0)return{error:true};var dec=+(n/d).toFixed(4),whole=Math.floor(n/d),rem=n%d;return{decimal:dec,whole_number:whole,remainder:rem,percentage:+(dec*100).toFixed(2)};"
new_calcs.append(make_calc(next_id, 'fraction-calculator', 13, 'matematicas',
    [num_input('numerador','Numerator',1,99999,1,1,''), num_input('denominador','Denominator',1,99999,1,2,'')],
    f1, [out('decimal','',True), out('whole_number',''), out('remainder',''), out('percentage','%')]))
next_id += 1

f2 = "var x1=parseFloat(inputs.x1)||0,y1=parseFloat(inputs.y1)||0,x2=parseFloat(inputs.x2)||0,y2=parseFloat(inputs.y2)||0;if(x1==x2)return{error:true};var m=+(y2-y1)/(x2-x1),b=+(y1-m*x1).toFixed(2),dist=+Math.sqrt((x2-x1)**2+(y2-y1)**2).toFixed(2);return{slope:+(m).toFixed(4),intercept:b,distance:dist,angle:+(Math.atan(m)*180/Math.PI).toFixed(2)};"
new_calcs.append(make_calc(next_id, 'slope-calculator', 13, 'matematicas',
    [num_input('x1','x1',-99999,99999,1,0,''), num_input('y1','y1',-99999,99999,1,0,''), num_input('x2','x2',-99999,99999,1,1,''), num_input('y2','y2',-99999,99999,1,1,'')],
    f2, [out('slope','',True), out('intercept',''), out('distance',''), out('angle','deg')]))
next_id += 1

f3 = "var n=parseFloat(inputs.numero)||0;if(n==0)return{error:true};var exp=Math.floor(Math.log10(Math.abs(n))),mant=+(n/Math.pow(10,exp)).toFixed(4),eng_exp=Math.floor(exp/3)*3,eng_mant=+(n/Math.pow(10,eng_exp)).toFixed(4);return{mantissa:mant,exponent:exp,scientific:mant+'e'+exp,engineering:eng_mant+'e'+eng_exp};"
new_calcs.append(make_calc(next_id, 'scientific-notation', 13, 'matematicas',
    [num_input('numero','Number',-1e308,1e308,0.001,1234.5,'')],
    f3, [out('scientific','',True), out('mantissa',''), out('exponent',''), out('engineering','')]))
next_id += 1

f4 = "var n=parseFloat(inputs.numero)||0,d=parseInt(inputs.decimales)||0;var factor=Math.pow(10,d);return{rounded:+(Math.round(n*factor)/factor).toFixed(d),floor:Math.floor(n),ceiling:Math.ceil(n),nearest_int:Math.round(n)};"
new_calcs.append(make_calc(next_id, 'rounding-calculator', 13, 'matematicas',
    [num_input('numero','Number',-1e308,1e308,0.001,3.14159,''), num_input('decimales','Decimal places',0,10,1,2,'')],
    f4, [out('rounded','',True), out('floor',''), out('ceiling',''), out('nearest_int','')]))
next_id += 1

f5 = "var a=parseInt(inputs.a)||0,b=parseInt(inputs.b)||0;if(!a||!b)return{error:true};function gcd(x,y){while(y){var t=y;y=x%y;x=t;}return x;}var g=gcd(a,b),l=(a*b)/g;return{gcf:g,lcm:l};"
new_calcs.append(make_calc(next_id, 'gcf-lcm-calculator', 13, 'matematicas',
    [num_input('a','First number',1,999999,1,12,''), num_input('b','Second number',1,999999,1,18,'')],
    f5, [out('gcf','',True), out('lcm','')]))
next_id += 1

f6 = "var n=parseInt(inputs.numero)||0;if(n<2)return{error:true};var temp=n,factors=[],d=2;while(d*d<=temp){while(temp%d==0){factors.push(d);temp/=d;}d++;}if(temp>1)factors.push(temp);return{factors:factors.join(' x '),count:factors.length,sum:factors.reduce((a,b)=>a+b,0),is_prime:factors.length==1};"
new_calcs.append(make_calc(next_id, 'prime-factorization', 13, 'matematicas',
    [num_input('numero','Number',2,999999,1,60,'')],
    f6, [out('factors','',True), out('count',''), out('sum',''), out('is_prime','')]))
next_id += 1

# === MATH - GEOMETRY ===
f7 = "var r=parseFloat(inputs.radio)||0;if(r<=0)return{error:true};var a=+(Math.PI*r*r).toFixed(2),c=+(2*Math.PI*r).toFixed(2),d=+(2*r).toFixed(2);return{area:a,circumference:c,diameter:d};"
new_calcs.append(make_calc(next_id, 'circle-calculator', 13, 'matematicas',
    [num_input('radio','Radius',0.001,99999,0.001,5,'')],
    f7, [out('area','',True), out('circumference',''), out('diameter','')]))
next_id += 1

f8 = "var a=parseFloat(inputs.cateto_a)||0,b=parseFloat(inputs.cateto_b)||0,c=parseFloat(inputs.hipotenusa)||0;var count=0;if(a>0)count++;if(b>0)count++;if(c>0)count++;if(count<2)return{error:true};if(!a)a=+Math.sqrt(c*c-b*b).toFixed(2);if(!b)b=+Math.sqrt(c*c-a*a).toFixed(2);if(!c)c=+Math.sqrt(a*a+b*b).toFixed(2);return{cateto_a:a,cateto_b:b,hipotenusa:c,area:+(a*b/2).toFixed(2),perimetro:+(a+b+c).toFixed(2)};"
new_calcs.append(make_calc(next_id, 'right-triangle-calculator', 13, 'matematicas',
    [num_input('cateto_a','Leg A',0,99999,0.001,3,''), num_input('cateto_b','Leg B',0,99999,0.001,4,''), num_input('hipotenusa','Hypotenuse',0,99999,0.001,0,'')],
    f8, [out('hipotenusa','',True), out('cateto_a',''), out('cateto_b',''), out('area',''), out('perimetro','')]))
next_id += 1

f9 = "var a=parseFloat(inputs.base)||0,b=parseFloat(inputs.altura)||0,c=parseFloat(inputs.lado_c)||0;if(!a||!b||!c)return{error:true};var s=(a+b+c)/2;var area=+Math.sqrt(s*(s-a)*(s-b)*(s-c)).toFixed(2);return{area:area,semiperimeter:+s.toFixed(2),perimetro:+(a+b+c).toFixed(2)};"
new_calcs.append(make_calc(next_id, 'heron-triangle-area', 13, 'matematicas',
    [num_input('base','Side A',0.001,99999,0.001,5,''), num_input('altura','Side B',0.001,99999,0.001,6,''), num_input('lado_c','Side C',0.001,99999,0.001,7,'')],
    f9, [out('area','',True), out('semiperimeter',''), out('perimetro','')]))
next_id += 1

f10 = "var b=parseFloat(inputs.base)||0,h=parseFloat(inputs.altura)||0;if(!b||!h)return{error:true};var area=+(b*h).toFixed(2),perim=+(2*(b+h)).toFixed(2),diag=+Math.sqrt(b*b+h*h).toFixed(2);return{area:area,perimeter:perim,diagonal:diag};"
new_calcs.append(make_calc(next_id, 'rectangle-calculator', 13, 'matematicas',
    [num_input('base','Width',0.001,99999,0.001,10,''), num_input('altura','Height',0.001,99999,0.001,5,'')],
    f10, [out('area','',True), out('perimeter',''), out('diagonal','')]))
next_id += 1

f11 = "var a=parseFloat(inputs.lado)||0;if(!a)return{error:true};return{area:+(a*a).toFixed(2),perimeter:+(4*a).toFixed(2),diagonal:+(a*Math.sqrt(2)).toFixed(2)};"
new_calcs.append(make_calc(next_id, 'square-calculator', 13, 'matematicas',
    [num_input('lado','Side',0.001,99999,0.001,5,'')],
    f11, [out('area','',True), out('perimeter',''), out('diagonal','')]))
next_id += 1

f12 = "var b1=parseFloat(inputs.base_mayor)||0,b2=parseFloat(inputs.base_menor)||0,h=parseFloat(inputs.altura)||0;if(!b1||!b2||!h)return{error:true};var area=+((b1+b2)*h/2).toFixed(2),l1=+Math.sqrt(h*h+((b1-b2)/2)**2).toFixed(2),perim=+(b1+b2+2*l1).toFixed(2);return{area:area,perimeter:perim,side:l1};"
new_calcs.append(make_calc(next_id, 'trapezoid-calculator', 13, 'matematicas',
    [num_input('base_mayor','Base 1',0.001,99999,0.001,10,''), num_input('base_menor','Base 2',0.001,99999,0.001,6,''), num_input('altura','Height',0.001,99999,0.001,4,'')],
    f12, [out('area','',True), out('perimeter',''), out('side','')]))
next_id += 1

f13 = "var r=parseFloat(inputs.radio)||0,h=parseFloat(inputs.altura)||0;if(!r||!h)return{error:true};var v=+(Math.PI*r*r*h).toFixed(2),sa=+(2*Math.PI*r*(r+h)).toFixed(2),ba=+(Math.PI*r*r).toFixed(2);return{volume:v,surface_area:sa,base_area:ba};"
new_calcs.append(make_calc(next_id, 'cylinder-volume', 13, 'matematicas',
    [num_input('radio','Radius',0.001,99999,0.001,3,''), num_input('altura','Height',0.001,99999,0.001,10,'')],
    f13, [out('volume','',True), out('surface_area',''), out('base_area','')]))
next_id += 1

f14 = "var r=parseFloat(inputs.radio)||0,h=parseFloat(inputs.altura)||0;if(!r||!h)return{error:true};var v=+(Math.PI*r*r*h/3).toFixed(2),sa=+(Math.PI*r*(r+Math.sqrt(r*r+h*h))).toFixed(2);return{volume:v,surface_area:sa,slant_height:+Math.sqrt(r*r+h*h).toFixed(2)};"
new_calcs.append(make_calc(next_id, 'cone-volume', 13, 'matematicas',
    [num_input('radio','Radius',0.001,99999,0.001,3,''), num_input('altura','Height',0.001,99999,0.001,10,'')],
    f14, [out('volume','',True), out('surface_area',''), out('slant_height','')]))
next_id += 1

f15 = "var a=parseFloat(inputs.base)||0,b=parseFloat(inputs.lado_b)||0,c=parseFloat(inputs.lado_c)||0,h=parseFloat(inputs.altura)||0;if(!a||!b||!c||!h)return{error:true};var v=+(a*h/3).toFixed(2),perim=+(a+b+c).toFixed(2);return{volume:v,base_perimeter:perim,lateral_area:+(perim*h/2).toFixed(2)};"
new_calcs.append(make_calc(next_id, 'pyramid-volume', 13, 'matematicas',
    [num_input('base','Base',0.001,99999,0.001,6,''), num_input('lado_b','Side B',0.001,99999,0.001,5,''), num_input('lado_c','Side C',0.001,99999,0.001,5,''), num_input('altura','Height',0.001,99999,0.001,8,'')],
    f15, [out('volume','',True), out('base_perimeter',''), out('lateral_area','')]))
next_id += 1

f16 = "var r=parseFloat(inputs.radio)||0;if(!r)return{error:true};var v=+(4/3*Math.PI*r*r*r).toFixed(2),sa=+(4*Math.PI*r*r).toFixed(2);return{volume:v,surface_area:sa,diameter:+(2*r).toFixed(2)};"
new_calcs.append(make_calc(next_id, 'sphere-calculator', 13, 'matematicas',
    [num_input('radio','Radius',0.001,99999,0.001,5,'')],
    f16, [out('volume','',True), out('surface_area',''), out('diameter','')]))
next_id += 1

# === HEALTH ===
f17 = "var p=parseFloat(inputs.peso_kg)||0,h=parseFloat(inputs.altura_cm)||0,e=parseFloat(inputs.edad)||30,s=inputs.sexo||'mujer';if(!p||!h||h<50||e<10)return{error:true};var bmr=s=='hombre'?88.362+(13.397*p)+(4.799*h)-(5.677*e):447.593+(9.247*p)+(3.098*h)-(4.330*e);return{bmr_harris:Math.round(bmr),tdee_sedentary:Math.round(bmr*1.2),tdee_light:Math.round(bmr*1.375),tdee_moderate:Math.round(bmr*1.55),tdee_active:Math.round(bmr*1.725),tdee_very_active:Math.round(bmr*1.9)};"
new_calcs.append(make_calc(next_id, 'bmr-harris-benedict', 12, 'salud',
    [num_input('peso_kg','Weight (kg)',10,500,0.1,70,'kg'), num_input('altura_cm','Height (cm)',50,250,0.5,175,'cm'), num_input('edad','Age',2,120,1,30,'years'), select_input('sexo','Gender',['mujer','hombre'],'mujer')],
    f17, [out('bmr_harris','',True), out('tdee_sedentary',''), out('tdee_light',''), out('tdee_moderate',''), out('tdee_active',''), out('tdee_very_active','')]))
next_id += 1

f18 = "var p=parseFloat(inputs.peso_kg)||0,h=parseFloat(inputs.altura_cm)||0,e=parseFloat(inputs.edad)||30,s=inputs.sexo||'mujer',bf=parseFloat(inputs.grasa_pct)||20;if(!p||!h||h<50)return{error:true};var lbm=p*(1-bf/100);var bmr=370+(21.6*lbm);return{bmr_katch:Math.round(bmr),lbm:+(lbm).toFixed(1),tdee:Math.round(bmr*1.2)};"
new_calcs.append(make_calc(next_id, 'bmr-katch-mcardle', 12, 'salud',
    [num_input('peso_kg','Weight (kg)',10,500,0.1,70,'kg'), num_input('altura_cm','Height (cm)',50,250,0.5,175,'cm'), num_input('edad','Age',2,120,1,30,'years'), select_input('sexo','Gender',['mujer','hombre'],'mujer'), num_input('grasa_pct','Body fat %',1,60,0.1,20,'%')],
    f18, [out('bmr_katch','',True), out('lbm','kg'), out('tdee','')]))
next_id += 1

f19 = "var p=parseFloat(inputs.peso_kg)||0,e=parseFloat(inputs.ejercicio_hrs)||0,g=inputs.objetivo||'mantener';if(!p)return{error:true};var base=p*1.2*24;var act=e>0?e*300:0;var total=base+act;var obj={mantener:total,perder:total-500,ganar:total+500};return{calorias_mantenimiento:Math.round(obj[g]),proteinas:Math.round(p*1.6),grasas:Math.round(p*0.9),carbohidratos:Math.round((obj[g]-(p*1.6*4)-(p*0.9*9))/4)};"
new_calcs.append(make_calc(next_id, 'macro-calculator', 12, 'salud',
    [num_input('peso_kg','Weight (kg)',10,500,0.1,70,'kg'), num_input('ejercicio_hrs','Exercise hours/week',0,50,0.5,3,'h'), select_input('objetivo','Goal',['mantener','perder','ganar'],'mantener')],
    f19, [out('calorias_mantenimiento','',True), out('proteinas','g'), out('grasas','g'), out('carbohidratos','g')]))
next_id += 1

f20 = "var sys=parseFloat(inputs.sistolica)||0,dia=parseFloat(inputs.diastolica)||0;if(!sys||!dia||sys<dia)return{error:true};var cat;if(sys<120&&dia<80)cat='Normal';else if(sys<130&&dia<80)cat='Elevated';else if(sys<140||dia<90)cat='Stage 1 Hypertension';else cat='Stage 2 Hypertension';var map=+(dia+(sys-dia)/3).toFixed(1),pp=sys-dia;return{systolic:sys,diastolic:dia,category:cat,map:mmHg,pulse_pressure:pp};"
new_calcs.append(make_calc(next_id, 'blood-pressure', 12, 'salud',
    [num_input('sistolica','Systolic',50,300,1,120,'mmHg'), num_input('diastolica','Diastolic',30,200,1,80,'mmHg')],
    f20, [out('category','',True), out('map','mmHg'), out('pulse_pressure','mmHg')]))
next_id += 1

f21 = "var edad=parseFloat(inputs.edad)||30,sexo=inputs.sexo||'mujer',cintura=parseFloat(inputs.cintura_cm)||0,cadera=parseFloat(inputs.cadera_cm)||0;if(!cintura||!cadera)return{error:true};var whr=+(cintura/cadera).toFixed(2),riesgo=sexo=='mujer'?(whr>0.85?'High':'Normal'):(whr>0.90?'High':'Normal');return{whr:whr,risk:riesgo,ideal:sexo=='mujer'?'<0.85':'<0.90'};"
new_calcs.append(make_calc(next_id, 'waist-hip-ratio', 12, 'salud',
    [num_input('cintura_cm','Waist (cm)',30,200,0.5,80,'cm'), num_input('cadera_cm','Hip (cm)',30,200,0.5,95,'cm'), select_input('sexo','Gender',['mujer','hombre'],'mujer')],
    f21, [out('whr','',True), out('risk',''), out('ideal','')]))
next_id += 1

f22 = "var altura=parseFloat(inputs.altura_cm)||0,cintura=parseFloat(inputs.cintura_cm)||0;if(!altura||!cintura)return{error:true};var whr=+(cintura/altura).toFixed(2),riesgo=whr>0.5?'High':'Normal';return{whr:whr,risk:riesgo,ideal:'<0.5'};"
new_calcs.append(make_calc(next_id, 'waist-height-ratio', 12, 'salud',
    [num_input('altura_cm','Height (cm)',50,250,0.5,175,'cm'), num_input('cintura_cm','Waist (cm)',30,200,0.5,80,'cm')],
    f22, [out('whr','',True), out('risk',''), out('ideal','')]))
next_id += 1

f23 = "var peso_inicial=parseFloat(inputs.peso_inicial)||0,peso_actual=parseFloat(inputs.peso_actual)||0;if(!peso_inicial||!peso_actual)return{error:true};var perdida=peso_inicial-peso_actual,pct=+(perdida/peso_inicial*100).toFixed(1);return{weight_lost:+(perdida).toFixed(1),percentage:pct,remaining:peso_actual};"
new_calcs.append(make_calc(next_id, 'weight-loss-percentage', 12, 'salud',
    [num_input('peso_inicial','Initial weight',10,500,0.1,80,'kg'), num_input('peso_actual','Current weight',10,500,0.1,75,'kg')],
    f23, [out('weight_lost','kg',True), out('percentage','%'), out('remaining','kg')]))
next_id += 1

f24 = "var edad=parseFloat(inputs.edad)||30,fc_reposo=parseFloat(inputs.fc_reposo)||60;if(!edad||!fc_reposo)return{error:true};var fc_max=220-edad;var z1_min=Math.round(fc_reposo+(fc_max-fc_reposo)*0.5),z1_max=Math.round(fc_reposo+(fc_max-fc_reposo)*0.6);var z2_min=Math.round(fc_reposo+(fc_max-fc_reposo)*0.6),z2_max=Math.round(fc_reposo+(fc_max-fc_reposo)*0.7);var z3_min=Math.round(fc_reposo+(fc_max-fc_reposo)*0.7),z3_max=Math.round(fc_reposo+(fc_max-fc_reposo)*0.8);var z4_min=Math.round(fc_reposo+(fc_max-fc_reposo)*0.8),z4_max=Math.round(fc_reposo+(fc_max-fc_reposo)*0.9);var z5_min=Math.round(fc_reposo+(fc_max-fc_reposo)*0.9),z5_max=fc_max;return{fc_max:fc_max,z1_recovery:z1_min+'-'+z1_max,z2_fat_burn:z2_min+'-'+z2_max,z3_aerobic:z3_min+'-'+z3_max,z4_threshold:z4_min+'-'+z4_max,z5_maximum:z5_min+'-'+z5_max};"
new_calcs.append(make_calc(next_id, 'heart-rate-zones', 12, 'salud',
    [num_input('edad','Age',10,100,1,30,'years'), num_input('fc_reposo','Resting HR',30,120,1,60,'bpm')],
    f24, [out('fc_max','bpm',True), out('z1_recovery',''), out('z2_fat_burn',''), out('z3_aerobic',''), out('z4_threshold',''), out('z5_maximum','')]))
next_id += 1

# === FINANCE ===
f25 = "var salario=parseFloat(inputs.salario_anual)||0,horas=parseFloat(inputs.horas_semana)||40,semanas=parseFloat(inputs.semanas_ano)||52;if(!salario)return{error:true};var hora=+(salario/(horas*semanas)).toFixed(2),mes=+(salario/12).toFixed(2),semana=+(salario/semanas).toFixed(2),dia=+(salario/(horas*semanas/5)).toFixed(2);return{hourly:hora,monthly:mes,weekly:semana,daily:dia};"
new_calcs.append(make_calc(next_id, 'salary-to-hourly', 11, 'finanzas',
    [num_input('salario_anual','Annual salary',0,9999999,100,50000,'EUR'), num_input('horas_semana','Hours/week',1,80,1,40,'h'), num_input('semanas_ano','Weeks/year',1,52,1,52,'wk')],
    f25, [out('hourly','EUR',True), out('monthly','EUR'), out('weekly','EUR'), out('daily','EUR')]))
next_id += 1

f26 = "var hora=parseFloat(inputs.salario_hora)||0,horas=parseFloat(inputs.horas_semana)||40,semanas=parseFloat(inputs.semanas_ano)||52;if(!hora)return{error:true};var anual=+(hora*horas*semanas).toFixed(2),mes=+(anual/12).toFixed(2),semana=+(hora*horas).toFixed(2),dia=+(hora*(horas/5)).toFixed(2);return{annual:anual,monthly:mes,weekly:semana,daily:dia};"
new_calcs.append(make_calc(next_id, 'hourly-to-salary', 11, 'finanzas',
    [num_input('salario_hora','Hourly rate',0,1000,0.01,25,'EUR'), num_input('horas_semana','Hours/week',1,80,1,40,'h'), num_input('semanas_ano','Weeks/year',1,52,1,52,'wk')],
    f26, [out('annual','EUR',True), out('monthly','EUR'), out('weekly','EUR'), out('daily','EUR')]))
next_id += 1

f27 = "var precio=parseFloat(inputs.precio_casa)||0,entrada=parseFloat(inputs.entrada_pct)||20,tasa=parseFloat(inputs.tasa_anual)||0,anos=parseFloat(inputs.anos)||30;if(!precio||!tasa||!anos)return{error:true};var prestamo=precio*(1-entrada/100),r=tasa/1200,n=anos*12,pmt=prestamo*r/(1-Math.pow(1+r,-n));var total=+(pmt*n).toFixed(2),interes=+(total-prestamo).toFixed(2);return{monthly_payment:+(pmt).toFixed(2),loan_amount:+(prestamo).toFixed(2),total_paid:total,total_interest:interes,interest_ratio:+(interes/total*100).toFixed(1)};"
new_calcs.append(make_calc(next_id, 'mortgage-calculator', 11, 'finanzas',
    [num_input('precio_casa','Home price',0,9999999,1000,300000,'EUR'), num_input('entrada_pct','Down payment %',0,100,1,20,'%'), num_input('tasa_anual','Interest rate',0,20,0.01,3.5,'%'), num_input('anos','Years',1,50,1,30,'yr')],
    f27, [out('monthly_payment','EUR',True), out('loan_amount','EUR'), out('total_paid','EUR'), out('total_interest','EUR'), out('interest_ratio','%')]))
next_id += 1

f28 = "var deuda=parseFloat(inputs.deuda_total)||0,tasa=parseFloat(inputs.tasa_anual)||0,pago=parseFloat(inputs.pago_mensual)||0;if(!deuda||!tasa||!pago)return{error:true};var r=tasa/1200,balance=deuda,meses=0,total_interes=0;while(balance>0&&meses<600){var interes_mes=balance*r;total_interes+=interes_mes;var principal=pago-interes_mes;if(principal<=0)return{error:true};balance-=principal;meses++;}return{months_to_payoff:meses,total_interest:+(total_interes).toFixed(2),total_paid:+(deuda+total_interes).toFixed(2)};"
new_calcs.append(make_calc(next_id, 'debt-payoff', 11, 'finanzas',
    [num_input('deuda_total','Total debt',0,999999,100,10000,'EUR'), num_input('tasa_anual','Interest rate',0,30,0.01,18,'%'), num_input('pago_mensual','Monthly payment',0,99999,10,300,'EUR')],
    f28, [out('months_to_payoff','',True), out('total_interest','EUR'), out('total_paid','EUR')]))
next_id += 1

f29 = "var ahorro=parseFloat(inputs.ahorro_mensual)||0,tasa=parseFloat(inputs.tasa_anual)||0,anos=parseFloat(inputs.anos)||20;if(!ahorro)return{error:true};var r=tasa/1200,n=anos*12;var total=ahorro*(Math.pow(1+r,n)-1)/r;var aportado=ahorro*n;var interes=total-aportado;return{final_amount:+(total).toFixed(2),total_contributed:+(aportado).toFixed(2),total_interest:+(interes).toFixed(2)};"
new_calcs.append(make_calc(next_id, 'savings-calculator', 11, 'finanzas',
    [num_input('ahorro_mensual','Monthly savings',0,99999,10,500,'EUR'), num_input('tasa_anual','Interest rate',0,20,0.01,7,'%'), num_input('anos','Years',1,50,1,20,'yr')],
    f29, [out('final_amount','EUR',True), out('total_contributed','EUR'), out('total_interest','EUR')]))
next_id += 1

f30 = "var costo=parseFloat(inputs.costo)||0,precio=parseFloat(inputs.precio_venta)||0;if(!costo||!precio)return{error:true};var margen=+((precio-costo)/precio*100).toFixed(2),markup=+((precio-costo)/costo*100).toFixed(2),ganancia=precio-costo;return{margin_pct:margen,markup_pct:markup,profit:ganancia};"
new_calcs.append(make_calc(next_id, 'profit-margin', 11, 'finanzas',
    [num_input('costo','Cost',0,999999,0.01,50,'EUR'), num_input('precio_venta','Selling price',0,999999,0.01,100,'EUR')],
    f30, [out('margin_pct','%',True), out('markup_pct','%'), out('profit','EUR')]))
next_id += 1

f31 = "var inversion=parseFloat(inputs.inversion)||0,flujos=parseFloat(inputs.flujo_anual)||0,anos=parseFloat(inputs.anos)||0;if(!inversion||!flujos||!anos)return{error:true};var vpn=-inversion;for(var i=1;i<=anos;i++){vpn+=flujos/Math.pow(1.08,i);}var tir_approx=+(flujos/inversion).toFixed(4);var payback=Math.ceil(inversion/flujos);return{npv:+(vpn).toFixed(2),roi_annual:+(tir_approx*100).toFixed(2),payback_years:payback};"
new_calcs.append(make_calc(next_id, 'npv-calculator', 11, 'finanzas',
    [num_input('inversion','Initial investment',0,9999999,100,10000,'EUR'), num_input('flujo_anual','Annual cash flow',0,999999,100,2500,'EUR'), num_input('anos','Years',1,50,1,5,'yr')],
    f31, [out('npv','EUR',True), out('roi_annual','%'), out('payback_years','yr')]))
next_id += 1

f32 = "var gastos=parseFloat(inputs.gastos_mensuales)||0,ahorro=parseFloat(inputs.ahorro_meses)||6;if(!gastos)return{error:true};var total=gastos*ahorro;return{emergency_fund:+(total).toFixed(2),monthly:gastos,months:ahorro};"
new_calcs.append(make_calc(next_id, 'emergency-fund', 11, 'finanzas',
    [num_input('gastos_mensuales','Monthly expenses',0,99999,10,2000,'EUR'), num_input('ahorro_meses','Months to cover',1,24,1,6,'mo')],
    f32, [out('emergency_fund','EUR',True), out('monthly','EUR'), out('months','mo')]))
next_id += 1

# === EVERYDAY LIFE ===
f33 = "var y=parseInt(inputs.anio)||2000,m=parseInt(inputs.mes)||1,d=parseInt(inputs.dia)||1;var birth=new Date(y,m-1,d);var now=new Date();var diff=now-birth;var dias=Math.floor(diff/86400000);var anos=Math.floor(dias/365.25);var meses=Math.floor((dias%365.25)/30.44);var dias_r=Math.floor(dias%30.44);var horas=Math.floor(diff/3600000);return{age_years:anos,age_months:Math.floor(dias/30.44),age_days:dias,age_hours:horas,days_until_birthday:(365-Math.floor(dias%365.25))};"
new_calcs.append(make_calc(next_id, 'age-calculator-advanced', 14, 'cotidiano',
    [num_input('anio','Year',1900,2026,1,1995,''), num_input('mes','Month',1,12,1,6,''), num_input('dia','Day',1,31,1,15,'')],
    f33, [out('age_years','',True), out('age_months',''), out('age_days',''), out('age_hours',''), out('days_until_birthday','')]))
next_id += 1

f34 = "var y1=parseInt(inputs.anio1)||2020,m1=parseInt(inputs.mes1)||1,d1=parseInt(inputs.dia1)||1,y2=parseInt(inputs.anio2)||2025,m2=parseInt(inputs.mes2)||1,d2=parseInt(inputs.dia2)||1;var date1=new Date(y1,m1-1,d1),date2=new Date(y2,m2-1,d2);var diff=Math.abs(date2-date1);var dias=Math.floor(diff/86400000);var semanas=Math.floor(dias/7);var meses=Math.floor(dias/30.44);var anos=Math.floor(dias/365.25);return{total_days:dias,total_weeks:semanas,total_months:meses,total_years:anos};"
new_calcs.append(make_calc(next_id, 'date-difference', 14, 'cotidiano',
    [num_input('anio1','Year 1',1900,2030,1,2020,''), num_input('mes1','Month 1',1,12,1,1,''), num_input('dia1','Day 1',1,31,1,1,''), num_input('anio2','Year 2',1900,2030,1,2025,''), num_input('mes2','Month 2',1,12,1,1,''), num_input('dia2','Day 2',1,31,1,1,'')],
    f34, [out('total_days','',True), out('total_weeks',''), out('total_months',''), out('total_years','')]))
next_id += 1

f35 = "var total=parseFloat(inputs.cuenta)||0,pct=parseFloat(inputs.porcentaje)||15,personas=parseInt(inputs.personas)||1;if(!total||personas<1)return{error:true};var propina=+(total*pct/100).toFixed(2),total_f=+(total+propina).toFixed(2),pp=+(total_f/personas).toFixed(2),prop_pp=+(propina/personas).toFixed(2);return{tip:propina,total:total_f,per_person:pp,tip_per_person:prop_pp};"
new_calcs.append(make_calc(next_id, 'tip-calculator-advanced', 14, 'cotidiano',
    [num_input('cuenta','Bill total',0,99999,0.01,100,'EUR'), num_input('porcentaje','Tip %',0,100,0.1,15,'%'), num_input('personas','People',1,100,1,2,'')],
    f35, [out('tip','EUR',True), out('total','EUR'), out('per_person','EUR'), out('tip_per_person','EUR')]))
next_id += 1

f36 = "var original=parseFloat(inputs.precio_original)||0,d1=parseFloat(inputs.descuento1)||0,d2=parseFloat(inputs.descuento2)||0;if(!original)return{error:true};var p1=original*(1-d1/100);var final=p1*(1-d2/100);var ahorro=original-final;return{final_price:+(final).toFixed(2),total_savings:+(ahorro).toFixed(2),savings_pct:+(ahorro/original*100).toFixed(1)};"
new_calcs.append(make_calc(next_id, 'double-discount', 14, 'cotidiano',
    [num_input('precio_original','Original price',0,99999,0.01,100,'EUR'), num_input('descuento1','Discount 1 %',0,100,0.1,20,'%'), num_input('descuento2','Discount 2 %',0,100,0.1,10,'%')],
    f36, [out('final_price','EUR',True), out('total_savings','EUR'), out('savings_pct','%')]))
next_id += 1

# === PHYSICS ===
f37 = "var m=parseFloat(inputs.masa)||0,v=parseFloat(inputs.velocidad)||0;if(!m||!v)return{error:true};var ke=+(0.5*m*v*v).toFixed(2);return{kinetic_energy:ke,joules:ke,calories:+(ke/4184).toFixed(4)};"
new_calcs.append(make_calc(next_id, 'kinetic-energy', 15, 'ciencia',
    [num_input('masa','Mass',0.001,999999,0.001,10,'kg'), num_input('velocidad','Velocity',0,999999,0.1,5,'m/s')],
    f37, [out('kinetic_energy','J',True), out('joules','J'), out('calories','cal')]))
next_id += 1

f38 = "var m=parseFloat(inputs.masa)||0,h=parseFloat(inputs.altura)||0,g=parseFloat(inputs.gravedad)||9.81;if(!m||!h)return{error:true};var pe=+(m*g*h).toFixed(2);return{potential_energy:pe,joules:pe,calories:+(pe/4184).toFixed(4)};"
new_calcs.append(make_calc(next_id, 'potential-energy', 15, 'ciencia',
    [num_input('masa','Mass',0.001,999999,0.001,10,'kg'), num_input('altura','Height',0,999999,0.1,10,'m'), num_input('gravedad','Gravity',0.1,100,0.01,9.81,'m/s2')],
    f38, [out('potential_energy','J',True), out('joules','J'), out('calories','cal')]))
next_id += 1

f39 = "var f=parseFloat(inputs.fuerza)||0,d=parseFloat(inputs.distancia)||0,t=parseFloat(inputs.tiempo)||1;if(!f||!d)return{error:true};var w=+(f*d).toFixed(2),p=+(w/t).toFixed(2);return{work:w,power:p,joules:w,watts:p};"
new_calcs.append(make_calc(next_id, 'work-power', 15, 'ciencia',
    [num_input('fuerza','Force',0,999999,0.1,100,'N'), num_input('distancia','Distance',0,999999,0.1,10,'m'), num_input('tiempo','Time',0.001,999999,0.1,5,'s')],
    f39, [out('work','J',True), out('power','W'), out('joules','J'), out('watts','W')]))
next_id += 1

f40 = "var v=parseFloat(inputs.voltaje)||0,i=parseFloat(inputs.corriente)||0,r=parseFloat(inputs.resistencia)||0,p=parseFloat(inputs.potencia)||0;var count=0;if(v>0)count++;if(i>0)count++;if(r>0)count++;if(p>0)count++;if(count<2)return{error:true};if(v&&i){r=+(v/i).toFixed(2);p=+(v*i).toFixed(2);}else if(v&&r){i=+(v/r).toFixed(2);p=+(v*v/r).toFixed(2);}else if(i&&r){v=+(i*r).toFixed(2);p=+(i*i*r).toFixed(2);}else if(v&&p){i=+(p/v).toFixed(2);r=+(v*v/p).toFixed(2);}else if(i&&p){v=+(p/i).toFixed(2);r=+(p/(i*i)).toFixed(2);}else if(r&&p){v=+(Math.sqrt(p*r)).toFixed(2);i=+(Math.sqrt(p/r)).toFixed(2);}return{voltage:v,current:i,resistance:r,power:p};"
new_calcs.append(make_calc(next_id, 'ohms-law-power', 15, 'ciencia',
    [num_input('voltaje','Voltage',0,999999,0.1,0,'V'), num_input('corriente','Current',0,999999,0.01,0,'A'), num_input('resistencia','Resistance',0,999999,0.1,0,'Ohm'), num_input('potencia','Power',0,999999,0.1,0,'W')],
    f40, [out('voltage','V',True), out('current','A'), out('resistance','Ohm'), out('power','W')]))
next_id += 1

f41 = "var m=parseFloat(inputs.masa)||0,a=parseFloat(inputs.aceleracion)||0,t=parseFloat(inputs.tiempo)||1;if(!m)return{error:true};var f=+(m*a).toFixed(2),v=+(a*t).toFixed(2),d=+(0.5*a*t*t).toFixed(2);return{force:f,final_velocity:v,distance:d};"
new_calcs.append(make_calc(next_id, 'newtons-second-law', 15, 'ciencia',
    [num_input('masa','Mass',0.001,999999,0.001,10,'kg'), num_input('aceleracion','Acceleration',-999,999,0.01,2,'m/s2'), num_input('tiempo','Time',0.001,999,0.1,5,'s')],
    f41, [out('force','N',True), out('final_velocity','m/s'), out('distance','m')]))
next_id += 1

# === SPORTS ===
f42 = "var peso=parseFloat(inputs.peso_kg)||0,reps=parseInt(inputs.repeticiones)||0;if(!peso||!reps||reps<1||reps>20)return{error:true};var orm=+(peso*(1+reps/30)).toFixed(1);return{one_rep_max:orm,at_90pct:+(orm*0.9).toFixed(1),at_80pct:+(orm*0.8).toFixed(1),at_70pct:+(orm*0.7).toFixed(1)};"
new_calcs.append(make_calc(next_id, 'one-rep-max', 16, 'deportes',
    [num_input('peso_kg','Weight lifted',0.1,500,0.1,80,'kg'), num_input('repeticiones','Reps',1,20,1,5,'')],
    f42, [out('one_rep_max','kg',True), out('at_90pct','kg'), out('at_80pct','kg'), out('at_70pct','kg')]))
next_id += 1

f43 = "var distancia=parseFloat(inputs.distancia_km)||0,tiempo=parseFloat(inputs.tiempo_min)||0;if(!distancia||!tiempo)return{error:true};var pace=+(tiempo/distancia).toFixed(1),speed=+(distancia/(tiempo/60)).toFixed(2);var t5k=Math.round(pace*5),t10k=Math.round(pace*10),thm=Math.round(pace*21.0975),tm=Math.round(pace*42.195);return{pace_min_km:pace,speed_kmh:speed,time_5k:t5k+' min',time_10k:t10k+' min',time_half_marathon:Math.floor(thm/60)+'h'+(thm%60)+'m',time_marathon:Math.floor(tm/60)+'h'+(tm%60)+'m'};"
new_calcs.append(make_calc(next_id, 'running-pace-predictor', 16, 'deportes',
    [num_input('distancia_km','Distance run',0.1,100,0.1,5,'km'), num_input('tiempo_min','Time (min)',1,600,0.1,25,'min')],
    f43, [out('pace_min_km','min/km',True), out('speed_kmh','km/h'), out('time_5k',''), out('time_10k',''), out('time_half_marathon',''), out('time_marathon','')]))
next_id += 1

f44 = "var edad=parseFloat(inputs.edad)||30,peso=parseFloat(inputs.peso_kg)||70,fc_reposo=parseFloat(inputs.fc_reposo)||60,duracion=parseFloat(inputs.duracion_min)||30;if(!edad||!peso)return{error:true};var fc_max=220-edad;var vo2=+(15.3*(fc_max/fc_reposo)).toFixed(1);var cal=+(0.0175*vo2*peso*duracion).toFixed(0);return{vo2_max:vo2,calories_burned:cal,fitness_level:vo2>50?'Excellent':vo2>40?'Good':vo2>30?'Average':'Below average'};"
new_calcs.append(make_calc(next_id, 'vo2-max-estimator', 16, 'deportes',
    [num_input('edad','Age',10,100,1,30,'years'), num_input('peso_kg','Weight',10,200,0.1,70,'kg'), num_input('fc_reposo','Resting HR',30,120,1,60,'bpm'), num_input('duracion_min','Duration',1,300,1,30,'min')],
    f44, [out('vo2_max','ml/kg/min',True), out('calories_burned','cal'), out('fitness_level','')]))
next_id += 1

# === CONVERSIONS ===
f45 = "var deg=parseFloat(inputs.grados)||0;var rad=+(deg*Math.PI/180).toFixed(4),grad=+(deg*10/9).toFixed(2);return{radians:rad,gradians:grad};"
new_calcs.append(make_calc(next_id, 'angle-converter', 17, 'conversion',
    [num_input('grados','Degrees',0,360,0.1,45,'deg')],
    f45, [out('radians','rad',True), out('gradians','gon')]))
next_id += 1

f46 = "var c=parseFloat(inputs.celsius)||0;var f=+(c*9/5+32).toFixed(2),k=+(c+273.15).toFixed(2),r=+(c*9/5+491.67).toFixed(2);return{fahrenheit:f,kelvin:k,rankine:r};"
new_calcs.append(make_calc(next_id, 'temperature-full', 17, 'conversion',
    [num_input('celsius','Celsius',-273.15,1000,0.1,25,'C')],
    f46, [out('fahrenheit','F',True), out('kelvin','K'), out('rankine','R')]))
next_id += 1

f47 = "var j=parseFloat(inputs.joules)||0;var cal=+(j/4.184).toFixed(4),kcal=+(j/4184).toFixed(6),wh=+(j/3600).toFixed(6),kwh=+(j/3600000).toFixed(9);return{calories:cal,kilocalories:kcal,watt_hours:wh,kilowatt_hours:kwh};"
new_calcs.append(make_calc(next_id, 'energy-converter', 17, 'conversion',
    [num_input('joules','Joules',0,1e15,0.001,100,'J')],
    f47, [out('calories','cal',True), out('kilocalories','kcal'), out('watt_hours','Wh'), out('kilowatt_hours','kWh')]))
next_id += 1

# === STATISTICS ===
f48 = "var n=parseInt(inputs.n)||0,r=parseInt(inputs.r)||0;if(r>n||n<0||r<0)return{error:true};function fact(x){var f=1;for(var i=2;i<=x;i++)f*=i;return f;}var comb=+(fact(n)/(fact(r)*fact(n-r))).toFixed(0),perm=+(fact(n)/fact(n-r)).toFixed(0);return{combinations:comb,permutations:perm};"
new_calcs.append(make_calc(next_id, 'combinations-permutations', 18, 'estadistica',
    [num_input('n','Total items',0,170,1,10,''), num_input('r','Items chosen',0,170,1,3,'')],
    f48, [out('combinations','',True), out('permutations','')]))
next_id += 1

f49 = "var x=parseFloat(inputs.valor)||0,m=parseFloat(inputs.media)||0,s=parseFloat(inputs.desviacion)||1;if(!s)return{error:true};var z=+((x-m)/s).toFixed(4);var percentile=+(0.5*(1+Math.erf(z/Math.sqrt(2)))*100).toFixed(2);return{z_score:z,percentile:percentile,classification:z>2?'Far above average':z>1?'Above average':z>-1?'Average':z>-2?'Below average':'Far below average'};"
new_calcs.append(make_calc(next_id, 'z-score-percentile', 18, 'estadistica',
    [num_input('valor','Value',-99999,99999,0.01,85,''), num_input('media','Mean',-99999,99999,0.01,75,''), num_input('desviacion','Std dev',0.001,99999,0.001,10,'')],
    f49, [out('z_score','',True), out('percentile','%'), out('classification','')]))
next_id += 1

f50 = "var n=parseInt(inputs.tamano_muestra)||0,p=parseFloat(inputs.proporcion)||0.5,e=parseFloat(inputs.margen_error)||0.05,conf=parseFloat(inputs.confianza)||0.95;if(!n)return{error:true};var z={0.9:1.645,0.95:1.96,0.99:2.576};var zv=z[conf]||1.96;var se=+Math.sqrt(p*(1-p)/n).toFixed(4);var me=+(zv*se).toFixed(4);var lower=+(p-me).toFixed(4),upper=+(p+me).toFixed(4);return{sample_size:n,standard_error:se,margin_of_error:me,ci_lower:lower,ci_upper:upper};"
new_calcs.append(make_calc(next_id, 'sample-size-confidence', 18, 'estadistica',
    [num_input('tamano_muestra','Sample size',1,999999,1,100,''), num_input('proporcion','Proportion',0,1,0.01,0.5,''), num_input('margen_error','Margin of error',0.001,0.5,0.001,0.05,''), num_input('confianza','Confidence level',0.8,0.99,0.01,0.95,'')],
    f50, [out('standard_error','',True), out('margin_of_error',''), out('ci_lower',''), out('ci_upper','')]))
next_id += 1

# === MORE HEALTH ===
f51 = "var edad=parseFloat(inputs.edad)||30,peso=parseFloat(inputs.peso_kg)||0,altura=parseFloat(inputs.altura_cm)||0,sexo=inputs.sexo||'mujer';if(!peso||!altura||altura<50)return{error:true};var bsa=+Math.sqrt((peso*altura)/3600).toFixed(2);var ibw=sexo=='hombre'?50+0.91*(altura-152.4):45.5+0.91*(altura-152.4);var abw=+(ibw+0.4*(peso-ibw)).toFixed(1);return{bsa:bsa+' m2',ideal_weight:+(ibw).toFixed(1),adjusted_weight:abw};"
new_calcs.append(make_calc(next_id, 'bsa-ideal-weight', 12, 'salud',
    [num_input('edad','Age',2,120,1,30,'years'), num_input('peso_kg','Weight',10,500,0.1,70,'kg'), num_input('altura_cm','Height',50,250,0.5,175,'cm'), select_input('sexo','Gender',['mujer','hombre'],'mujer')],
    f51, [out('bsa','m2',True), out('ideal_weight','kg'), out('adjusted_weight','kg')]))
next_id += 1

f52 = "var glucosa=parseFloat(inputs.glucosa_mgdl)||0;if(!glucosa)return{error:true};var a1c=+((glucosa+46.7)/28.7).toFixed(1);return{a1c_estimated:a1c+'%',glucose:glucosa+' mg/dL',category:glucosa<100?'Normal':glucosa<126?'Prediabetic':'Diabetic'};"
new_calcs.append(make_calc(next_id, 'a1c-estimator', 12, 'salud',
    [num_input('glucosa_mgdl','Glucose (mg/dL)',30,600,1,100,'mg/dL')],
    f52, [out('a1c_estimated','%',True), out('glucose','mg/dL'), out('category','')]))
next_id += 1

f53 = "var total=parseFloat(inputs.colesterol_total)||0,hdl=parseFloat(inputs.hdl)||0,trig=parseFloat(inputs.trigliceridos)||0;if(!total||!hdl)return{error:true};var ldl=+(total-hdl-trig/5).toFixed(1);var ratio=+(total/hdl).toFixed(1);return{ldl:ldl+' mg/dL',total_hdl_ratio:ratio,risk:ratio<3.5?'Low':ratio<5?'Moderate':'High'};"
new_calcs.append(make_calc(next_id, 'cholesterol-ldl', 12, 'salud',
    [num_input('colesterol_total','Total cholesterol',50,500,1,200,'mg/dL'), num_input('hdl','HDL',10,150,1,50,'mg/dL'), num_input('trigliceridos','Triglycerides',20,1000,1,150,'mg/dL')],
    f53, [out('ldl','mg/dL',True), out('total_hdl_ratio',''), out('risk','')]))
next_id += 1

print(f'Total new calculators: {len(new_calcs)}')
print(f'Next ID will be: {next_id}')

# === WRITE CALCULATORS ===
calcs.extend(new_calcs)
with open(CALCS_FILE, 'w', encoding='utf-8') as fp:
    json.dump({'calculators': calcs}, fp, ensure_ascii=False, indent=2)
print(f'Wrote {len(calcs)} calculators to {CALCS_FILE}')

# === GENERATE I18N ===
# Basic i18n templates for new outputs
I18N_TEMPLATES = {
    'es': {
        'decimal': 'Decimal', 'whole_number': 'Entero', 'remainder': 'Resto', 'percentage': 'Porcentaje',
        'slope': 'Pendiente', 'intercept': 'Ordenada', 'distance': 'Distancia', 'angle': 'Angulo',
        'mantissa': 'Mantisa', 'exponent': 'Exponente', 'scientific': 'Cientifica', 'engineering': 'Ingenieria',
        'rounded': 'Redondeado', 'floor': 'Piso', 'ceiling': 'Techo', 'nearest_int': 'Entero cercano',
        'gcf': 'MCD', 'lcm': 'mcm',
        'factors': 'Factores', 'count': 'Cantidad', 'sum': 'Suma', 'is_prime': 'Es primo',
        'ratio': 'Razon', 'simplified': 'Simplificado', 'decimal_val': 'Decimal', 'x': 'X',
        'mean': 'Media', 'count_val': 'Cantidad', 'sum_val': 'Suma', 'min': 'Min', 'max': 'Max', 'range': 'Rango',
        'area': 'Area', 'circumference': 'Circunferencia', 'diameter': 'Diametro',
        'hipotenusa': 'Hipotenusa', 'cateto_a': 'Cateto A', 'cateto_b': 'Cateto B', 'perimetro': 'Perimetro',
        'semiperimeter': 'Semiperimetro', 'side': 'Lado', 'base_perimeter': 'Perimetro base', 'lateral_area': 'Area lateral',
        'volume': 'Volumen', 'surface_area': 'Area superficie', 'base_area': 'Area base', 'slant_height': 'Altura inclinada',
        'bmr_harris': 'TMB Harris-Benedict', 'tdee_sedentary': 'TDEE Sedentario', 'tdee_light': 'TDEE Ligero',
        'tdee_moderate': 'TDEE Moderado', 'tdee_active': 'TDEE Activo', 'tdee_very_active': 'TDEE Muy activo',
        'bmr_katch': 'TMB Katch-McArdle', 'lbm': 'Masa magra', 'tdee': 'TDEE',
        'calorias_mantenimiento': 'Calorias mantenimiento', 'proteinas': 'Proteinas', 'grasas': 'Grasas', 'carbohidratos': 'Carbohidratos',
        'category': 'Categoria', 'map': 'Presion media', 'pulse_pressure': 'Presion pulso',
        'whr': 'Indice cintura-cadera', 'risk': 'Riesgo', 'ideal': 'Ideal',
        'weight_lost': 'Peso perdido', 'remaining': 'Restante',
        'fc_max': 'FC max', 'z1_recovery': 'Z1 Recuperacion', 'z2_fat_burn': 'Z2 Quema grasa',
        'z3_aerobic': 'Z3 Aerobica', 'z4_threshold': 'Z4 Umbral', 'z5_maximum': 'Z5 Maxima',
        'hourly': 'Por hora', 'monthly': 'Mensual', 'weekly': 'Semanal', 'daily': 'Diario',
        'annual': 'Anual', 'monthly_val': 'Mensual', 'weekly_val': 'Semanal', 'daily_val': 'Diario',
        'monthly_payment': 'Cuota mensual', 'loan_amount': 'Capital prestado', 'total_paid': 'Total pagado',
        'total_interest': 'Total intereses', 'interest_ratio': 'Ratio interes',
        'months_to_payoff': 'Meses para pagar', 'final_amount': 'Monto final',
        'total_contributed': 'Total aportado', 'margin_pct': 'Margen %', 'markup_pct': 'Markup %', 'profit': 'Ganancia',
        'npv': 'VAN', 'roi_annual': 'ROI anual', 'payback_years': 'Anos recuperacion',
        'emergency_fund': 'Fondo emergencia', 'monthly_val2': 'Mensual',
        'age_years': 'Anos', 'age_months': 'Meses', 'age_days': 'Dias', 'age_hours': 'Horas', 'days_until_birthday': 'Dias hasta cumple',
        'total_days': 'Dias totales', 'total_weeks': 'Semanas', 'total_months': 'Meses', 'total_years': 'Anos',
        'tip': 'Propina', 'per_person': 'Por persona', 'tip_per_person': 'Propina/persona',
        'final_price': 'Precio final', 'total_savings': 'Ahorro total', 'savings_pct': 'Ahorro %',
        'kinetic_energy': 'Energia cinetica', 'joules': 'Julios', 'calories': 'Calorias',
        'potential_energy': 'Energia potencial', 'work': 'Trabajo', 'power': 'Potencia', 'watts': 'Watts',
        'voltage': 'Voltaje', 'current': 'Corriente', 'resistance': 'Resistencia',
        'force': 'Fuerza', 'final_velocity': 'Velocidad final', 'distance': 'Distancia',
        'one_rep_max': '1RM', 'at_90pct': '90%', 'at_80pct': '80%', 'at_70pct': '70%',
        'pace_min_km': 'Ritmo min/km', 'speed_kmh': 'Velocidad km/h', 'time_5k': 'Tiempo 5K',
        'time_10k': 'Tiempo 10K', 'time_half_marathon': 'Media maraton', 'time_marathon': 'Maraton',
        'vo2_max': 'VO2 max', 'calories_burned': 'Calorias quemadas', 'fitness_level': 'Nivel fitness',
        'radians': 'Radianes', 'gradians': 'Gradianes',
        'fahrenheit': 'Fahrenheit', 'kelvin': 'Kelvin', 'rankine': 'Rankine',
        'kilocalories': 'Kilocalorias', 'watt_hours': 'Wh', 'kilowatt_hours': 'kWh',
        'combinations': 'Combinaciones', 'permutations': 'Permutaciones',
        'z_score': 'Z-score', 'percentile': 'Percentil', 'classification': 'Clasificacion',
        'sample_size': 'Tamano muestra', 'standard_error': 'Error estandar', 'margin_of_error': 'Margen error',
        'ci_lower': 'IC inferior', 'ci_upper': 'IC superior',
        'bsa': 'ASC', 'ideal_weight': 'Peso ideal', 'adjusted_weight': 'Peso ajustado',
        'a1c_estimated': 'A1c estimado', 'glucose': 'Glucosa',
        'ldl': 'LDL', 'total_hdl_ratio': 'Ratio Total/HDL',
    },
    'en': {
        'decimal': 'Decimal', 'whole_number': 'Whole number', 'remainder': 'Remainder', 'percentage': 'Percentage',
        'slope': 'Slope', 'intercept': 'Intercept', 'distance': 'Distance', 'angle': 'Angle',
        'mantissa': 'Mantissa', 'exponent': 'Exponent', 'scientific': 'Scientific', 'engineering': 'Engineering',
        'rounded': 'Rounded', 'floor': 'Floor', 'ceiling': 'Ceiling', 'nearest_int': 'Nearest integer',
        'gcf': 'GCF', 'lcm': 'LCM',
        'factors': 'Factors', 'count': 'Count', 'sum': 'Sum', 'is_prime': 'Is prime',
        'ratio': 'Ratio', 'simplified': 'Simplified', 'decimal_val': 'Decimal', 'x': 'X',
        'mean': 'Mean', 'count_val': 'Count', 'sum_val': 'Sum', 'min': 'Min', 'max': 'Max', 'range': 'Range',
        'area': 'Area', 'circumference': 'Circumference', 'diameter': 'Diameter',
        'hipotenusa': 'Hypotenuse', 'cateto_a': 'Leg A', 'cateto_b': 'Leg B', 'perimetro': 'Perimeter',
        'semiperimeter': 'Semiperimeter', 'side': 'Side', 'base_perimeter': 'Base perimeter', 'lateral_area': 'Lateral area',
        'volume': 'Volume', 'surface_area': 'Surface area', 'base_area': 'Base area', 'slant_height': 'Slant height',
        'bmr_harris': 'BMR Harris-Benedict', 'tdee_sedentary': 'TDEE Sedentary', 'tdee_light': 'TDEE Light',
        'tdee_moderate': 'TDEE Moderate', 'tdee_active': 'TDEE Active', 'tdee_very_active': 'TDEE Very active',
        'bmr_katch': 'BMR Katch-McArdle', 'lbm': 'Lean body mass', 'tdee': 'TDEE',
        'calorias_mantenimiento': 'Maintenance calories', 'proteinas': 'Protein', 'grasas': 'Fats', 'carbohidratos': 'Carbs',
        'category': 'Category', 'map': 'MAP', 'pulse_pressure': 'Pulse pressure',
        'whr': 'Waist-hip ratio', 'risk': 'Risk', 'ideal': 'Ideal',
        'weight_lost': 'Weight lost', 'remaining': 'Remaining',
        'fc_max': 'Max HR', 'z1_recovery': 'Z1 Recovery', 'z2_fat_burn': 'Z2 Fat burn',
        'z3_aerobic': 'Z3 Aerobic', 'z4_threshold': 'Z4 Threshold', 'z5_maximum': 'Z5 Maximum',
        'hourly': 'Hourly', 'monthly': 'Monthly', 'weekly': 'Weekly', 'daily': 'Daily',
        'annual': 'Annual', 'monthly_val': 'Monthly', 'weekly_val': 'Weekly', 'daily_val': 'Daily',
        'monthly_payment': 'Monthly payment', 'loan_amount': 'Loan amount', 'total_paid': 'Total paid',
        'total_interest': 'Total interest', 'interest_ratio': 'Interest ratio',
        'months_to_payoff': 'Months to payoff', 'final_amount': 'Final amount',
        'total_contributed': 'Total contributed', 'margin_pct': 'Margin %', 'markup_pct': 'Markup %', 'profit': 'Profit',
        'npv': 'NPV', 'roi_annual': 'Annual ROI', 'payback_years': 'Payback years',
        'emergency_fund': 'Emergency fund', 'monthly_val2': 'Monthly',
        'age_years': 'Years', 'age_months': 'Months', 'age_days': 'Days', 'age_hours': 'Hours', 'days_until_birthday': 'Days to birthday',
        'total_days': 'Total days', 'total_weeks': 'Total weeks', 'total_months': 'Total months', 'total_years': 'Total years',
        'tip': 'Tip', 'per_person': 'Per person', 'tip_per_person': 'Tip per person',
        'final_price': 'Final price', 'total_savings': 'Total savings', 'savings_pct': 'Savings %',
        'kinetic_energy': 'Kinetic energy', 'joules': 'Joules', 'calories': 'Calories',
        'potential_energy': 'Potential energy', 'work': 'Work', 'power': 'Power', 'watts': 'Watts',
        'voltage': 'Voltage', 'current': 'Current', 'resistance': 'Resistance',
        'force': 'Force', 'final_velocity': 'Final velocity', 'distance': 'Distance',
        'one_rep_max': '1RM', 'at_90pct': '90%', 'at_80pct': '80%', 'at_70pct': '70%',
        'pace_min_km': 'Pace min/km', 'speed_kmh': 'Speed km/h', 'time_5k': '5K time',
        'time_10k': '10K time', 'time_half_marathon': 'Half marathon', 'time_marathon': 'Marathon',
        'vo2_max': 'VO2 max', 'calories_burned': 'Calories burned', 'fitness_level': 'Fitness level',
        'radians': 'Radians', 'gradians': 'Gradians',
        'fahrenheit': 'Fahrenheit', 'kelvin': 'Kelvin', 'rankine': 'Rankine',
        'kilocalories': 'Kilocalories', 'watt_hours': 'Wh', 'kilowatt_hours': 'kWh',
        'combinations': 'Combinations', 'permutations': 'Permutations',
        'z_score': 'Z-score', 'percentile': 'Percentile', 'classification': 'Classification',
        'sample_size': 'Sample size', 'standard_error': 'Standard error', 'margin_of_error': 'Margin of error',
        'ci_lower': 'CI lower', 'ci_upper': 'CI upper',
        'bsa': 'BSA', 'ideal_weight': 'Ideal weight', 'adjusted_weight': 'Adjusted weight',
        'a1c_estimated': 'A1c estimated', 'glucose': 'Glucose',
        'ldl': 'LDL', 'total_hdl_ratio': 'Total/HDL ratio',
    }
}

# Spanish calculator names for new calculators
SPANISH_NAMES = {
    'fraction-calculator': {'name': 'Calculadora de Fracciones', 'desc': 'Convierte fracciones a decimales, enteros y porcentajes.'},
    'slope-calculator': {'name': 'Calculadora de Pendiente', 'desc': 'Calcula la pendiente, interseccion y distancia entre dos puntos.'},
    'scientific-notation': {'name': 'Notacion Cientifica', 'desc': 'Convierte numeros a notacion cientifica e ingenieria.'},
    'rounding-calculator': {'name': 'Redondeo', 'desc': 'Redondea numeros a los decimales deseados.'},
    'gcf-lcm-calculator': {'name': 'MCD y mcm', 'desc': 'Calcula el maximo comun divisor y minimo comun multiplo.'},
    'prime-factorization': {'name': 'Factorizacion Prima', 'desc': 'Descompone un numero en sus factores primos.'},
    'ratio-calculator': {'name': 'Razon y Proporcion', 'desc': 'Calcula razones, proporciones y simplifica.'},
    'proportion-calculator': {'name': 'Regla de Tres', 'desc': 'Resuelve proporciones y regla de tres.'},
    'mean-average-calculator': {'name': 'Media y Promedio', 'desc': 'Calcula la media, rango y estadisticas basicas.'},
    'circle-calculator': {'name': 'Circulo', 'desc': 'Calcula area, circunferencia y diametro de un circulo.'},
    'right-triangle-calculator': {'name': 'Triangulo Rectangulo', 'desc': 'Resuelve triangulos rectangulos con Pitagoras.'},
    'heron-triangle-area': {'name': 'Area Triangulo Heron', 'desc': 'Calcula el area de un triangulo con tres lados.'},
    'rectangle-calculator': {'name': 'Rectangulo', 'desc': 'Calcula area, perimetro y diagonal de un rectangulo.'},
    'square-calculator': {'name': 'Cuadrado', 'desc': 'Calcula area, perimetro y diagonal de un cuadrado.'},
    'trapezoid-calculator': {'name': 'Trapecio', 'desc': 'Calcula area y perimetro de un trapecio.'},
    'cylinder-volume': {'name': 'Volumen Cilindro', 'desc': 'Calcula volumen y area de un cilindro.'},
    'cone-volume': {'name': 'Volumen Cono', 'desc': 'Calcula volumen y area de un cono.'},
    'pyramid-volume': {'name': 'Volumen Piramide', 'desc': 'Calcula volumen y area de una piramide.'},
    'sphere-calculator': {'name': 'Esfera', 'desc': 'Calcula volumen y area de una esfera.'},
    'bmr-harris-benedict': {'name': 'TMB Harris-Benedict', 'desc': 'Calcula tu Tasa Metabolica Basal con la formula Harris-Benedict.'},
    'bmr-katch-mcardle': {'name': 'TMB Katch-McArdle', 'desc': 'Calcula tu TMB con la formula Katch-McArdle.'},
    'macro-calculator': {'name': 'Calculadora de Macros', 'desc': 'Calcula proteinas, carbohidratos y grasas diarias.'},
    'blood-pressure': {'name': 'Presion Arterial', 'desc': 'Evalua tu presion arterial y categoria de riesgo.'},
    'waist-hip-ratio': {'name': 'Indice Cintura-Cadera', 'desc': 'Calcula tu relacion cintura-cadera y riesgo cardiovascular.'},
    'waist-height-ratio': {'name': 'Indice Cintura-Altura', 'desc': 'Evalua tu riesgo metabolico con cintura/altura.'},
    'weight-loss-percentage': {'name': 'Porcentaje Perdida Peso', 'desc': 'Calcula el porcentaje de peso perdido.'},
    'heart-rate-zones': {'name': 'Zonas de Frecuencia Cardiaca', 'desc': 'Calcula tus 5 zonas de entrenamiento cardiaco.'},
    'salary-to-hourly': {'name': 'Salario a Hora', 'desc': 'Convierte salario anual a hora, mes y dia.'},
    'hourly-to-salary': {'name': 'Hora a Salario', 'desc': 'Convierte tarifa horaria a salario anual.'},
    'mortgage-calculator': {'name': 'Hipoteca', 'desc': 'Calcula cuota mensual, intereses totales y capital de tu hipoteca.'},
    'debt-payoff': {'name': 'Pago Deuda', 'desc': 'Calcula cuanto tardaras en pagar tu deuda.'},
    'savings-calculator': {'name': 'Ahorro', 'desc': 'Proyecta el crecimiento de tus ahorros con interes compuesto.'},
    'profit-margin': {'name': 'Margen de Beneficio', 'desc': 'Calcula margen, markup y ganancia.'},
    'npv-calculator': {'name': 'VAN / NPV', 'desc': 'Calcula el Valor Actual Neto de una inversion.'},
    'emergency-fund': {'name': 'Fondo de Emergencia', 'desc': 'Calcula cuanto necesitas en tu fondo de emergencia.'},
    'age-calculator-advanced': {'name': 'Calculadora de Edad Avanzada', 'desc': 'Calcula tu edad exacta en anos, meses, dias y horas.'},
    'date-difference': {'name': 'Diferencia de Fechas', 'desc': 'Calcula la diferencia entre dos fechas.'},
    'tip-calculator-advanced': {'name': 'Propina Avanzada', 'desc': 'Calcula propina dividida entre varias personas.'},
    'double-discount': {'name': 'Doble Descuento', 'desc': 'Calcula el precio final con dos descuentos acumulados.'},
    'kinetic-energy': {'name': 'Energia Cinetica', 'desc': 'Calcula energia cinetica en julios y calorias.'},
    'potential-energy': {'name': 'Energia Potencial', 'desc': 'Calcula energia potencial gravitatoria.'},
    'work-power': {'name': 'Trabajo y Potencia', 'desc': 'Calcula trabajo y potencia mecanica.'},
    'ohms-law-power': {'name': 'Ley de Ohm + Potencia', 'desc': 'Resuelve circuitos electricos con V, I, R y P.'},
    'newtons-second-law': {'name': 'Segunda Ley de Newton', 'desc': 'Calcula fuerza, velocidad y distancia.'},
    'one-rep-max': {'name': '1 Repeticion Maxima', 'desc': 'Estima tu 1RM y cargas de entrenamiento.'},
    'running-pace-predictor': {'name': 'Prediccion Ritmo Carrera', 'desc': 'Predice tiempos de 5K, 10K, media maraton y maraton.'},
    'vo2-max-estimator': {'name': 'Estimador VO2 Max', 'desc': 'Estima tu VO2 max y nivel de forma fisica.'},
    'angle-converter': {'name': 'Conversor de Angulos', 'desc': 'Convierte grados a radianes y gradianes.'},
    'temperature-full': {'name': 'Temperatura Completa', 'desc': 'Convierte Celsius a Fahrenheit, Kelvin y Rankine.'},
    'energy-converter': {'name': 'Conversor de Energia', 'desc': 'Convierte julios a calorias, kWh y mas.'},
    'combinations-permutations': {'name': 'Combinaciones y Permutaciones', 'desc': 'Calcula combinaciones y permutaciones.'},
    'z-score-percentile': {'name': 'Z-Score y Percentil', 'desc': 'Calcula z-score, percentil y clasificacion.'},
    'sample-size-confidence': {'name': 'Tamano Muestra e IC', 'desc': 'Calcula error estandar, margen de error e intervalo de confianza.'},
    'bsa-ideal-weight': {'name': 'ASC y Peso Ideal', 'desc': 'Calcula area superficie corporal y peso ideal.'},
    'a1c-estimator': {'name': 'Estimador A1c', 'desc': 'Estima tu A1c a partir de glucosa en sangre.'},
    'cholesterol-ldl': {'name': 'Colesterol LDL', 'desc': 'Calcula LDL estimado y ratio Total/HDL.'},
}

ENGLISH_NAMES = {
    'fraction-calculator': {'name': 'Fraction Calculator', 'desc': 'Convert fractions to decimals, whole numbers and percentages.'},
    'slope-calculator': {'name': 'Slope Calculator', 'desc': 'Calculate slope, intercept and distance between two points.'},
    'scientific-notation': {'name': 'Scientific Notation', 'desc': 'Convert numbers to scientific and engineering notation.'},
    'rounding-calculator': {'name': 'Rounding Calculator', 'desc': 'Round numbers to desired decimal places.'},
    'gcf-lcm-calculator': {'name': 'GCF and LCM', 'desc': 'Calculate greatest common factor and least common multiple.'},
    'prime-factorization': {'name': 'Prime Factorization', 'desc': 'Decompose a number into its prime factors.'},
    'ratio-calculator': {'name': 'Ratio Calculator', 'desc': 'Calculate ratios, proportions and simplify.'},
    'proportion-calculator': {'name': 'Proportion Calculator', 'desc': 'Solve proportions and rule of three.'},
    'mean-average-calculator': {'name': 'Mean and Average', 'desc': 'Calculate mean, range and basic statistics.'},
    'circle-calculator': {'name': 'Circle Calculator', 'desc': 'Calculate area, circumference and diameter of a circle.'},
    'right-triangle-calculator': {'name': 'Right Triangle Calculator', 'desc': 'Solve right triangles with Pythagorean theorem.'},
    'heron-triangle-area': {'name': 'Heron Triangle Area', 'desc': 'Calculate triangle area from three sides.'},
    'rectangle-calculator': {'name': 'Rectangle Calculator', 'desc': 'Calculate area, perimeter and diagonal.'},
    'square-calculator': {'name': 'Square Calculator', 'desc': 'Calculate area, perimeter and diagonal.'},
    'trapezoid-calculator': {'name': 'Trapezoid Calculator', 'desc': 'Calculate area and perimeter of a trapezoid.'},
    'cylinder-volume': {'name': 'Cylinder Volume', 'desc': 'Calculate volume and surface area of a cylinder.'},
    'cone-volume': {'name': 'Cone Volume', 'desc': 'Calculate volume and surface area of a cone.'},
    'pyramid-volume': {'name': 'Pyramid Volume', 'desc': 'Calculate volume and surface area of a pyramid.'},
    'sphere-calculator': {'name': 'Sphere Calculator', 'desc': 'Calculate volume and surface area of a sphere.'},
    'bmr-harris-benedict': {'name': 'BMR Harris-Benedict', 'desc': 'Calculate Basal Metabolic Rate using Harris-Benedict equation.'},
    'bmr-katch-mcardle': {'name': 'BMR Katch-McArdle', 'desc': 'Calculate BMR using Katch-McArdle formula.'},
    'macro-calculator': {'name': 'Macro Calculator', 'desc': 'Calculate daily protein, carbs and fats.'},
    'blood-pressure': {'name': 'Blood Pressure', 'desc': 'Evaluate blood pressure and risk category.'},
    'waist-hip-ratio': {'name': 'Waist-Hip Ratio', 'desc': 'Calculate waist-hip ratio and cardiovascular risk.'},
    'waist-height-ratio': {'name': 'Waist-Height Ratio', 'desc': 'Assess metabolic risk with waist/height ratio.'},
    'weight-loss-percentage': {'name': 'Weight Loss Percentage', 'desc': 'Calculate percentage of weight lost.'},
    'heart-rate-zones': {'name': 'Heart Rate Zones', 'desc': 'Calculate your 5 heart rate training zones.'},
    'salary-to-hourly': {'name': 'Salary to Hourly', 'desc': 'Convert annual salary to hourly, monthly and daily.'},
    'hourly-to-salary': {'name': 'Hourly to Salary', 'desc': 'Convert hourly rate to annual salary.'},
    'mortgage-calculator': {'name': 'Mortgage Calculator', 'desc': 'Calculate monthly payment, total interest and loan amount.'},
    'debt-payoff': {'name': 'Debt Payoff', 'desc': 'Calculate how long to pay off your debt.'},
    'savings-calculator': {'name': 'Savings Calculator', 'desc': 'Project savings growth with compound interest.'},
    'profit-margin': {'name': 'Profit Margin', 'desc': 'Calculate margin, markup and profit.'},
    'npv-calculator': {'name': 'NPV Calculator', 'desc': 'Calculate Net Present Value of an investment.'},
    'emergency-fund': {'name': 'Emergency Fund', 'desc': 'Calculate how much you need in your emergency fund.'},
    'age-calculator-advanced': {'name': 'Advanced Age Calculator', 'desc': 'Calculate exact age in years, months, days and hours.'},
    'date-difference': {'name': 'Date Difference', 'desc': 'Calculate difference between two dates.'},
    'tip-calculator-advanced': {'name': 'Advanced Tip Calculator', 'desc': 'Calculate tip split among multiple people.'},
    'double-discount': {'name': 'Double Discount', 'desc': 'Calculate final price with two stacked discounts.'},
    'kinetic-energy': {'name': 'Kinetic Energy', 'desc': 'Calculate kinetic energy in joules and calories.'},
    'potential-energy': {'name': 'Potential Energy', 'desc': 'Calculate gravitational potential energy.'},
    'work-power': {'name': 'Work and Power', 'desc': 'Calculate mechanical work and power.'},
    'ohms-law-power': {'name': "Ohm's Law + Power", 'desc': 'Solve electrical circuits with V, I, R and P.'},
    'newtons-second-law': {'name': "Newton's Second Law", 'desc': 'Calculate force, velocity and distance.'},
    'one-rep-max': {'name': 'One Rep Max', 'desc': 'Estimate 1RM and training loads.'},
    'running-pace-predictor': {'name': 'Running Pace Predictor', 'desc': 'Predict 5K, 10K, half marathon and marathon times.'},
    'vo2-max-estimator': {'name': 'VO2 Max Estimator', 'desc': 'Estimate your VO2 max and fitness level.'},
    'angle-converter': {'name': 'Angle Converter', 'desc': 'Convert degrees to radians and gradians.'},
    'temperature-full': {'name': 'Temperature Converter', 'desc': 'Convert Celsius to Fahrenheit, Kelvin and Rankine.'},
    'energy-converter': {'name': 'Energy Converter', 'desc': 'Convert joules to calories, kWh and more.'},
    'combinations-permutations': {'name': 'Combinations & Permutations', 'desc': 'Calculate combinations and permutations.'},
    'z-score-percentile': {'name': 'Z-Score & Percentile', 'desc': 'Calculate z-score, percentile and classification.'},
    'sample-size-confidence': {'name': 'Sample Size & CI', 'desc': 'Calculate standard error, margin of error and confidence interval.'},
    'bsa-ideal-weight': {'name': 'BSA & Ideal Weight', 'desc': 'Calculate body surface area and ideal weight.'},
    'a1c-estimator': {'name': 'A1c Estimator', 'desc': 'Estimate A1c from blood glucose.'},
    'cholesterol-ldl': {'name': 'Cholesterol LDL', 'desc': 'Calculate estimated LDL and Total/HDL ratio.'},
}

# Generate SEO titles and descriptions
def seo_title(name): return name + ' - Free Online Calculator'
def seo_desc(name, desc): return desc + ' Calculate instantly and for free with CalcToWork.'

# Update i18n files
for lang in LANGS:
    i18n_path = I18N_DIR / f'{lang}.json'
    with open(i18n_path, 'r', encoding='utf-8') as fp:
        i18n = json.load(fp)
    
    if 'calculators' not in i18n:
        i18n['calculators'] = {}
    
    # Translate function (simple: use English for missing languages)
    def translate(key, lang):
        if lang == 'es':
            return I18N_TEMPLATES['es'].get(key, key)
        elif lang in ('fr', 'pt', 'de', 'it'):
            # Use English as fallback for now
            return I18N_TEMPLATES['en'].get(key, key)
        return I18N_TEMPLATES['en'].get(key, key)
    
    for calc in new_calcs:
        cid = calc['id']
        slug = calc['slug']
        
        if lang == 'es':
            names = SPANISH_NAMES.get(slug, {'name': slug, 'desc': ''})
        else:
            names = ENGLISH_NAMES.get(slug, {'name': slug, 'desc': ''})
        
        # Build inputs dict
        inputs_dict = {}
        for inp in calc['inputs']:
            key = inp['id']
            # Default label = key
            inputs_dict[key] = translate(key, lang)
        
        # Build outputs dict
        outputs_dict = {}
        for o in calc['outputs']:
            key = o['id']
            outputs_dict[key] = translate(key, lang)
        
        i18n['calculators'][cid] = {
            'name': names['name'],
            'desc': names['desc'],
            'description': names['desc'],
            'seo_title': seo_title(names['name']),
            'seo_description': seo_desc(names['name'], names['desc']),
            'inputs': inputs_dict,
            'outputs': outputs_dict
        }
    
    with open(i18n_path, 'w', encoding='utf-8') as fp:
        json.dump(i18n, fp, ensure_ascii=False, indent=2)
    print(f'Updated {i18n_path}')

print(f'\\nTotal calculators: {len(calcs)}')
print('Done! Run: python scripts/generate_calctowork.py')
