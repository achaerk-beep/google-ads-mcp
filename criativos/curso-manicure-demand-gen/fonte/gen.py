import os
SIZES={'1200x628':(1200,628),'1200x1200':(1200,1200),'960x1200':(960,1200),'1080x1920':(1080,1920)}
BASE="""<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fonts.css"><style>
:root{--wine:#7B1E2E;--deep:#4A0F1C;--rose:#F4C9D2;--cream:#FFF6F3;--gold:#E0B05A}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:%(w)dpx;height:%(h)dpx;overflow:hidden}
body{font-family:Montserrat,sans-serif;position:relative;background:var(--cream);color:var(--deep)}
.serif{font-family:'Playfair Display',serif}
.blob{position:absolute;border-radius:50%%}
.pill{display:inline-block;font-weight:700;letter-spacing:.08em;text-transform:uppercase;border-radius:999px}
.ticks{list-style:none}.ticks li{display:flex;align-items:center;gap:.5em;font-weight:600}
.ticks li:before{content:"";flex:none;width:.95em;height:.95em;border-radius:50%%;background:var(--gold) url("data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%%3E%%3Cpath d='M4 8.5l2.5 2.5L12 5.5' stroke='%%234A0F1C' stroke-width='2.2' fill='none' stroke-linecap='round'/%%3E%%3C/svg%%3E") center/80%% no-repeat}
%(css)s</style></head><body>%(body)s</body></html>"""

def instrutora(w,h):
    r=w/h; s=min(w,h)/1200
    if r>1.5:
        css=f"""body{{background:linear-gradient(115deg,var(--deep),var(--wine))}}
.photo{{position:absolute;right:0;top:0;width:{h}px;height:{h}px;object-fit:cover}}
.fade{{position:absolute;right:{h-90}px;top:0;width:90px;height:{h}px;background:linear-gradient(90deg,#5f1625,rgba(95,22,37,0))}}
.txt{{position:absolute;left:64px;top:0;bottom:0;width:560px;display:flex;flex-direction:column;justify-content:center;color:#fff}}
.pill{{background:var(--gold);color:var(--deep);font-size:18px;padding:9px 20px;align-self:flex-start;margin-bottom:22px}}
h1{{font-size:58px;line-height:1.04;font-weight:800}} h1 em{{color:var(--rose)}}
.ticks{{margin-top:26px;font-size:22px}}.ticks li+li{{margin-top:10px}}
.sig{{margin-top:26px;font-size:18px;opacity:.85}}"""
    else:
        side={1.0:h*0.64,0.8:w*0.8}.get(round(r,2),w*0.86)
        bot=h*{1.0:0.05,0.8:0.06}.get(round(r,2),0.2)
        css=f"""body{{background:linear-gradient(180deg,var(--deep) 0%,var(--wine) 100%)}}
.b1{{width:{side*1.5}px;height:{side*1.5}px;left:{(w-side*1.5)/2}px;bottom:{bot-side*0.25}px;background:radial-gradient(circle,rgba(224,176,90,.28) 0%,transparent 62%)}}
.photo{{position:absolute;left:{(w-side)/2}px;bottom:{bot}px;width:{side}px;height:{side}px;object-fit:cover;border-radius:{32*s}px;border:{6*s}px solid var(--gold);box-shadow:0 {24*s}px {60*s}px rgba(0,0,0,.4)}}
.txt{{position:absolute;left:0;right:0;top:{h*(0.07 if r<0.6 else 0.05)}px;text-align:center;color:#fff;padding:0 {60*s}px}}
.pill{{background:var(--gold);color:var(--deep);font-size:{20*s if r>=0.8 else 30*s}px;padding:.5em 1.2em;margin-bottom:{20*s}px}}
h1{{font-size:{(70 if r==1 else 78 if r>=0.8 else 108)*s}px;line-height:1.04;font-weight:800}} h1 em{{color:var(--rose)}}
.ticks{{display:flex;justify-content:center;flex-wrap:wrap;gap:{8*s}px {28*s}px;margin-top:{20*s}px;font-size:{(28 if r==1 else 32 if r>=0.8 else 40)*s}px}}
.sig{{display:none}}"""
    body="""<div class="blob b1"></div><img class="photo" src="unhas.jpg"><div class="fade"></div>
<div class="txt"><span class="pill">100% online</span>
<h1>Seja uma manicure <em>profissional</em></h1>
<ul class="ticks"><li>Aulas no seu ritmo</li><li>Certificado incluso</li></ul>
<p class="sig">Com a instrutora Faby Cardoso</p></div>"""
    return css,body

def kit(w,h):
    r=w/h; s=min(w,h)/1200
    if r>1.5:
        css=f"""body{{background:var(--cream)}}
.b1{{width:520px;height:520px;left:-160px;top:-180px;background:var(--rose)}}
.b2{{width:260px;height:260px;left:420px;bottom:-150px;background:#F9DDE3}}
.card{{position:absolute;right:36px;top:50%;transform:translateY(-50%);width:640px;background:#fff;border-radius:24px;box-shadow:0 20px 50px rgba(74,15,28,.18);overflow:hidden}}
.card img{{display:block;width:100%}}
.txt{{position:absolute;left:60px;top:0;bottom:0;width:470px;display:flex;flex-direction:column;justify-content:center}}
.pill{{background:var(--wine);color:#fff;font-size:17px;padding:9px 18px;align-self:flex-start;margin-bottom:20px}}
h1{{font-size:50px;line-height:1.08;font-weight:800;color:var(--deep)}} h1 em{{color:var(--wine);font-family:'Playfair Display',serif;font-style:italic;white-space:nowrap;font-size:46px}}
p.sub{{margin-top:18px;font-size:21px;line-height:1.4;font-weight:500;color:#6b3a44}}"""
    else:
        cw={1.0:0.84,0.8:0.92}.get(round(r,2),0.96)
        css=f"""body{{background:var(--cream)}}
.b1{{width:{w*0.8}px;height:{w*0.8}px;left:{-w*0.3}px;top:{-w*0.32}px;background:var(--rose)}}
.b2{{width:{w*0.6}px;height:{w*0.6}px;right:{-w*0.25}px;bottom:{-w*0.2}px;background:#F9DDE3}}
.card{{position:absolute;left:50%;transform:translateX(-50%);bottom:{h*(0.06 if r>=0.8 else 0.2)}px;width:{w*cw}px;background:#fff;border-radius:{28*s}px;box-shadow:0 {20*s}px {50*s}px rgba(74,15,28,.18);overflow:hidden}}
.card img{{display:block;width:100%}}
.txt{{position:absolute;left:0;right:0;top:{h*(0.06 if r>=0.8 else 0.16)}px;text-align:center;padding:0 {60*s}px}}
.pill{{background:var(--wine);color:#fff;font-size:{(19 if r>=0.8 else 28)*s}px;padding:.5em 1.1em;margin-bottom:{20*s}px}}
h1{{font-size:{(64 if r==1 else 66 if r>=0.8 else 96)*s}px;line-height:1.05;font-weight:800}} h1 em{{color:var(--wine);font-family:'Playfair Display',serif;font-style:italic}}
p.sub{{margin:{16*s}px auto 0;max-width:{(820 if r>=0.8 else 1000)*s}px;font-size:{(28 if r>=0.8 else 40)*s}px;line-height:1.4;font-weight:500;color:#6b3a44}}"""
    body="""<div class="blob b1"></div><div class="blob b2"></div>
<div class="txt"><span class="pill">Bônus exclusivos</span>
<h1>Curso completo<br><em>+ materiais de apoio</em></h1>
<p class="sub">E-books, apostila, agenda e frases prontas para divulgar seus serviços.</p></div>
<div class="card"><img src="kit.jpg"></div>"""
    return css,body

def certificado(w,h):
    r=w/h; s=min(w,h)/1200
    if r>1.5:
        css=f"""body{{background:linear-gradient(120deg,var(--wine),var(--deep))}}
.b1{{width:560px;height:560px;right:60px;top:40px;background:radial-gradient(circle,rgba(224,176,90,.35),transparent 65%)}}
.cert{{position:absolute;right:56px;top:50%;width:560px;transform:translateY(-50%) rotate(3deg);border-radius:10px;box-shadow:0 24px 60px rgba(0,0,0,.45);border:8px solid #fff}}
.txt{{position:absolute;left:64px;top:0;bottom:0;width:520px;display:flex;flex-direction:column;justify-content:center;color:#fff}}
.pill{{background:rgba(255,255,255,.14);border:2px solid var(--gold);color:var(--gold);font-size:17px;padding:8px 18px;align-self:flex-start;margin-bottom:20px}}
h1{{font-size:56px;line-height:1.06;font-weight:800}} h1 em{{font-family:'Playfair Display',serif;font-style:italic;color:var(--gold)}}
.ticks{{margin-top:24px;font-size:21px}}.ticks li+li{{margin-top:10px}}"""
    else:
        cwid=w*(0.8 if r==1 else 0.88 if r>=0.8 else 0.94)
        css=f"""body{{background:linear-gradient(180deg,var(--wine),var(--deep))}}
.b1{{width:{w}px;height:{w}px;left:0;bottom:{h*0.0}px;background:radial-gradient(circle,rgba(224,176,90,.33),transparent 62%)}}
.cert{{position:absolute;left:50%;bottom:{h*(0.07 if r>=0.8 else 0.22)}px;width:{cwid}px;transform:translateX(-50%) rotate(-2.5deg);border-radius:{10*s}px;box-shadow:0 {24*s}px {60*s}px rgba(0,0,0,.45);border:{8*s}px solid #fff}}
.txt{{position:absolute;left:0;right:0;top:{h*(0.06 if r>=0.8 else 0.16)}px;text-align:center;color:#fff;padding:0 {60*s}px}}
.pill{{border:{2*s}px solid var(--gold);color:var(--gold);font-size:{(19 if r>=0.8 else 28)*s}px;padding:.5em 1.1em;margin-bottom:{20*s}px}}
h1{{font-size:{(70 if r==1 else 74 if r>=0.8 else 108)*s}px;line-height:1.05;font-weight:800}} h1 em{{font-family:'Playfair Display',serif;font-style:italic;color:var(--gold)}}
.ticks{{display:flex;justify-content:center;flex-wrap:wrap;gap:{8*s}px {28*s}px;margin-top:{22*s}px;font-size:{(28 if r==1 else 32 if r>=0.8 else 40)*s}px}}"""
    body="""<div class="blob b1"></div>
<div class="txt"><span class="pill">Certificado de conclusão</span>
<h1>Aprenda online e <em>receba seu certificado</em></h1>
<ul class="ticks"><li>Cutilagem e esmaltação</li><li>Mãos e pés</li></ul></div>
<img class="cert" src="cert.jpg">"""
    return css,body

def limpo(w,h):
    r=w/h; s=min(w,h)/1200
    ph=h*(0.92 if r>1.5 else 0.82 if r>=0.8 else 0.7)
    css=f"""body{{background:radial-gradient(ellipse at 50% 60%,#A8324A 0%,var(--wine) 45%,var(--deep) 100%)}}
.photo{{position:absolute;left:50%;transform:translateX(-50%);bottom:0;height:{ph}px}}
.b1{{width:{min(w,h)*0.18}px;height:{min(w,h)*0.18}px;left:{w*0.08}px;top:{h*0.12}px;background:var(--rose);opacity:.5}}
.b2{{width:{min(w,h)*0.1}px;height:{min(w,h)*0.1}px;right:{w*0.1}px;top:{h*0.22}px;background:var(--gold);opacity:.55}}
.b3{{width:{min(w,h)*0.26}px;height:{min(w,h)*0.26}px;right:{-min(w,h)*0.06}px;bottom:{h*0.04}px;border:{6*s}px solid var(--rose);opacity:.35}}
.b4{{width:{min(w,h)*0.06}px;height:{min(w,h)*0.06}px;left:{w*0.16}px;bottom:{h*0.24}px;background:var(--gold);opacity:.5}}"""
    body='<div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div><div class="blob b4"></div><img class="photo" src="faby.png">'
    return css,body

for name,fn in [('01-unhas',instrutora),('02-bonus',kit),('03-certificado',certificado),('04-limpo-sem-texto',limpo)]:
    for sz,(w,h) in SIZES.items():
        css,body=fn(w,h)
        open(f'{name}_{sz}.html','w').write(BASE%dict(w=w,h=h,css=css,body=body))

# logo
open('logo_1200x1200.html','w').write(BASE%dict(w=1200,h=1200,css="""body{background:var(--wine);display:flex;align-items:center;justify-content:center}
.ring{width:960px;height:960px;border-radius:50%;border:14px solid var(--gold);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff}
.m{font-family:'Playfair Display',serif;font-style:italic;font-weight:700;font-size:430px;line-height:1}
.n{margin-top:10px;font-weight:700;letter-spacing:.22em;font-size:64px;text-transform:uppercase;color:var(--rose)}""",
body='<div class="ring"><div class="m">FC</div><div class="n">Faby Cardoso</div></div>'))
