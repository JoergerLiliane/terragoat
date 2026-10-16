import base64,io,html,os
from PIL import Image
D='/home/user/terragoat/icyber/systeme/'
B=D+'blocks/'
SZ=Image.open(D+'wealth-roadmap-laptop.webp').size
def uri(p,size,q=82):
    im=Image.open(D+p);im=im.resize(size);b=io.BytesIO();im.save(b,'WEBP',quality=q)
    return 'data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
names=sorted(n for n in os.listdir(B) if n.endswith('.html'))
blocks={n:open(B+n).read() for n in names}
gap='\n<div style="height:48px"></div>\n'
btn='''<div style="text-align:center;margin:14px 0 0"><a href="https://www.cybercnslt.com/4dd2503b" style="display:inline-block;background:#8E1F45;color:#fff;font:800 15px/1 'Avenir Next','Segoe UI',Arial,sans-serif;padding:14px 26px;border-radius:12px;text-decoration:none;box-shadow:0 8px 18px rgba(142,31,69,.28)">Get the bundle</a></div>'''
def full(photos):
    b=dict(blocks)
    if photos:
        b['02-hero-portrait.html']=b['02-hero-portrait.html'].replace('PASTE-YOUR-PHOTO-URL-HERE',uri('liliane-portrait.png',(380,380)))
        b['03-bundle-card.html']=b['03-bundle-card.html'].replace('PASTE-ROADMAP-IMAGE-URL',uri('wealth-roadmap-laptop.webp',(900,int(900*SZ[1]/SZ[0])),80)).replace('PASTE-ROADMAP-ONLY-IMAGE-URL',uri('bundle-images/product-wealth-roadmap.png',(760,468),78)).replace('PASTE-TRACKER-IMAGE-URL',uri('bundle-images/product-trust-tracker-pro.png',(760,468),78))
        b['04-free-trust-sheet-card.html']=b['04-free-trust-sheet-card.html'].replace('PASTE-TRUST-IMAGE-URL',uri('trust-sheet-laptop.webp',(900,554),80))
        b['05-about-liliane-card.html']=b['05-about-liliane-card.html'].replace('PASTE-JOURNEY-IMAGE-URL',uri('liliane-journey.webp',(1200,675),80))
    pad=lambda x:'<div style="padding:0 16px">\n'+x+'\n</div>'
    return ('<!-- iCyber · Wealth shop · whole page in ONE systeme.io "Custom HTML/CSS/JS" element -->\n'+b['01-top-buttons.html']+pad(b['02-hero-portrait.html']+gap+b['03-bundle-card.html']+gap+b['04-free-trust-sheet-card.html']+gap+gap+b['05-about-liliane-card.html']+gap+gap+b['06-three-road-cards.html'])+'\n<div style="height:60px"></div>\n')
fa=full(True); fb=full(False)
open(D+'wealth-shop-FULL-with-photos.html','w').write(fa)
open(D+'wealth-shop-FULL-photo-links.html','w').write(fb)
print(len(fa),len(fb))
items=[('all-photos','Whole page · photos included','Paste once and you\'re done: your portrait, both laptop images and your journey photo are built into the code.',fa,True),
       ('all-links','Whole page · photo links','Smaller code. Replace PASTE-YOUR-PHOTO-URL-HERE, PASTE-ROADMAP-IMAGE-URL, PASTE-ROADMAP-ONLY-IMAGE-URL, PASTE-TRACKER-IMAGE-URL, PASTE-TRUST-IMAGE-URL and PASTE-JOURNEY-IMAGE-URL with your uploaded image links.',fb,False)]
labels={'01-top-buttons.html':'Top buttons','02-hero-portrait.html':'Hero with portrait','03-bundle-card.html':'Bundle card (no button)','04-free-trust-sheet-card.html':'TRUST Sheet card','05-about-liliane-card.html':"Hey, I'm Liliane card",'06-three-road-cards.html':'Roads + road cards'}
for n in names: items.append((n[:2],n[:2]+' · '+labels[n],'Single block, for pasting the page piece by piece.',blocks[n],False))
rows=''
for k,t,d,code,main in items:
    kb=len(code.encode())/1024
    rows+=f'''<section class="row{' main' if main else ''}"><div class="txt"><h2>{html.escape(t)}</h2><p>{html.escape(d)}</p><span class="size">{kb:.0f} KB</span></div>
<div class="btns"><button type="button" data-k="{k}">Copy code</button><button type="button" class="show" data-s="{k}">Show code</button></div><p class="msg" id="m-{k}"></p><textarea id="c-{k}" readonly spellcheck="false" aria-label="{html.escape(t)} code">{html.escape(code)}</textarea></section>\n'''
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Shop Code Copier</title>
<style>
:root{{--bg:#EDF3F2;--card:#fff;--line:#E3ECEB;--head:#0F4C4C;--mut:#64777a;--turq:#1A9E9E;--mag:#8E1F45;--ok:#1B4D36;}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0e1621;--card:#16202c;--line:#273543;--head:#fff;--mut:#93a6a6;--ok:#6fcf9c;}}}}
:root[data-theme="dark"]{{--bg:#0e1621;--card:#16202c;--line:#273543;--head:#fff;--mut:#93a6a6;--ok:#6fcf9c;}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--head);font:16px/1.5 "Avenir Next","Segoe UI","Helvetica Neue",Arial,sans-serif;}}
main{{max-width:760px;margin:0 auto;padding:32px 16px 60px;}}
h1{{font-size:28px;margin:0 0 6px;letter-spacing:-.5px}} .lead{{color:var(--mut);margin:0 0 24px}}
.row{{display:flex;flex-wrap:wrap;align-items:center;gap:16px;background:var(--card);border:1px solid var(--line);border-top:4px solid var(--turq);border-radius:16px;padding:16px 18px;margin:0 0 12px;}}
.row.main{{border-top-color:var(--mag);padding:20px 18px;}}
.txt{{flex:1;min-width:0}} h2{{font-size:16px;margin:0 0 2px}} .txt p{{margin:0;color:var(--mut);font-size:13.5px}} .size{{font-size:12px;color:var(--mut);font-weight:700}}
button{{flex:none;cursor:pointer;border:0;border-radius:10px;padding:12px 18px;font:800 14px/1 inherit;font-family:inherit;color:#fff;background:linear-gradient(135deg,#1A9E9E,#0F4C4C);min-width:120px}}
.main button{{background:#8E1F45}} button.done{{background:var(--ok)!important}}
textarea{{display:none;flex-basis:100%;width:100%;height:170px;font:12px/1.4 ui-monospace,Menlo,monospace;border:2px solid var(--turq);border-radius:10px;padding:10px;background:var(--bg);color:var(--head);}}
textarea.on{{display:block}}
.btns{{display:flex;flex-direction:column;gap:8px}} button.show{{background:transparent;color:var(--head);border:1.5px solid var(--line);padding:9px 14px;font-size:13px}}
.msg{{display:none;flex-basis:100%;margin:0;background:#FFF4D6;color:#5a4300;border-radius:10px;padding:10px 12px;font-size:14px;font-weight:700}} .msg.on{{display:block}}
.steps{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 20px;margin:24px 0 0;color:var(--mut);font-size:14px}} .steps b{{color:var(--head)}}
@media (max-width:480px){{.row{{flex-direction:column;align-items:stretch}} button{{width:100%}}}}
</style></head><body><main>
<h1>Your shop code</h1>
<p class="lead">Click <b>Copy code</b>. If your browser blocks copying, the code appears in a box, already selected: just press <b>Cmd + C</b> (Mac) or <b>Ctrl + C</b> (Windows). Then paste it into a systeme.io <b>Custom HTML/CSS/JS</b> element with <b>Cmd + V</b>.</p>
{rows}
<div class="steps"><b>In systeme.io:</b> add a section with background <b>Clear</b> and padding 0, drop in one <b>Custom HTML/CSS/JS</b> element, paste, save. The bundle card has its own <b>Get The Roadmap</b> buttons linking to your store: <b>cybercnslt.com/4dd2503b</b>.</div>
</main>
<script>
function ljSel(t){{t.classList.add('on');t.focus();t.select();try{{t.setSelectionRange(0,t.value.length);}}catch(e){{}}}}
function ljManual(k,b){{var t=document.getElementById('c-'+k),m=document.getElementById('m-'+k);ljSel(t);
  m.textContent='Your browser blocked automatic copying here. The code below is selected: press Cmd + C now (Ctrl + C on Windows). If it is not selected, click into the box and press Cmd + A first.';m.classList.add('on');b.textContent='Press Cmd + C';}}
function ljDone(k,b){{var m=document.getElementById('m-'+k);m.textContent='Copied ✓ Now paste it in systeme.io with Cmd + V.';m.classList.add('on');b.textContent='Copied ✓';b.classList.add('done');setTimeout(function(){{b.textContent='Copy code';b.classList.remove('done');}},2500);}}
document.querySelectorAll('button[data-k]').forEach(function(b){{
  b.addEventListener('click',function(){{
    var k=b.dataset.k,t=document.getElementById('c-'+k),ok=false;
    ljSel(t);
    try{{ok=document.execCommand('copy');}}catch(e){{ok=false;}}
    if(ok){{ljDone(k,b);return;}}
    if(navigator.clipboard&&navigator.clipboard.writeText){{navigator.clipboard.writeText(t.value).then(function(){{ljDone(k,b);}},function(){{ljManual(k,b);}});}}
    else ljManual(k,b);
  }});
}});
document.querySelectorAll('button[data-s]').forEach(function(b){{
  b.addEventListener('click',function(){{var t=document.getElementById('c-'+b.dataset.s);if(t.classList.contains('on')){{t.classList.remove('on');b.textContent='Show code';}}else{{ljSel(t);b.textContent='Hide code';}}}});
}});
</script></body></html>'''
open('shop-code-copier.html','w').write(page);print(len(page))
