#!/usr/bin/env python3
"""Phase 2: Add ~65 calculators. Run with: python scripts/phase2_add_calcs.py"""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

CALC_FILE = os.path.join(BASE, "src", "calculators", "calculators.json")
I18N_DIR  = os.path.join(BASE, "src", "i18n")
TOOLS_FILE = os.path.join(BASE, "scripts", "tools_config.py")
CONTENT_FILE = os.path.join(BASE, "scripts", "calc_content.py")
LANGS = ["es", "en", "fr", "pt", "de", "it"]

def ni(id_, unit="", default=0, min_=0, max_=1e12, step="any"):
    return {"id": id_, "type": "number", "min": min_, "max": max_, "step": step, "default": default, "unit": unit}

def ou(id_, unit="", hl=False):
    o = {"id": id_, "unit": unit}
    if hl: o["highlight"] = True
    return o

# ══════════════════════════════════════════════════════════════════
# STEP 1: Calculator definitions (formula JS + inputs + outputs)
# ══════════════════════════════════════════════════════════════════

def build_calculators():
    C = []
    VINPUTS = [ni(f"v{i}","",0) for i in range(1,11)]
    VLABELS = [f"v{i}" for i in range(1,11)]

    # ── STATISTICS (estadistica, block 14) ──
    C.append({"id":"600","slug":"media","block":14,"block_slug":"estadistica",
        "inputs": VINPUTS,
        "formula":"var vals=[],K=['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10'];for(var i=0;i<K.length;i++){var r=inputs[K[i]],v=parseFloat(r);if(r!==''&&r!==undefined&&!isNaN(v))vals.push(v);}if(!vals.length)return{error:true};var s=0;for(var i=0;i<vals.length;i++)s+=vals[i];return{media:+(s/vals.length).toFixed(4),suma:+s.toFixed(4),cantidad:vals.length};",
        "outputs":[ou("media","",True),ou("suma",""),ou("cantidad","")],"related":["602","608","601"]})

    C.append({"id":"601","slug":"mediana","block":14,"block_slug":"estadistica",
        "inputs": VINPUTS,
        "formula":"var vals=[],K=['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10'];for(var i=0;i<K.length;i++){var r=inputs[K[i]],v=parseFloat(r);if(r!==''&&r!==undefined&&!isNaN(v))vals.push(v);}if(!vals.length)return{error:true};vals.sort(function(a,b){return a-b;});var n=vals.length,m;if(n%2===1)m=vals[Math.floor(n/2)];else m=(vals[n/2-1]+vals[n/2])/2;return{mediana:+m.toFixed(4),cantidad:n,minimo:vals[0],maximo:vals[n-1]};",
        "outputs":[ou("mediana","",True),ou("cantidad",""),ou("minimo",""),ou("maximo","")],"related":["600","602","608"]})

    C.append({"id":"602","slug":"desviacion-estandar","block":14,"block_slug":"estadistica",
        "inputs": VINPUTS,
        "formula":"var vals=[],K=['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10'];for(var i=0;i<K.length;i++){var r=inputs[K[i]],v=parseFloat(r);if(r!==''&&r!==undefined&&!isNaN(v))vals.push(v);}if(vals.length<2)return{error:true};var n=vals.length,s=0;for(var i=0;i<n;i++)s+=vals[i];var m=s/n,ss=0;for(var i=0;i<n;i++)ss+=Math.pow(vals[i]-m,2);return{desv_est_muestra:+Math.sqrt(ss/(n-1)).toFixed(4),desv_est_poblacion:+Math.sqrt(ss/n).toFixed(4),varianza_muestra:+(ss/(n-1)).toFixed(4),media:+m.toFixed(4),cantidad:n};",
        "outputs":[ou("desv_est_muestra","",True),ou("desv_est_poblacion",""),ou("varianza_muestra",""),ou("media",""),ou("cantidad","")],"related":["600","608","601"]})

    C.append({"id":"603","slug":"probabilidad","block":14,"block_slug":"estadistica",
        "inputs":[ni("favorables","",1,0,1e9),ni("totales","",100,1,1e12)],
        "formula":"var F=parseFloat(inputs.favorables)||0,T=parseFloat(inputs.totales)||0;if(!T)return{error:true};var p=F/T;return{probabilidad:+p.toFixed(6),porcentaje:+(p*100).toFixed(2),complementaria:+((1-p)*100).toFixed(2)};",
        "outputs":[ou("probabilidad","",True),ou("porcentaje","%"),ou("complementaria","%")],"related":["604","605","606"]})

    C.append({"id":"604","slug":"combinaciones","block":14,"block_slug":"estadistica",
        "inputs":[ni("n","",10,0,170),ni("r","",3,0,170)],
        "formula":"var n=parseFloat(inputs.n)||0,r=parseFloat(inputs.r)||0;if(r>n||n<0||r<0)return{error:true};function f(x){var v=1;for(var i=2;i<=x;i++)v*=i;return v;}var res=f(n)/(f(r)*f(n-r));return{resultado:res,formula:'C('+n+','+r+')'};",
        "outputs":[ou("resultado","",True),ou("formula","")],"related":["605","603","609"]})

    C.append({"id":"605","slug":"permutaciones","block":14,"block_slug":"estadistica",
        "inputs":[ni("n","",10,0,170),ni("r","",3,0,170)],
        "formula":"var n=parseFloat(inputs.n)||0,r=parseFloat(inputs.r)||0;if(r>n||n<0||r<0)return{error:true};function f(x){var v=1;for(var i=2;i<=x;i++)v*=i;return v;}var res=f(n)/f(n-r);return{resultado:res,formula:'P('+n+','+r+')'};",
        "outputs":[ou("resultado","",True),ou("formula","")],"related":["604","603","609"]})

    C.append({"id":"606","slug":"intervalo-confianza","block":14,"block_slug":"estadistica",
        "inputs":[ni("media","",50),ni("desviacion","",10,0.001),ni("n","",100,2,1e9),ni("confianza","",95,1,99.9)],
        "formula":"var m=parseFloat(inputs.media)||0,s=parseFloat(inputs.desviacion)||0,n=parseFloat(inputs.n)||0,c=parseFloat(inputs.confianza)||95;if(!n||!s)return{error:true};var z=c>=99?2.576:c>=98?2.326:c>=95?1.96:c>=90?1.645:1.036;var se=s/Math.sqrt(n),me=z*se;return{limite_inferior:+(m-me).toFixed(4),limite_superior:+(m+me).toFixed(4),margen_error:+me.toFixed(4),error_estandar:+se.toFixed(4)};",
        "outputs":[ou("limite_inferior","",True),ou("limite_superior",""),ou("margen_error",""),ou("error_estandar","")],"related":["600","602","608"]})

    C.append({"id":"607","slug":"coeficiente-variacion","block":14,"block_slug":"estadistica",
        "inputs":[ni("desviacion","",10,0.001),ni("media","",50)],
        "formula":"var s=parseFloat(inputs.desviacion)||0,m=parseFloat(inputs.media)||0;if(!m)return{error:true};return{cv_porcentaje:+(s/m*100).toFixed(2)};",
        "outputs":[ou("cv_porcentaje","%",True)],"related":["602","600","608"]})

    C.append({"id":"608","slug":"varianza","block":14,"block_slug":"estadistica",
        "inputs": VINPUTS,
        "formula":"var vals=[],K=['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10'];for(var i=0;i<K.length;i++){var r=inputs[K[i]],v=parseFloat(r);if(r!==''&&r!==undefined&&!isNaN(v))vals.push(v);}if(vals.length<2)return{error:true};var n=vals.length,s=0;for(var i=0;i<n;i++)s+=vals[i];var m=s/n,ss=0;for(var i=0;i<n;i++)ss+=Math.pow(vals[i]-m,2);return{varianza_poblacion:+(ss/n).toFixed(4),varianza_muestra:+(ss/(n-1)).toFixed(4),desv_est:+Math.sqrt(ss/(n-1)).toFixed(4),media:+m.toFixed(4)};",
        "outputs":[ou("varianza_poblacion","",True),ou("varianza_muestra",""),ou("desv_est",""),ou("media","")],"related":["602","600","601"]})

    C.append({"id":"609","slug":"puntuacion-z","block":14,"block_slug":"estadistica",
        "inputs":[ni("valor","",75),ni("media","",70),ni("desviacion","",10,0.001)],
        "formula":"var x=parseFloat(inputs.valor)||0,m=parseFloat(inputs.media)||0,s=parseFloat(inputs.desviacion)||0;if(!s)return{error:true};var z=(x-m)/s;function erf(t){var a1=.254829592,a2=-.284496736,a3=1.421413741,a4=-1.453152027,a5=1.061405429,p=.3275911,sg=t<0?-1:1;t=Math.abs(t);var u=1/(1+p*t);return sg*(1-(((((a5*u+a4)*u)+a3)*u+a2)*u+a1)*u*Math.exp(-t*t));}return{z_score:+z.toFixed(4),porcentil:+(0.5*(1+erf(z/Math.sqrt(2)))*100).toFixed(2)};",
        "outputs":[ou("z_score","",True),ou("porcentil","%")],"related":["602","606","600"]})

    # ── SCIENCE / PHYSICS (ciencia, block 15) ──
    C.append({"id":"700","slug":"velocidad","block":15,"block_slug":"ciencia",
        "inputs":[ni("distancia","",100,0),ni("tiempo","",2,0.001)],
        "formula":"var d=parseFloat(inputs.distancia)||0,t=parseFloat(inputs.tiempo)||0;if(!t)return{error:true};var v=d/t;return{velocidad_ms:+v.toFixed(4),velocidad_kmh:+(v*3.6).toFixed(2),velocidad_mph:+(v*2.237).toFixed(2)};",
        "outputs":[ou("velocidad_ms","m/s",True),ou("velocidad_kmh","km/h"),ou("velocidad_mph","mph")],"related":["701","709","805"]})

    C.append({"id":"701","slug":"densidad","block":15,"block_slug":"ciencia",
        "inputs":[ni("masa","",100,0),ni("volumen","",50,0.001)],
        "formula":"var m=parseFloat(inputs.masa)||0,v=parseFloat(inputs.volumen)||0;if(!v)return{error:true};return{densidad:+(m/v).toFixed(4),densidad_gl:+(m/v*0.001).toFixed(4)};",
        "outputs":[ou("densidad","kg/m\u00b3",True),ou("densidad_gl","g/L")],"related":["700","702","800"]})

    C.append({"id":"702","slug":"fuerza","block":15,"block_slug":"ciencia",
        "inputs":[ni("masa","",10,0),ni("aceleracion","",9.81,0)],
        "formula":"var m=parseFloat(inputs.masa)||0,a=parseFloat(inputs.aceleracion)||0;var f=m*a;return{fuerza_n:+f.toFixed(4),fuerza_kgf:+(f/9.80665).toFixed(4),fuerza_lbf:+(f/4.448222).toFixed(4)};",
        "outputs":[ou("fuerza_n","N",True),ou("fuerza_kgf","kgf"),ou("fuerza_lbf","lbf")],"related":["703","704","706"]})

    C.append({"id":"703","slug":"energia-cinetica","block":15,"block_slug":"ciencia",
        "inputs":[ni("masa","",10,0),ni("velocidad","",15,0)],
        "formula":"var m=parseFloat(inputs.masa)||0,v=parseFloat(inputs.velocidad)||0;var ke=.5*m*v*v;return{energia_j:+ke.toFixed(4),energia_kj:+(ke/1000).toFixed(4),velocidad_kmh:+(v*3.6).toFixed(2)};",
        "outputs":[ou("energia_j","J",True),ou("energia_kj","kJ"),ou("velocidad_kmh","km/h")],"related":["704","702","706"]})

    C.append({"id":"704","slug":"energia-potencial","block":15,"block_slug":"ciencia",
        "inputs":[ni("masa","",10,0),ni("altura","",5,0),ni("gravedad","",9.81,0)],
        "formula":"var m=parseFloat(inputs.masa)||0,h=parseFloat(inputs.altura)||0,g=parseFloat(inputs.gravedad)||9.81;var pe=m*g*h;return{energia_j:+pe.toFixed(4),energia_kj:+(pe/1000).toFixed(4)};",
        "outputs":[ou("energia_j","J",True),ou("energia_kj","kJ")],"related":["703","702","706"]})

    C.append({"id":"705","slug":"presion","block":15,"block_slug":"ciencia",
        "inputs":[ni("fuerza","",100,0),ni("area","",2,0.001)],
        "formula":"var f=parseFloat(inputs.fuerza)||0,a=parseFloat(inputs.area)||0;if(!a)return{error:true};var p=f/a;return{presion_pa:+p.toFixed(2),presion_atm:+(p/101325).toFixed(6),presion_bar:+(p/100000).toFixed(6),presion_psi:+(p/6894.76).toFixed(4)};",
        "outputs":[ou("presion_pa","Pa",True),ou("presion_atm","atm"),ou("presion_bar","bar"),ou("presion_psi","psi")],"related":["702","807","701"]})

    C.append({"id":"706","slug":"trabajo-mecanico","block":15,"block_slug":"ciencia",
        "inputs":[ni("fuerza","",100,0),ni("distancia","",5,0),ni("angulo","",0,0,360)],
        "formula":"var f=parseFloat(inputs.fuerza)||0,d=parseFloat(inputs.distancia)||0,a=parseFloat(inputs.angulo)||0;var w=f*d*Math.cos(a*Math.PI/180);return{trabajo_j:+w.toFixed(4),trabajo_kj:+(w/1000).toFixed(4)};",
        "outputs":[ou("trabajo_j","J",True),ou("trabajo_kj","kJ")],"related":["702","703","704"]})

    C.append({"id":"707","slug":"ley-ohm","block":15,"block_slug":"ciencia",
        "inputs":[ni("voltaje","",12),ni("corriente","",2),ni("resistencia","",0)],
        "formula":"var V=parseFloat(inputs.voltaje),I=parseFloat(inputs.corriente),R=parseFloat(inputs.resistencia);if(!isNaN(V)&&!isNaN(I)&&V&&I)return{voltaje:V,corriente:+I.toFixed(4),resistencia:+(V/I).toFixed(4)};if(!isNaN(V)&&!isNaN(R)&&V&&R)return{voltaje:V,corriente:+(V/R).toFixed(4),resistencia:R};if(!isNaN(I)&&!isNaN(R)&&I&&R)return{voltaje:+(I*R).toFixed(4),corriente:I,resistencia:R};return{error:true};",
        "outputs":[ou("voltaje","V",True),ou("corriente","A"),ou("resistencia","\u03a9")],"related":["708","705","702"]})

    C.append({"id":"708","slug":"potencia-electrica","block":15,"block_slug":"ciencia",
        "inputs":[ni("voltaje","",220),ni("corriente","",10)],
        "formula":"var V=parseFloat(inputs.voltaje)||0,I=parseFloat(inputs.corriente)||0;var p=V*I;return{potencia_w:+p.toFixed(2),potencia_kw:+(p/1000).toFixed(4),potencia_hp:+(p/745.7).toFixed(4)};",
        "outputs":[ou("potencia_w","W",True),ou("potencia_kw","kW"),ou("potencia_hp","HP")],"related":["707","705","706"]})

    C.append({"id":"709","slug":"aceleracion","block":15,"block_slug":"ciencia",
        "inputs":[ni("vi","",0),ni("vf","",30),ni("tiempo","",5,0.001)],
        "formula":"var vi=parseFloat(inputs.vi)||0,vf=parseFloat(inputs.vf)||0,t=parseFloat(inputs.tiempo)||0;if(!t)return{error:true};var a=(vf-vi)/t;return{aceleracion:+a.toFixed(4),aceleracion_g:+(a/9.80665).toFixed(4)};",
        "outputs":[ou("aceleracion","m/s\u00b2",True),ou("aceleracion_g","g")],"related":["700","702","703"]})

    # ── CONVERSIONS (conversion, block 16) ──
    C.append({"id":"800","slug":"longitud","block":16,"block_slug":"conversion",
        "inputs":[ni("valor_m","",1,0)],
        "formula":"var m=parseFloat(inputs.valor_m)||0;return{km:+(m/1000).toFixed(6),cm:+(m*100).toFixed(4),mm:+(m*1000).toFixed(4),ft:+(m*3.28084).toFixed(6),in_:+(m*39.3701).toFixed(6),yd:+(m*1.09361).toFixed(6),mi:+(m/1609.34).toFixed(8)};",
        "outputs":[ou("km","km",True),ou("cm","cm"),ou("mm","mm"),ou("ft","ft"),ou("in_","in"),ou("yd","yd"),ou("mi","mi")],"related":["801","804","803"]})

    C.append({"id":"801","slug":"peso","block":16,"block_slug":"conversion",
        "inputs":[ni("valor_kg","",1,0)],
        "formula":"var kg=parseFloat(inputs.valor_kg)||0;return{g:+(kg*1000).toFixed(4),mg:+(kg*1e6).toFixed(2),lb:+(kg*2.20462).toFixed(6),oz:+(kg*35.274).toFixed(4),ton:+(kg/1000).toFixed(6),stone:+(kg/6.35029).toFixed(6)};",
        "outputs":[ou("g","g",True),ou("mg","mg"),ou("lb","lb"),ou("oz","oz"),ou("ton","t"),ou("stone","st")],"related":["800","802","803"]})

    C.append({"id":"802","slug":"temperatura","block":16,"block_slug":"conversion",
        "inputs":[ni("celsius","",25)],
        "formula":"var c=parseFloat(inputs.celsius)||0;return{fahrenheit:+(c*9/5+32).toFixed(2),kelvin:+(c+273.15).toFixed(2)};",
        "outputs":[ou("fahrenheit","\u00b0F",True),ou("kelvin","K")],"related":["800","801","805"]})

    C.append({"id":"803","slug":"volumen","block":16,"block_slug":"conversion",
        "inputs":[ni("valor_l","",1,0)],
        "formula":"var l=parseFloat(inputs.valor_l)||0;return{ml:+(l*1000).toFixed(4),gal_us:+(l/3.78541).toFixed(6),gal_uk:+(l/4.54609).toFixed(6),m3:+(l/1000).toFixed(6),ft3:+(l/28.3168).toFixed(6),oz_fl:+(l*33.814).toFixed(4)};",
        "outputs":[ou("ml","mL",True),ou("gal_us","gal (US)"),ou("gal_uk","gal (UK)"),ou("m3","m\u00b3"),ou("ft3","ft\u00b3"),ou("oz_fl","fl oz")],"related":["800","801","804"]})

    C.append({"id":"804","slug":"area","block":16,"block_slug":"conversion",
        "inputs":[ni("valor_m2","",1,0)],
        "formula":"var m2=parseFloat(inputs.valor_m2)||0;return{ft2:+(m2*10.7639).toFixed(6),km2:+(m2/1e6).toFixed(8),ha:+(m2/10000).toFixed(6),acre:+(m2/4046.86).toFixed(6),in2:+(m2*1550).toFixed(4)};",
        "outputs":[ou("ft2","ft\u00b2",True),ou("km2","km\u00b2"),ou("ha","ha"),ou("acre","acre"),ou("in2","in\u00b2")],"related":["800","803","801"]})

    C.append({"id":"805","slug":"velocidad-unidades","block":16,"block_slug":"conversion",
        "inputs":[ni("valor_kmh","",100,0)],
        "formula":"var kmh=parseFloat(inputs.valor_kmh)||0;return{ms:+(kmh/3.6).toFixed(4),mph:+(kmh/1.60934).toFixed(4),nudos:+(kmh/1.852).toFixed(4)};",
        "outputs":[ou("ms","m/s",True),ou("mph","mph"),ou("nudos","kn")],"related":["800","801","802"]})

    C.append({"id":"806","slug":"datos-digitales","block":16,"block_slug":"conversion",
        "inputs":[ni("valor_mb","",1,0)],
        "formula":"var mb=parseFloat(inputs.valor_mb)||0;return{bytes:+(mb*1048576).toFixed(0),kb:+(mb*1024).toFixed(2),gb:+(mb/1024).toFixed(6),tb:+(mb/1048576).toFixed(8)};",
        "outputs":[ou("bytes","bytes",True),ou("kb","KB"),ou("gb","GB"),ou("tb","TB")],"related":["800","801","805"]})

    C.append({"id":"807","slug":"presion-unidades","block":16,"block_slug":"conversion",
        "inputs":[ni("valor_atm","",1,0)],
        "formula":"var atm=parseFloat(inputs.valor_atm)||0;return{pa:+(atm*101325).toFixed(2),bar:+(atm*1.01325).toFixed(6),psi:+(atm*14.696).toFixed(4),mmhg:+(atm*760).toFixed(2)};",
        "outputs":[ou("pa","Pa",True),ou("bar","bar"),ou("psi","psi"),ou("mmhg","mmHg")],"related":["800","805","801"]})

    C.append({"id":"808","slug":"tiempo-unidades","block":16,"block_slug":"conversion",
        "inputs":[ni("valor_h","",1,0)],
        "formula":"var h=parseFloat(inputs.valor_h)||0;return{minutos:+(h*60).toFixed(2),segundos:+(h*3600).toFixed(2),dias:+(h/24).toFixed(6),semanas:+(h/168).toFixed(6),meses:+(h/730).toFixed(6)};",
        "outputs":[ou("minutos","min",True),ou("segundos","s"),ou("dias",""),ou("semanas",""),ou("meses","")],"related":["800","801","805"]})

    C.append({"id":"809","slug":"energia-unidades","block":16,"block_slug":"conversion",
        "inputs":[ni("valor_j","",1000,0)],
        "formula":"var j=parseFloat(inputs.valor_j)||0;return{kj:+(j/1000).toFixed(6),cal:+(j/4.184).toFixed(4),kcal:+(j/4184).toFixed(6),kwh:+(j/3600000).toFixed(8),btu:+(j/1055.06).toFixed(6)};",
        "outputs":[ou("kj","kJ",True),ou("cal","cal"),ou("kcal","kcal"),ou("kwh","kWh"),ou("btu","BTU")],"related":["800","801","805"]})

    # ── SPORTS (deportes, block 17) ──
    C.append({"id":"900","slug":"ritmo-carrera","block":17,"block_slug":"deportes",
        "inputs":[ni("distancia_km","",10,0.01),ni("tiempo_min","",50,0.1)],
        "formula":"var d=parseFloat(inputs.distancia_km)||0,t=parseFloat(inputs.tiempo_min)||0;if(!d||!t)return{error:true};var pace=t/d,speed=d*60/t;var pm=Math.floor(pace),ps=Math.round((pace-pm)*60);return{ritmo_min_km:pm+':'+(ps<10?'0':'')+ps,velocidad_kmh:+speed.toFixed(2),velocidad_mph:+(speed/1.60934).toFixed(2)};",
        "outputs":[ou("ritmo_min_km","min/km",True),ou("velocidad_kmh","km/h"),ou("velocidad_mph","mph")],"related":["901","907","908"]})

    C.append({"id":"901","slug":"calorias-ejercicio","block":17,"block_slug":"deportes",
        "inputs":[ni("peso_kg","",70,20,300),ni("duracion_min","",30,1),ni("met","",8,1,25)],
        "formula":"var p=parseFloat(inputs.peso_kg)||0,d=parseFloat(inputs.duracion_min)||0,met=parseFloat(inputs.met)||0;var cal=met*p*(d/60);return{calorias:+cal.toFixed(0),calorias_hora:+(cal/d*60).toFixed(0)};",
        "outputs":[ou("calorias","kcal",True),ou("calorias_hora","kcal/h")],"related":["900","401","905"]})

    C.append({"id":"902","slug":"frecuencia-cardiaca-max","block":17,"block_slug":"deportes",
        "inputs":[ni("edad","",30,1,100)],
        "formula":"var age=parseFloat(inputs.edad)||0;if(!age)return{error:true};return{fc_max_tanaka:+(208-.7*age).toFixed(0),fc_max_haskell:+(220-age).toFixed(0),fc_max_arena:+(205.8-.685*age).toFixed(0)};",
        "outputs":[ou("fc_max_tanaka","bpm",True),ou("fc_max_haskell","bpm"),ou("fc_max_arena","bpm")],"related":["903","904","901"]})

    C.append({"id":"903","slug":"zonas-cardiacas","block":17,"block_slug":"deportes",
        "inputs":[ni("edad","",30,1,100),ni("fc_reposo","",60,30,100)],
        "formula":"var age=parseFloat(inputs.edad)||0,rhr=parseFloat(inputs.fc_reposo)||0;if(!age)return{error:true};var mhr=220-age;var r1=Math.round((mhr-rhr)*.5+rhr),r2=Math.round((mhr-rhr)*.6+rhr),r3=Math.round((mhr-rhr)*.7+rhr),r4=Math.round((mhr-rhr)*.8+rhr),r5=Math.round((mhr-rhr)*.9+rhr);return{zona1:r1+'-'+r2,zona2:r2+'-'+r3,zona3:r3+'-'+r4,zona4:r4+'-'+r5,zona5:r5+'-'+mhr};",
        "outputs":[ou("zona1","",True),ou("zona2",""),ou("zona3",""),ou("zona4",""),ou("zona5","")],"related":["902","904","901"]})

    C.append({"id":"904","slug":"vo2-max","block":17,"block_slug":"deportes",
        "inputs":[ni("edad","",30,10,80),ni("fc_reposo","",60,30,100)],
        "formula":"var age=parseFloat(inputs.edad)||0,rhr=parseFloat(inputs.fc_reposo)||0;if(!age)return{error:true};var mhr=220-age;return{vo2_max:+(15.3*(mhr/rhr)).toFixed(1),fc_max:+mhr.toFixed(0)};",
        "outputs":[ou("vo2_max","ml/kg/min",True),ou("fc_max","bpm")],"related":["902","903","901"]})

    C.append({"id":"905","slug":"pasos-calorias","block":17,"block_slug":"deportes",
        "inputs":[ni("pasos","",10000,100),ni("peso_kg","",70,20,300)],
        "formula":"var s=parseFloat(inputs.pasos)||0,p=parseFloat(inputs.peso_kg)||0;return{calorias:+(s*.04*p).toFixed(0),distancia_km:+(s*.000762).toFixed(2)};",
        "outputs":[ou("calorias","kcal",True),ou("distancia_km","km")],"related":["900","901","401"]})

    C.append({"id":"906","slug":"ritmo-natacion","block":17,"block_slug":"deportes",
        "inputs":[ni("distancia_m","",1500,1),ni("tiempo_min","",30,0.1)],
        "formula":"var d=parseFloat(inputs.distancia_m)||0,t=parseFloat(inputs.tiempo_min)||0;if(!d||!t)return{error:true};var p=t/d*100;var pm=Math.floor(p),ps=Math.round((p-pm)*60);return{ritmo_100m:pm+':'+(ps<10?'0':'')+ps+' /100m',velocidad_ms:+(d/t/60).toFixed(3)};",
        "outputs":[ou("ritmo_100m","/100m",True),ou("velocidad_ms","m/s")],"related":["900","907","901"]})

    C.append({"id":"907","slug":"ritmo-ciclismo","block":17,"block_slug":"deportes",
        "inputs":[ni("distancia_km","",40,0.1),ni("tiempo_min","",90,0.1)],
        "formula":"var d=parseFloat(inputs.distancia_km)||0,t=parseFloat(inputs.tiempo_min)||0;if(!d||!t)return{error:true};var s=d/(t/60);return{velocidad_kmh:+s.toFixed(2),velocidad_mph:+(s/1.60934).toFixed(2)};",
        "outputs":[ou("velocidad_kmh","km/h",True),ou("velocidad_mph","mph")],"related":["900","906","901"]})

    C.append({"id":"908","slug":"imc-deportista","block":17,"block_slug":"deportes",
        "inputs":[ni("peso_kg","",75,20,300),ni("altura_cm","",180,50,250)],
        "formula":"var p=parseFloat(inputs.peso_kg)||0,h=parseFloat(inputs.altura_cm)||0;if(!p||!h)return{error:true};var hm=h/100,bmi=p/(hm*hm);var cat=bmi<18.5?'Bajo':bmi<25?'Normal':bmi<30?'Sobrepeso':'Obesidad';return{imc:+bmi.toFixed(1),categoria:cat,peso_min:+(18.5*hm*hm).toFixed(1),peso_max:+(24.9*hm*hm).toFixed(1)};",
        "outputs":[ou("imc","kg/m\u00b2",True),ou("categoria",""),ou("peso_min","kg"),ou("peso_max","kg")],"related":["400","901","401"]})

    C.append({"id":"909","slug":"tiempo-pista","block":17,"block_slug":"deportes",
        "inputs":[ni("distancia_5k","",25,5,60),ni("distancia_objetivo","",10,0.1,42.2)],
        "formula":"var t5k=parseFloat(inputs.distancia_5k)||0,d=parseFloat(inputs.distancia_objetivo)||0;if(!t5k||!d)return{error:true};var pred=t5k*Math.pow(d/5,1.06);var pm=Math.floor(pred),ps=Math.round((pred-pm)*60);return{tiempo_estimado:pm+':'+(ps<10?'0':'')+ps,ritmo_min_km:+(pred/d).toFixed(2)};",
        "outputs":[ou("tiempo_estimado","",True),ou("ritmo_min_km","min/km")],"related":["900","907","906"]})

    # ── MORE MATH (matematicas, block 10) ──
    C.append({"id":"210","slug":"area-circulo","block":10,"block_slug":"matematicas",
        "inputs":[ni("radio","",5,0)],
        "formula":"var r=parseFloat(inputs.radio)||0;if(!r)return{error:true};return{area:+(Math.PI*r*r).toFixed(4),circunferencia:+(2*Math.PI*r).toFixed(4),diametro:+(2*r).toFixed(4)};",
        "outputs":[ou("area","u\u00b2",True),ou("circunferencia","u"),ou("diametro","u")],"related":["202","211","212"]})

    C.append({"id":"211","slug":"area-triangulo","block":10,"block_slug":"matematicas",
        "inputs":[ni("base","",10,0),ni("altura","",6,0)],
        "formula":"var b=parseFloat(inputs.base)||0,h=parseFloat(inputs.altura)||0;if(!b||!h)return{error:true};return{area:+(b*h/2).toFixed(4)};",
        "outputs":[ou("area","u\u00b2",True)],"related":["210","202","203"]})

    C.append({"id":"212","slug":"volumen-esfera","block":10,"block_slug":"matematicas",
        "inputs":[ni("radio","",5,0)],
        "formula":"var r=parseFloat(inputs.radio)||0;if(!r)return{error:true};return{volumen:+(4/3*Math.PI*Math.pow(r,3)).toFixed(4),superficie:+(4*Math.PI*r*r).toFixed(4)};",
        "outputs":[ou("volumen","u\u00b3",True),ou("superficie","u\u00b2")],"related":["210","213","202"]})

    C.append({"id":"213","slug":"volumen-cilindro","block":10,"block_slug":"matematicas",
        "inputs":[ni("radio","",5,0),ni("altura","",10,0)],
        "formula":"var r=parseFloat(inputs.radio)||0,h=parseFloat(inputs.altura)||0;if(!r||!h)return{error:true};return{volumen:+(Math.PI*r*r*h).toFixed(4),area_lateral:+(2*Math.PI*r*h).toFixed(4)};",
        "outputs":[ou("volumen","u\u00b3",True),ou("area_lateral","u\u00b2")],"related":["210","212","202"]})

    C.append({"id":"214","slug":"potencias","block":10,"block_slug":"matematicas",
        "inputs":[ni("base","",2),ni("exponente","",10)],
        "formula":"var b=parseFloat(inputs.base)||0,e=parseFloat(inputs.exponente)||0;return{resultado:+Math.pow(b,e).toFixed(8)};",
        "outputs":[ou("resultado","",True)],"related":["215","216","217"]})

    C.append({"id":"215","slug":"raiz","block":10,"block_slug":"matematicas",
        "inputs":[ni("numero","",16,0),ni("indice","",2,0.001)],
        "formula":"var n=parseFloat(inputs.numero)||0,i=parseFloat(inputs.indice)||2;if(n<0&&i%2===0)return{error:true};return{resultado:+Math.pow(n,1/i).toFixed(8)};",
        "outputs":[ou("resultado","",True)],"related":["214","216","200"]})

    C.append({"id":"216","slug":"logaritmo","block":10,"block_slug":"matematicas",
        "inputs":[ni("numero","",100,0.001),ni("base_log","",10,0.001)],
        "formula":"var n=parseFloat(inputs.numero)||0,b=parseFloat(inputs.base_log)||10;if(n<=0||b<=0||b===1)return{error:true};return{resultado:+(Math.log(n)/Math.log(b)).toFixed(8),log_natural:+Math.log(n).toFixed(8)};",
        "outputs":[ou("resultado","",True),ou("log_natural","")],"related":["214","215","217"]})

    C.append({"id":"217","slug":"factorial","block":10,"block_slug":"matematicas",
        "inputs":[ni("n","",10,0,170)],
        "formula":"var n=parseInt(inputs.n)||0;if(n<0||n>170)return{error:true};var f=1;for(var i=2;i<=n;i++)f*=i;return{resultado:f};",
        "outputs":[ou("resultado","",True)],"related":["214","604","605"]})

    C.append({"id":"218","slug":"ecuacion-segundo-grado","block":10,"block_slug":"matematicas",
        "inputs":[ni("a","",1),ni("b","",5),ni("c","",6)],
        "formula":"var a=parseFloat(inputs.a)||0,b=parseFloat(inputs.b)||0,c=parseFloat(inputs.c)||0;if(!a)return{error:true};var d=b*b-4*a*c;if(d<0)return{discriminante:+d.toFixed(4),solucion:'Sin soluciones reales'};return{x1:+((-b+Math.sqrt(d))/(2*a)).toFixed(6),x2:+((-b-Math.sqrt(d))/(2*a)).toFixed(6),discriminante:+d.toFixed(4)};",
        "outputs":[ou("x1","",True),ou("x2",""),ou("discriminante","")],"related":["214","215","200"]})

    C.append({"id":"219","slug":"mcm-mcd","block":10,"block_slug":"matematicas",
        "inputs":[ni("num1","",12,1),ni("num2","",18,1)],
        "formula":"var a=parseInt(inputs.num1)||0,b=parseInt(inputs.num2)||0;if(!a||!b)return{error:true};var x=a,y=b;while(y){var t=y;y=x%y;x=t;}return{mcm:a*b/x,mcd:x};",
        "outputs":[ou("mcm","",True),ou("mcd","")],"related":["217","214","200"]})

    # ── MORE FINANCE (finanzas, block 11) ──
    C.append({"id":"310","slug":"roi","block":11,"block_slug":"finanzas",
        "inputs":[ni("inversion","",10000,1),ni("ganancia","",15000,0)],
        "formula":"var inv=parseFloat(inputs.inversion)||0,g=parseFloat(inputs.ganancia)||0;if(!inv)return{error:true};return{roi_pct:+((g-inv)/inv*100).toFixed(2),beneficio_neto:+(g-inv).toFixed(2)};",
        "outputs":[ou("roi_pct","%",True),ou("beneficio_neto","\u20ac")],"related":["300","302","307"]})

    C.append({"id":"311","slug":"ahorro-compuesto","block":11,"block_slug":"finanzas",
        "inputs":[ni("deposito_mensual","",200,0),ni("tasa_anual","",7,0,50),ni("anos","",10,1,50)],
        "formula":"var d=parseFloat(inputs.deposito_mensual)||0,r=parseFloat(inputs.tasa_anual)||0,n=parseFloat(inputs.anos)||0;if(!d||!n)return{error:true};var mr=r/100/12,nm=n*12;var total=mr?d*((Math.pow(1+mr,nm)-1)/mr)*(1+mr):d*nm;var dep=d*nm;return{total:+total.toFixed(2),intereses:+(total-dep).toFixed(2),depositado:+dep.toFixed(2)};",
        "outputs":[ou("total","\u20ac",True),ou("intereses","\u20ac"),ou("depositado","\u20ac")],"related":["302","300","314"]})

    C.append({"id":"312","slug":"inflacion","block":11,"block_slug":"finanzas",
        "inputs":[ni("valor_actual","",1000,0),ni("tasa_inflacion","",3,0,100),ni("anos","",10,1,50)],
        "formula":"var v=parseFloat(inputs.valor_actual)||0,r=parseFloat(inputs.tasa_inflacion)||0,n=parseFloat(inputs.anos)||0;return{valor_futuro:+(v*Math.pow(1+r/100,n)).toFixed(2),poder_adquisitivo:+(v/Math.pow(1+r/100,n)).toFixed(2)};",
        "outputs":[ou("valor_futuro","\u20ac",True),ou("poder_adquisitivo","\u20ac")],"related":["310","300","302"]})

    C.append({"id":"313","slug":"subida-salarial","block":11,"block_slug":"finanzas",
        "inputs":[ni("salario_actual","",2000,0),ni("porcentaje","",5,0,100)],
        "formula":"var s=parseFloat(inputs.salario_actual)||0,p=parseFloat(inputs.porcentaje)||0;var n=s*(1+p/100);return{nuevo_salario:+n.toFixed(2),incremento:+(n-s).toFixed(2),nuevo_anual:+(n*12).toFixed(2)};",
        "outputs":[ou("nuevo_salario","\u20ac/mes",True),ou("incremento","\u20ac/mes"),ou("nuevo_anual","\u20ac/a\u00f1o")],"related":["305","200","310"]})

    C.append({"id":"314","slug":"plan-jubilacion","block":11,"block_slug":"finanzas",
        "inputs":[ni("ahorro_actual","",10000,0),ni("aportacion_mensual","",300,0),ni("rentabilidad_pct","",7,0,30),ni("anos_jubilacion","",30,1,60)],
        "formula":"var a=parseFloat(inputs.ahorro_actual)||0,d=parseFloat(inputs.aportacion_mensual)||0,r=parseFloat(inputs.rentabilidad_pct)||0,n=parseFloat(inputs.anos_jubilacion)||0;var mr=r/100/12,nm=n*12;var fvA=a*Math.pow(1+mr,nm),fvD=mr?d*((Math.pow(1+mr,nm)-1)/mr):d*nm;var total=fvA+fvD;return{total_acumulado:+total.toFixed(2),aportado:+(a+d*nm).toFixed(2),rendimientos:+(total-a-d*nm).toFixed(2)};",
        "outputs":[ou("total_acumulado","\u20ac",True),ou("aportado","\u20ac"),ou("rendimientos","\u20ac")],"related":["311","302","300"]})

    C.append({"id":"315","slug":"regla-72","block":11,"block_slug":"finanzas",
        "inputs":[ni("tasa_interes","",7,0.01,50)],
        "formula":"var r=parseFloat(inputs.tasa_interes)||0;if(!r)return{error:true};return{anos_duplicar:+(72/r).toFixed(1)};",
        "outputs":[ou("anos_duplicar","a\u00f1os",True)],"related":["302","311","314"]})

    C.append({"id":"316","slug":"deposito-plazo","block":11,"block_slug":"finanzas",
        "inputs":[ni("capital","",10000,1),ni("tasa_anual","",4,0.01,30),ni("plazo_meses","",12,1,120)],
        "formula":"var c=parseFloat(inputs.capital)||0,r=parseFloat(inputs.tasa_anual)||0,m=parseFloat(inputs.plazo_meses)||0;var i=c*(r/100)*(m/12);return{intereses:+i.toFixed(2),total:+(c+i).toFixed(2)};",
        "outputs":[ou("intereses","\u20ac",True),ou("total","\u20ac")],"related":["302","303","300"]})

    C.append({"id":"317","slug":"retorno-acciones","block":11,"block_slug":"finanzas",
        "inputs":[ni("precio_compra","",50,0.01),ni("precio_venta","",65,0.01),ni("dividendos","",2,0)],
        "formula":"var pc=parseFloat(inputs.precio_compra)||0,pv=parseFloat(inputs.precio_venta)||0,div=parseFloat(inputs.dividendos)||0;var g=pv-pc+div;return{retorno_pct:+(g/pc*100).toFixed(2),ganancia:+g.toFixed(2),ganancia_pct:+((pv-pc)/pc*100).toFixed(2)};",
        "outputs":[ou("retorno_pct","%",True),ou("ganancia","\u20ac"),ou("ganancia_pct","%")],"related":["310","302","300"]})

    C.append({"id":"318","slug":"ratio-deuda","block":11,"block_slug":"finanzas",
        "inputs":[ni("deuda_mensual","",800,0),ni("ingresos_mensuales","",2500,1)],
        "formula":"var d=parseFloat(inputs.deuda_mensual)||0,i=parseFloat(inputs.ingresos_mensuales)||0;if(!i)return{error:true};var r=d/i*100;var ev=r<=15?'Excelente':r<=25?'Bueno':r<=35?'Aceptable':r<=45?'Preocupante':'Peligroso';return{ratio:+r.toFixed(1),evaluacion:ev};",
        "outputs":[ou("ratio","%",True),ou("evaluacion","")],"related":["300","301","305"]})

    C.append({"id":"319","slug":"punto-equilibrio-unidades","block":11,"block_slug":"finanzas",
        "inputs":[ni("costos_fijos","",5000,0),ni("precio_unitario","",50,0.01),ni("costo_variable","",30,0)],
        "formula":"var cf=parseFloat(inputs.costos_fijos)||0,p=parseFloat(inputs.precio_unitario)||0,cv=parseFloat(inputs.costo_variable)||0;var m=p-cv;if(m<=0)return{error:true};var u=Math.ceil(cf/m);return{unidades:u,facturacion:+(u*p).toFixed(2),margen_contribucion:+m.toFixed(2)};",
        "outputs":[ou("unidades","uds",True),ou("facturacion","\u20ac"),ou("margen_contribucion","\u20ac/ud")],"related":["307","310","300"]})

    # ── MORE HEALTH (salud, block 12) ──
    C.append({"id":"410","slug":"metabolismo-basal","block":12,"block_slug":"salud",
        "inputs":[ni("peso_kg","",70,20,300),ni("altura_cm","",175,50,250),ni("edad","",30,1,120)],
        "formula":"var p=parseFloat(inputs.peso_kg)||0,h=parseFloat(inputs.altura_cm)||0,a=parseFloat(inputs.edad)||0;if(!p||!h||!a)return{error:true};var mH=10*p+6.25*h-5*a+5,mF=10*p+6.25*h-5*a-161;return{bmr_hombre:+mH.toFixed(0),bmr_mujer:+mF.toFixed(0),tdee_sedentario_h:+(mH*1.2).toFixed(0),tdee_sedentario_m:+(mF*1.2).toFixed(0),tdee_activo_h:+(mH*1.55).toFixed(0),tdee_activo_m:+(mF*1.55).toFixed(0)};",
        "outputs":[ou("bmr_hombre","kcal/d\u00eda",True),ou("bmr_mujer","kcal/d\u00eda"),ou("tdee_sedentario_h","kcal"),ou("tdee_sedentario_m","kcal"),ou("tdee_activo_h","kcal"),ou("tdee_activo_m","kcal")],"related":["401","400","403"]})

    C.append({"id":"411","slug":"frecuencia-cardiaca-max-salud","block":12,"block_slug":"salud",
        "inputs":[ni("edad","",30,1,100)],
        "formula":"var age=parseFloat(inputs.edad)||0;if(!age)return{error:true};return{fc_tanaka:+(208-.7*age).toFixed(0),fc_haskell:+(220-age),fc_arena:+(205.8-.685*age).toFixed(0),fc_gulati:+(206-.88*age).toFixed(0)};",
        "outputs":[ou("fc_tanaka","bpm",True),ou("fc_haskell","bpm"),ou("fc_arena","bpm"),ou("fc_gulati","bpm")],"related":["400","410","401"]})

    C.append({"id":"412","slug":"horas-sueno","block":12,"block_slug":"salud",
        "inputs":[ni("hora_despertar","",7,0,23)],
        "formula":"var wake=parseFloat(inputs.hora_despertar)||7;var cycle=1.5,fb=.25;function fmt(h){var hh=Math.floor(h),mm=Math.round((h-hh)*60);if(mm===60){hh++;mm=0;}return hh+':'+(mm<10?'0':'')+mm;}var beds=[];for(var i=6;i>=3;i--){var bed=wake-i*cycle-fb;if(bed<0)bed+=24;beds.push(fmt(bed)+' ('+i+' cycles = '+i*1.5+'h)');}return{cama_6:beds[0],cama_5:beds[1],cama_4:beds[2],cama_3:beds[3]};",
        "outputs":[ou("cama_6","",True),ou("cama_5",""),ou("cama_4",""),ou("cama_3","")],"related":["401","410","403"]})

    C.append({"id":"413","slug":"porcentaje-grasa","block":12,"block_slug":"salud",
        "inputs":[ni("imc","",24,10,60),ni("edad","",30,1,100)],
        "formula":"var bmi=parseFloat(inputs.imc)||0,age=parseFloat(inputs.edad)||0;if(!bmi||!age)return{error:true};return{grasa_hombre:+(1.20*bmi+.23*age-16.2).toFixed(1),grasa_mujer:+(1.20*bmi+.23*age-5.4).toFixed(1)};",
        "outputs":[ou("grasa_hombre","%",True),ou("grasa_mujer","%")],"related":["400","410","401"]})

    C.append({"id":"414","slug":"rango-peso-saludable","block":12,"block_slug":"salud",
        "inputs":[ni("altura_cm","",175,50,250)],
        "formula":"var h=parseFloat(inputs.altura_cm)||0;if(!h)return{error:true};var hm=h/100;return{peso_min:+(18.5*hm*hm).toFixed(1),peso_max:+(24.9*hm*hm).toFixed(1)};",
        "outputs":[ou("peso_min","kg",True),ou("peso_max","kg")],"related":["400","402","413"]})

    return C

def step1_add_calculators():
    data = json.load(open(CALC_FILE, encoding="utf-8"))
    existing_ids = {c["id"] for c in data["calculators"]}
    new_calcs = build_calculators()
    added = 0
    for c in new_calcs:
        if c["id"] not in existing_ids:
            data["calculators"].append(c)
            added += 1
    data["calculators"].sort(key=lambda c: int(c["id"]))
    with open(CALC_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Step 1: Added {added} calculators (total: {len(data['calculators'])})")

if __name__ == "__main__":
    step1_add_calculators()
    print("Done step 1. Run phase2_add_tools.py next.")
