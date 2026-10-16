import os
OUT = '/home/user/terragoat/icyber/systeme/blocks'
os.makedirs(OUT, exist_ok=True)
JOURNEY = 'https://www.cybercnslt.com/'

# Shared design tokens, copied from the journey website (light + dark).
def base(id_, maxw):
    return f"""#{id_}{{--bg:#EDF3F2;--card:#ffffff;--cardbd:#E3ECEB;--ink:#3c4f50;--head:#0F4C4C;--mut:#64777a;--turq:#1A9E9E;--turqbr:#35B7B7;--green:#1B4D36;--mag:#8E1F45;--magdk:#5E1530;--soft:#F6F9F9;--hl:#F7E6EE;
  font-family:"Avenir Next","Segoe UI","Helvetica Neue",-apple-system,Arial,sans-serif;-webkit-font-smoothing:antialiased;
  max-width:{maxw}px;margin:0 auto;padding:0 2px;color:var(--ink);line-height:1.5;text-align:left;}}
html[data-theme="dark"] #{id_}{{--bg:#0e1621;--card:#16202c;--cardbd:#273543;--ink:#c6d5d5;--head:#ffffff;--mut:#93a6a6;--soft:#1c2836;--hl:#2a1d27;--magtxt:#E0577F;}}
#{id_} *,#{id_} *::before,#{id_} *::after{{box-sizing:border-box;margin:0;padding:0;border:0;background:none;box-shadow:none;text-shadow:none;letter-spacing:normal;text-transform:none;list-style:none;}}
#{id_} a{{text-decoration:none;}}
"""

# The .stop card exactly as on the journey site
STOP = """#{i} .stop{{background:var(--card);border:1px solid var(--cardbd);border-top:4px solid var(--turq);border-radius:18px;padding:24px 26px;box-shadow:0 8px 22px rgba(10,20,25,.08);}}
#{i} .stop-top{{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:10px;}}
#{i} .stop-ic{{font-size:28px;line-height:1;}}
#{i} .stop-badge{{display:inline-block;font:800 10.5px/1 "Avenir Next",Arial;letter-spacing:1px;text-transform:uppercase;padding:6px 12px;border-radius:20px;}}
#{i} .stop-badge.paid{{color:var(--magtxt,var(--mag));border:1.5px solid var(--magtxt,var(--mag));}}
#{i} .stop-badge.free{{color:var(--green);border:1.5px solid var(--green);}}
html[data-theme="dark"] #{i} .stop-badge.free{{color:#6fcf9c;border-color:#6fcf9c;}}
#{i} .stop-sub{{display:block;margin:0 0 6px;font:800 12px/1.3 "Avenir Next",Arial;letter-spacing:1.4px;text-transform:uppercase;color:var(--turq);}}
#{i} h3{{font:800 19px/1.24 "Avenir Next",Arial;color:var(--head);margin:0 0 7px;letter-spacing:-.3px;}}
#{i} p{{margin:0 0 14px;font-size:13.8px;color:var(--mut);line-height:1.5;font-weight:500;}}
#{i} .stop-cta{{display:table;margin:4px auto 0;text-align:center;font:800 12.5px/1 "Avenir Next",Arial;padding:11px 18px;border-radius:10px;letter-spacing:.2px;color:#fff;transition:transform .22s cubic-bezier(.2,.75,.25,1),box-shadow .22s ease,filter .15s;}}
#{i} .stop-cta:hover{{transform:translateY(-3px) scale(1.04);}}
#{i} .stop-cta.free{{background:linear-gradient(135deg,#245F46,#0F3324);box-shadow:0 8px 18px rgba(27,77,54,.28);}}
@media (max-width:420px){{#{i} .stop{{padding:20px 18px;}}#{i} h3{{font-size:18px;}}}}
"""

import re as _re
def block(id_, maxw, css, html, script='', note=''):
    # systeme.io's mobile view ignores width media queries, so size everything by the block's own width
    css = _re.sub(r'@media \(max-width:(\d+)px\)', r'@container (max-width:\1px)', css)
    css = css.replace('{#'+id_+'{padding-top:32px;}', '{')
    css = '#'+id_+'{container-type:inline-size;width:100%;box-sizing:border-box;}\n' + css
    s = f'<!-- iCyber · {note} · paste into a systeme.io "Custom HTML/CSS/JS" element -->\n<div id="{id_}">\n<style>\n{base(id_, maxw)}{css}</style>\n{html}\n</div>\n'
    if script:
        s += f'<script>\n{script}\n</script>\n'
    return s

files = {}
KART = open('/tmp/claude-0/-home-user-terragoat/11c993cd-3a5f-5f3f-9b94-f763b4772daf/scratchpad/kart.uri').read()

# ---------- 01 top bar: identical to the journey site ----------
i = 'lj-shoptop'
css = f"""#{i} .lj-topbar{{display:flex;justify-content:space-between;align-items:center;gap:10px;max-width:900px;margin:0 auto;width:100%;padding:18px 10px 0;}}
#{i} .lj-back,#{i} .lj-amazon,#{i} .lj-free,#{i} .welcome-pill,#{i} .themebtn{{display:inline-flex;align-items:center;justify-content:center;width:152px;height:29px;padding:0 8px;border-radius:15px;
  font:800 10px/1 "Avenir Next",Arial;letter-spacing:.3px;white-space:nowrap;cursor:pointer;
  transition:transform .22s cubic-bezier(.2,.75,.25,1),box-shadow .22s ease,filter .15s;}}
#{i} .lj-back{{color:var(--head);background:var(--card);border:1.5px solid var(--cardbd);box-shadow:0 6px 16px rgba(0,0,0,.14);}}
#{i} .lj-amazon{{color:#131A22;background:linear-gradient(135deg,#FEBD69,#FF9900);border:1.5px solid #E88A00;box-shadow:0 6px 16px rgba(0,0,0,.20);}}
html[data-theme="dark"] #{i} .lj-amazon{{color:#ffffff;}}
#{i} .lj-free{{color:#fff;background:linear-gradient(135deg,#245F46,#0F3324);border:1.5px solid #0F3324;box-shadow:0 6px 16px rgba(15,51,36,.30);}}
#{i} .welcome-pill{{color:#fff;letter-spacing:1.4px;text-transform:uppercase;background:linear-gradient(135deg,#8E1F45,#5E1530);box-shadow:0 6px 16px rgba(94,21,48,.28);}}
#{i} .themebtn{{color:var(--head);background:var(--card);border:1.5px solid var(--cardbd);box-shadow:0 6px 18px rgba(0,0,0,.18);}}
#{i} .themebtn .tb-ic{{margin-right:5px;line-height:1;}}
#{i} .lj-back:hover,#{i} .lj-amazon:hover,#{i} .lj-free:hover,#{i} .welcome-pill:hover,#{i} .themebtn:hover{{transform:translateY(-3px) scale(1.04);filter:brightness(1.05);}}
#{i} .lbl-short{{display:none;}}
@media (max-width:640px){{#{i} .lj-topbar{{gap:6px;padding:14px 0 0;}}
  #{i} .lj-back,#{i} .lj-amazon,#{i} .lj-free,#{i} .welcome-pill,#{i} .themebtn{{width:auto;flex:1 1 0;min-width:0;padding:0 4px;font-size:10px;}}
  #{i} .lbl-full{{display:none;}}#{i} .lbl-short{{display:inline;}}}}
@container (max-width:460px){{
 #{i} .lj-topbar{{gap:4px;}}
 #{i} .lj-back,#{i} .lj-amazon,#{i} .lj-free,#{i} .welcome-pill,#{i} .themebtn{{padding:0 3px;font-size:9px;letter-spacing:0;height:27px;}}
 #{i} .welcome-pill{{letter-spacing:.4px;}} #{i} .themebtn .tb-ic{{margin-right:2px;}}
}}
"""
html = f"""<div class="lj-topbar">
  <a class="lj-back" href="https://www.cybercnslt.com/"><span class="lbl-full">Main Page</span><span class="lbl-short">Home</span></a>
  <a class="lj-amazon" href="https://amzn.to/3QzHB0n" target="_blank" rel="noopener nofollow">&#128722;&nbsp;<span class="lbl-full">My Amazon Store</span><span class="lbl-short">Amazon</span></a>
  <a class="lj-free" href="{JOURNEY}#tools"><span class="lbl-full">Tools and Resources</span><span class="lbl-short">Tools</span></a>
  <a class="welcome-pill" href="{JOURNEY}#journeys"><span class="lbl-full">All journeys</span><span class="lbl-short">Journeys</span></a>
  <button class="themebtn" type="button" onclick="toggleTheme()" title="Dark Mode / White Mode" aria-label="Switch dark or white mode"><span class="tb-ic">&#127769;</span><span class="lbl-full">Dark Mode</span><span class="lbl-short">Dark</span></button>
</div>"""
script = """/* Light / dark mode switch. The page always opens in white mode; dark mode only lasts for the current visit */
(function(){
  var r=document.documentElement;
  r.removeAttribute('data-theme');
  try{ localStorage.removeItem('lj-theme'); }catch(e){}
  if(!document.getElementById('lj-pagebg')){
    var s=document.createElement('style');s.id='lj-pagebg';
    s.textContent='html,body{background:#EDF3F2 !important;transition:background .3s ease;}html[data-theme="dark"],html[data-theme="dark"] body{background:#0e1621 !important;}';
    document.head.appendChild(s);
  }
  window.ljLabel=function(){
    var dark=r.getAttribute('data-theme')==='dark';
    document.querySelectorAll('.themebtn').forEach(function(b){
      b.innerHTML=dark?'<span class="tb-ic">&#9728;&#65039;</span><span class="lbl-full">White Mode</span><span class="lbl-short">White</span>'
                      :'<span class="tb-ic">&#127769;</span><span class="lbl-full">Dark Mode</span><span class="lbl-short">Dark</span>';
    });
  };
  window.toggleTheme=function(){
    if(r.getAttribute('data-theme')==='dark'){r.removeAttribute('data-theme');}
    else{r.setAttribute('data-theme','dark');}
    window.ljLabel();
  };
  window.ljLabel();
  document.addEventListener('DOMContentLoaded',window.ljLabel);
  window.addEventListener('load',window.ljLabel);
})();"""
files['01-top-buttons.html'] = block(i, 900, css, html, script, 'Top buttons (Main Page · Amazon · Tools · All journeys · Dark/White mode) · put this FIRST on the page')

# ---------- 02 hero with portrait (same as the journey hero) ----------
i = 'lj-hero'
css = f"""#{i}{{text-align:center;padding:44px 16px 10px;}}
#{i} .ey{{display:block;font:800 13px/1 "Avenir Next",Arial;letter-spacing:3px;text-transform:uppercase;color:var(--turq);margin-bottom:18px;}}
html[data-theme="dark"] #{i} .ey{{color:#35B7B7;}}
#{i} h1{{font:800 52px/1.02 "Avenir Next",Arial;letter-spacing:-1px;color:var(--head);margin:0;}}
#{i} h1 .acc{{color:var(--acc,#E6117F);}}
html[data-theme="dark"] #{i} h1 .acc{{color:#ff62ad;}}
#{i} .sub{{max-width:580px;margin:12px auto 0;color:var(--mut);font-size:16.5px;line-height:1.5;font-weight:500;}}
html[data-theme="dark"] #{i} .sub{{color:#cfe0df;}}
#{i} .sub b{{color:var(--head);font-weight:800;}}
#{i} .eternity{{display:flex;justify-content:center;align-items:center;margin:22px 0 0;perspective:1100px;}}
#{i} .ering{{display:block;border-radius:50%;padding:7px;background:linear-gradient(160deg,#8E1F45 0%,#5E1530 45%,#1A9E9E 100%);box-shadow:0 18px 44px rgba(0,0,0,.35);
  animation:ljhSpin 1.15s cubic-bezier(.3,.7,.3,1) both,ljhFloat 5.5s ease-in-out 1.3s infinite;}}
#{i} .ecirc{{display:block;width:190px;height:190px;object-fit:cover;border-radius:50%;border:6px solid #fff;background:#0c1119;}}
#{i} .by{{margin-top:16px;font:700 14px/1.5 "Avenir Next",Arial;color:var(--turq);}}
html[data-theme="dark"] #{i} .by{{color:#9fd0d0;}}
#{i} .by-n{{display:block;font-size:17px;font-weight:800;}}
#{i} .by-t{{display:block;font-size:14px;font-weight:600;margin-top:2px;}}
#{i} h1,#{i} .sub,#{i} .eternity,#{i} .by{{animation:ljhUp .85s both;}}
#{i} .sub{{animation-delay:.12s;}}#{i} .eternity{{animation-delay:.24s;}}#{i} .by{{animation-delay:.38s;}}
@keyframes ljhSpin{{from{{transform:rotateY(0deg);}}to{{transform:rotateY(360deg);}}}}
@keyframes ljhFloat{{0%,100%{{transform:translateY(0);}}50%{{transform:translateY(-9px);}}}}
@keyframes ljhUp{{from{{opacity:0;transform:translateY(26px);}}to{{opacity:1;transform:none;}}}}
@media (prefers-reduced-motion:reduce){{#{i} *{{animation:none !important;}}}}
@media (max-width:600px){{#{i}{{padding-top:32px;}}#{i} h1{{font-size:27px;letter-spacing:-.4px;}}#{i} .sub{{font-size:13.5px;}}#{i} .ey{{font-size:11px;margin-bottom:12px;}}#{i} .ecirc{{width:160px;height:160px;}}}}
"""
html = """<span class="ey">The Wealth Roadmap</span>
<h1>Build your <span class="acc">wealth</span><br>without quitting <span style="white-space:nowrap">your <span class="acc">9&#8211;5</span>.</span></h1>
<p class="sub"><b>Know your numbers. Leverage your career. Reclaim your time.</b> Financial literacy for people in demanding jobs.</p>
<div class="eternity"><span class="ering"><img class="ecirc" src="PASTE-YOUR-PHOTO-URL-HERE" alt="Liliane" width="190" height="190"></span></div>
<p class="by"><span class="by-n">Liliane</span><span class="by-t">cybersecurity consultant, solo-preneur, creator</span></p>"""
files['02-hero-portrait.html'] = block(i, 900, css, html, note='Hero with your portrait · put this right under the top buttons')

# ---------- 02 bundle card (no button: added in systeme.io) ----------
i = 'lj-bundle'
css = STOP.format(i=i) + f"""#{i} .stop{{border-top-color:var(--mag);}}
#{i} .mock{{margin:0 0 18px;animation:ljbFloat 5.5s ease-in-out infinite;}}
#{i} .mock img{{display:block;width:100%;height:auto;border-radius:14px;box-shadow:0 16px 34px rgba(10,20,25,.16);}}
@keyframes ljbFloat{{0%,100%{{transform:translateY(0);}}50%{{transform:translateY(-8px);}}}}
@media (prefers-reduced-motion:reduce){{#{i} .mock{{animation:none;}}}}
#{i} .steps{{margin:0 0 20px;padding:16px 18px;background:var(--soft);border:1px solid var(--cardbd);border-radius:14px;}}
#{i} .steps .sh{{display:block;font:800 11.5px/1.2 "Avenir Next",Arial;letter-spacing:1.6px;text-transform:uppercase;color:var(--turq);margin:0 0 12px;}}
#{i} .steps ol{{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(4,auto);grid-auto-flow:column;gap:10px 18px;align-content:start;}}
#{i} .steps li{{display:flex;align-items:flex-start;gap:10px;font:700 14px/1.35 "Avenir Next",Arial;color:var(--head);padding:0;border:0;justify-content:flex-start;}}
#{i} .steps li::before{{content:none !important;}}
#{i} .steps li span:first-child::before{{content:none !important;margin:0 !important;}}
#{i} .steps li span:last-child{{white-space:normal !important;color:var(--head) !important;font-weight:700 !important;}}
#{i} .steps li .nb{{color:#fff !important;font-weight:800 !important;}}
#{i} .steps li small{{color:var(--mut) !important;font-weight:600 !important;}}
#{i} .steps .nb{{flex:none;width:24px;height:24px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font:800 12px/1 "Avenir Next",Arial;color:#fff;background:var(--c,#1A9E9E);margin-top:-2px;}}
#{i} .steps li small{{display:block;font:600 12.5px/1.35 "Avenir Next",Arial;color:var(--mut);margin-top:2px;}}
@media (max-width:560px){{#{i} .steps ol{{grid-template-columns:1fr;grid-template-rows:none;grid-auto-flow:row;}}}}
#{i} .cmp{{margin:0 0 20px;padding:16px 18px;background:var(--soft);border:1px solid var(--cardbd);border-radius:14px;}}
#{i} .cmp .sh{{display:block;font:800 11.5px/1.2 "Avenir Next",Arial;letter-spacing:1.6px;text-transform:uppercase;color:var(--turq);margin:0 0 10px;}}
#{i} .cmp table{{width:100%;border-collapse:collapse;}}
#{i} .cmp th{{font:800 11px/1.2 "Avenir Next",Arial;letter-spacing:1px;text-transform:uppercase;color:var(--mut);text-align:center;padding:0 0 8px;width:64px;}}
#{i} .cmp th:first-child{{width:auto;}}
#{i} .cmp td{{font:700 14px/1.35 "Avenir Next",Arial;color:var(--head);padding:7px 0;border-top:1px dashed var(--cardbd);}}
#{i} .cmp td+td{{text-align:center;color:var(--mut);font-weight:800;}}
#{i} .cmp td:last-child{{color:var(--turq);}}
#{i} .cmp .cmpn{{margin:10px 0 0;font-size:13px;color:var(--mut);}}
#{i} .prod{{margin:0 0 18px;padding:18px;border:1px solid var(--cardbd);border-radius:16px;background:var(--card);}}
#{i} .ph{{display:flex;align-items:center;gap:12px;margin:0 0 14px;}}
#{i} .pn{{flex:none;width:34px;height:34px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;background:var(--c,#1A9E9E);color:#fff;font:800 16px/1 "Avenir Next",Arial;}}
#{i} .pt{{flex:1;min-width:0;}}
#{i} .pk{{display:block;font:800 11px/1.2 "Avenir Next",Arial;letter-spacing:1.4px;text-transform:uppercase;color:var(--turq);}}
#{i} h4{{margin:2px 0 0;font:800 20px/1.2 "Avenir Next",Arial;color:var(--head);letter-spacing:-.3px;}}
#{i} .pv{{flex:none;font:800 13px/1 "Avenir Next",Arial;color:var(--mut);}}
#{i} .pimg{{display:block;width:78%;max-width:100%;height:auto;margin:0 auto 16px;border-radius:12px;box-shadow:0 10px 24px rgba(10,20,25,.12);}}
#{i} .prod .steps,#{i} .prod .cmp{{margin-bottom:14px;}}
#{i} .prod .cmp{{margin-bottom:0;}}
#{i} .pfmt{{margin:0;font-size:13.5px;color:var(--mut);}}
@media (max-width:560px){{#{i} .pimg{{width:100%;}}#{i} .prod{{padding:14px;}}#{i} h4{{font-size:18px;}}}}
#{i} .price{{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;margin:0 0 14px;}}
#{i} .now{{font:800 30px/1 "Avenir Next",Arial;color:#E6117F !important;-webkit-text-fill-color:#E6117F !important;letter-spacing:-.5px;}}
#{i} .foot b{{color:#E6117F !important;-webkit-text-fill-color:#E6117F !important;}}
html[data-theme="dark"] #{i} .now,html[data-theme="dark"] #{i} .foot b{{color:#ff62ad !important;-webkit-text-fill-color:#ff62ad !important;}}
#{i} .was{{font:600 16px/1 "Avenir Next",Arial;color:var(--mut);text-decoration:line-through;}}
#{i} .note{{font:600 10.5px/1.2 "Avenir Next",Arial;color:var(--mut) !important;-webkit-text-fill-color:var(--mut) !important;font-size:10.5px !important;font-weight:600 !important;}}
#{i} ul{{background:var(--soft);border:1px solid var(--cardbd);border-radius:12px;padding:12px 14px;}}
#{i} li{{display:flex;justify-content:space-between;gap:12px;font-size:13.5px;font-weight:600;color:var(--ink);padding:6px 0;border-bottom:1px dashed var(--cardbd);}}
#{i} li:last-child{{border-bottom:0;}}
#{i} li span:first-child::before{{content:"\\2713";color:var(--turq);font-weight:800;margin-right:8px;}}
#{i} li span:last-child{{white-space:nowrap;color:var(--mut);font-weight:700;}}
#{i} li.tot span{{color:var(--head);font-weight:800;}}
#{i} li.tot span:first-child::before{{content:"";margin:0;}}
#{i} .fine{{margin:12px 0 0;font-size:12px;color:var(--mut);text-align:center;}}
#{i}{{max-width:1000px !important;}}
#{i} .hero{{display:grid;grid-template-columns:1fr auto;gap:18px 28px;align-items:end;margin:0 0 22px;}}
#{i} .hero .stop-top{{justify-content:flex-start;gap:12px;flex-wrap:wrap;margin-bottom:6px;}}
#{i} .hero .stop-sub{{margin:0;}}
#{i} .hero h3{{font-size:24px;}}
#{i} .hero p{{margin:0;font-size:14.5px;}}
#{i} .buy{{display:flex;flex-direction:column;align-items:stretch;gap:8px;min-width:260px;}}
#{i} .buy .price{{margin:0;justify-content:flex-start;}}
#{i} .cta{{display:block;text-align:center;background:var(--mag);color:#fff;font:800 16px/1 "Avenir Next",Arial;padding:15px 22px;border-radius:12px;box-shadow:0 10px 22px rgba(142,31,69,.30);transition:transform .2s,filter .2s;}}
#{i} .cta:hover{{transform:translateY(-2px);filter:brightness(1.06);}}
#{i} .cta:focus-visible{{outline:3px solid var(--turq);outline-offset:3px;}}
#{i} .buy .fine{{font-size:12px;color:var(--mut);text-align:center;}}
#{i} .duo{{display:grid;grid-template-columns:1fr 1fr;gap:18px;}}
#{i} .duo .prod{{margin:0;display:flex;flex-direction:column;}}
#{i} .duo .pimg{{width:100%;}}
#{i} .ls{{display:flex;flex-direction:column;gap:7px;margin:0 0 12px;}}
#{i} .ls li{{display:flex;align-items:flex-start;gap:9px;font:700 13.5px/1.35 "Avenir Next",Arial;color:var(--head);padding:0;border:0;justify-content:flex-start;}}
#{i} .ls li::before,#{i} .ls li span:first-child::before{{content:none !important;margin:0 !important;}}
#{i} .ls li span:last-child{{white-space:normal !important;color:var(--head) !important;font-weight:700 !important;}}
#{i} .ls li small{{font-weight:600;color:var(--mut);}}
#{i} .ls li em{{font-style:normal;font-weight:600;color:var(--mut);}}
#{i} .ls .nb{{flex:none;width:22px;height:22px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font:800 11px/1 "Avenir Next",Arial;color:#fff !important;background:var(--c,#1A9E9E);}}
#{i} details{{margin-top:auto;border-top:1px dashed var(--cardbd);padding-top:10px;}}
#{i} summary{{cursor:pointer;font:800 13px/1.3 "Avenir Next",Arial;color:var(--turq);list-style:none;}}
#{i} summary::-webkit-details-marker{{display:none;}}
#{i} summary::before{{content:"+ ";}}
#{i} details[open] summary::before{{content:"\2013  ";}}
#{i} .more{{margin:8px 0 0;display:flex;flex-direction:column;gap:5px;}}
#{i} .more li{{display:block;font:600 13px/1.4 "Avenir Next",Arial;color:var(--mut);padding:0;border:0;}}
#{i} .more li::before,#{i} .more li span::before{{content:none !important;}}
#{i} .more b{{color:var(--head);margin-right:4px;}}
#{i} .cmpt{{width:100%;border-collapse:collapse;margin-top:8px;}}
#{i} .cmpt th{{font:800 10.5px/1.2 "Avenir Next",Arial;letter-spacing:1px;text-transform:uppercase;color:var(--mut);padding:0 0 6px;width:44px;text-align:center;}}
#{i} .cmpt th:first-child{{width:auto;}}
#{i} .cmpt td{{font:700 13px/1.35 "Avenir Next",Arial;color:var(--head);padding:5px 0;border-top:1px dashed var(--cardbd);}}
#{i} .cmpt td+td{{text-align:center;color:var(--mut);}}
#{i} .cmpt td:last-child{{color:var(--turq);}}
#{i} .foot{{display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap;margin-top:20px;padding-top:18px;border-top:1px solid var(--cardbd);}}
#{i} .foot span{{font:700 15px/1.3 "Avenir Next",Arial;color:var(--mut);}}
#{i} .foot b{{color:var(--head);font-size:18px;}}
#{i} .foot .cta{{min-width:260px;}}
@media (max-width:760px){{#{i} .hero{{grid-template-columns:1fr;}}#{i} .buy{{min-width:0;}}#{i} .duo{{grid-template-columns:1fr;}}#{i} .foot .cta{{width:100%;min-width:0;}}}}
#{i} .stop{{background:none !important;border:0 !important;box-shadow:none !important;border-radius:0 !important;padding:0 !important;}}
#{i} .stop>.mock{{max-width:780px;margin:0 auto 26px;}}
#{i} .hero{{display:flex !important;flex-direction:column;align-items:center;text-align:center;gap:16px;max-width:720px;margin:0 auto 30px;}}
#{i} .hero .stop-top{{justify-content:center !important;}}
#{i} .hero p{{max-width:600px;margin:0 auto;}}
#{i} .buy{{align-items:center !important;min-width:0 !important;width:100%;max-width:380px;}}
#{i} .buy .price{{justify-content:center !important;}}
#{i} .buy .cta{{width:100%;}}
#{i} .foot{{flex-direction:column;justify-content:center !important;text-align:center;gap:12px;}}
#{i} .foot .cta{{width:100%;max-width:380px;min-width:0 !important;}}
#{i} .ph{{flex-wrap:wrap;}}
@container (max-width:760px){{#{i} .duo{{grid-template-columns:1fr !important;}}}}
@container (max-width:520px){{
 #{i} .hero{{gap:12px;margin-bottom:22px;}}
 #{i} .hero h3{{font-size:20px;}} #{i} .hero p{{font-size:13.5px;}}
 #{i} .now{{font-size:26px;}} #{i} .was{{font-size:14px;}}
 #{i} .cta{{font-size:14px;padding:12px 14px;border-radius:10px;}}
 #{i} .buy,#{i} .foot .cta{{max-width:300px;}}
 #{i} .stop-sub{{font-size:10.5px;letter-spacing:1.1px;}} #{i} .stop-badge{{font-size:10px;padding:5px 10px;}}
 #{i} .duo{{gap:14px;}}
 #{i} .prod{{padding:12px;border-radius:14px;}} #{i} .pimg{{width:100%;margin-bottom:12px;}}
 #{i} h4{{font-size:16px;}} #{i} .pk{{font-size:10px;}} #{i} .pv{{font-size:12px;}} #{i} .pn{{width:28px;height:28px;font-size:14px;}}
 #{i} .ls{{gap:6px;}} #{i} .ls li{{font-size:12.5px;gap:8px;}} #{i} .ls li small{{font-size:11.5px;}}
 #{i} .ls .nb{{width:19px;height:19px;font-size:10px;}}
 #{i} summary{{font-size:12.5px;}} #{i} .more li,#{i} .cmpt td{{font-size:12px;}}
 #{i} .foot span{{font-size:13.5px;}} #{i} .foot b{{font-size:16px;}}
 #{i} .stop>.mock{{margin-bottom:18px;}}
}}
#{i} .look{{margin:26px 0 0;}}
#{i} .lh{{text-align:center;margin:0 0 16px;}}
#{i} .lh p{{margin:4px 0 0;font-size:13.5px;color:var(--mut);}}
#{i} .lkrow{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;}}
#{i} .lk{{margin:0;min-width:0;}}
#{i} .lk img{{display:block;width:100%;height:auto;border-radius:6px;box-shadow:0 10px 24px rgba(10,20,25,.16);transition:transform .25s ease,box-shadow .25s ease;}}
#{i} .lk:hover img{{transform:translateY(-4px);box-shadow:0 18px 36px rgba(10,20,25,.22);}}
#{i} .lk figcaption{{margin-top:10px;text-align:center;font:700 13px/1.3 "Avenir Next",Arial;color:var(--head);}}
#{i} .lk figcaption span{{display:block;font:800 10.5px/1.2 "Avenir Next",Arial;letter-spacing:1.3px;text-transform:uppercase;color:var(--c);margin-bottom:3px;}}
html[data-theme="dark"] #{i} .lk figcaption span{{color:#4CC3C3;}}
@container (max-width:700px){{
 #{i} .lkrow{{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:14px;padding:4px 2px 14px;-webkit-overflow-scrolling:touch;}}
 #{i} .lk{{flex:0 0 46%;scroll-snap-align:start;}}
 #{i} .lh h4{{font-size:16px;}} #{i} .lh p{{font-size:12.5px;}}
}}
#{i} .prod .sh{{display:block;font:800 11.5px/1.2 "Avenir Next",Arial;letter-spacing:1.6px;text-transform:uppercase;color:var(--turq);margin:0 0 12px;}}
#{i} .cta{{display:inline-block !important;width:250px !important;max-width:100% !important;min-width:0 !important;padding:14px 16px !important;font-size:15px !important;border-radius:12px !important;text-align:center;}}
#{i} .buy{{max-width:none !important;}}
@container (max-width:520px){{#{i} .cta{{width:220px !important;padding:12px 14px !important;font-size:14px !important;}}}}
"""
html = """<div class="stop">
  <div class="mock"><img src="PASTE-ROADMAP-IMAGE-URL" alt="The Wealth Roadmap on a laptop with the TRUST Tracker Pro dashboard on a tablet" width="1518" height="935"></div>
  <div class="hero">
    <div class="hl">
      <div class="stop-top"><span class="stop-sub">Paid bundle · 2 products</span><span class="stop-badge paid">Early Bird Price</span></div>
      <h3>The Wealth Roadmap + TRUST Tracker Pro</h3>
      <p>Build your wealth without quitting your 9&#8211;5: a 50+ page roadmap through 7 clear stages, plus the tracker that shows what you really keep.</p>
    </div>
    <div class="buy">
      <div class="price"><span class="now">&#8364;39</span><span class="was">&#8364;59</span><span class="note">You save &#8364;20</span></div>
      <a class="cta" href="https://www.cybercnslt.com/4dd2503b">Get The Roadmap</a>
      <span class="fine">Instant download &#183; PDF + Excel / Google Sheets</span>
    </div>
  </div>
  <div class="duo">
    <div class="prod">
      <div class="ph"><span class="pn">1</span><div class="pt"><span class="pk">PDF · 50+ pages</span><h4>The Wealth Roadmap</h4></div><span class="pv">&#8364;49</span></div>
      <img class="pimg" src="PASTE-ROADMAP-ONLY-IMAGE-URL" alt="The Wealth Roadmap on a laptop" width="3036" height="1870">
      <span class="sh">What's inside the roadmap</span>
      <ol class="ls"><li><span class="nb" style="--c:#1A9E9E">1</span><span>Money mindset: your 9–5 is your wealth engine</span></li><li><span class="nb" style="--c:#8E1F45">2</span><span>Know your salary &amp; your numbers</span></li><li><span class="nb" style="--c:#1B4D36">3</span><span>Clear your debts <em>(optional)</em></span></li><li><span class="nb" style="--c:#1A9E9E">4</span><span>Build a safety net</span></li><li><span class="nb" style="--c:#8E1F45">5</span><span>Build wealth with smart investing</span></li><li><span class="nb" style="--c:#1B4D36">6</span><span>Build multiple income streams</span></li><li><span class="nb" style="--c:#1A9E9E">7</span><span>Repeat, automate &amp; buy back time</span></li></ol>
      <details><summary>A tool in every stage</summary><ul class="more"><li><b>1</b> Your real hourly value + the 5 laws of money</li><li><b>2</b> Salary &amp; raise script, weekly win file</li><li><b>3</b> Starter buffer, debt payoff plan, bill-cutting call script</li><li><b>4</b> Emergency buffer calculator</li><li><b>5</b> Investing basics &amp; scam red-flag checklist</li><li><b>6</b> The 90-day income test</li><li><b>7</b> Automated payday plan &amp; monthly review</li></ul></details>
    </div>
    <div class="prod">
      <div class="ph"><span class="pn" style="--c:#8E1F45">2</span><div class="pt"><span class="pk">Excel &amp; Google Sheets</span><h4>TRUST Tracker Pro</h4></div><span class="pv">&#8364;39</span></div>
      <img class="pimg" src="PASTE-TRACKER-IMAGE-URL" alt="TRUST Tracker Pro dashboard on a tablet" width="3036" height="1870">
      <span class="sh">What's inside TRUST Tracker Pro</span>
      <ol class="ls"><li><span class="nb" style="--c:#1A9E9E">&#10003;</span><span>Track <small>· money in and out</small></span></li><li><span class="nb" style="--c:#8E1F45">&#10003;</span><span>Reclaim <small>· cut or renegotiate costs</small></span></li><li><span class="nb" style="--c:#1B4D36">&#10003;</span><span>Understand <small>· debt payoff order</small></span></li><li><span class="nb" style="--c:#1A9E9E">&#10003;</span><span>Save <small>· buffer &amp; emergency fund</small></span></li><li><span class="nb" style="--c:#8E1F45">&#10003;</span><span>Time <small>· your 168-hour week</small></span></li><li><span class="nb" style="--c:#1B4D36">&#10003;</span><span>Income Streams <small>· &#8364; per hour per stream</small></span></li><li><span class="nb" style="--c:#1A9E9E">&#10003;</span><span>KEEP Dashboard <small>· Freedom Level &amp; next step</small></span></li><li><span class="nb" style="--c:#8E1F45">&#10003;</span><span>Monthly Review <small>· 12 months of progress</small></span></li></ol>
      <details><summary>Free TRUST Sheet vs Pro</summary><table class="cmpt"><thead><tr><th></th><th>Free</th><th>Pro</th></tr></thead><tbody><tr><td>What you keep each month</td><td>&#10003;</td><td>&#10003;</td></tr><tr><td>Needs, wants &amp; keep rate</td><td>&#10003;</td><td>&#10003;</td></tr><tr><td>Debt payoff plan</td><td>&#8211;</td><td>&#10003;</td></tr><tr><td>Emergency fund &amp; goal pots</td><td>&#8211;</td><td>&#10003;</td></tr><tr><td>Income streams &amp; &#8364; per hour</td><td>&#8211;</td><td>&#10003;</td></tr><tr><td>168-hour week &amp; family time</td><td>&#8211;</td><td>&#10003;</td></tr><tr><td>Freedom Level 0–6</td><td>&#8211;</td><td>&#10003;</td></tr><tr><td>12-month review</td><td>&#8211;</td><td>&#10003;</td></tr><tr><td>Linked to the 7 stages</td><td>&#8211;</td><td>&#10003;</td></tr></tbody></table></details>
    </div>
  </div>
  <div class="look"><div class="lh"><span class="pk">Look inside</span><h4>The Wealth Roadmap, stage by stage</h4><p>50+ pages · every stage with deep dives, real examples, a tool and a checklist</p></div>
    <div class="lkrow">"""+open('/tmp/claude-0/-home-user-terragoat/11c993cd-3a5f-5f3f-9b94-f763b4772daf/scratchpad/look_html.txt').read()+"""</div></div>
  <div class="foot"><span>Total value <s>&#8364;88</s> &#183; today <b>&#8364;39</b></span><a class="cta" href="https://www.cybercnslt.com/4dd2503b">Get The Roadmap</a></div>
</div>"""
files['03-bundle-card.html'] = block(i, 760, css, html, note='Bundle card · add your systeme.io "Get the bundle" button directly below it')

# ---------- 03 free TRUST Sheet card ----------
i = 'lj-freecard'
css = STOP.format(i=i) + f"""#{i} .stop{{border-top-color:var(--green);}}
#{i} .steps{{margin:0 0 20px;padding:16px 18px;background:var(--soft);border:1px solid var(--cardbd);border-radius:14px;}}
#{i} .steps .sh{{display:block;font:800 11.5px/1.2 "Avenir Next",Arial;letter-spacing:1.6px;text-transform:uppercase;color:var(--turq);margin:0 0 12px;}}
#{i} .steps ol{{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(4,auto);grid-auto-flow:column;gap:10px 18px;align-content:start;}}
#{i} .steps li{{display:flex;align-items:flex-start;gap:10px;font:700 14px/1.35 "Avenir Next",Arial;color:var(--head);padding:0;border:0;justify-content:flex-start;}}
#{i} .steps li::before{{content:none !important;}}
#{i} .steps li span:first-child::before{{content:none !important;margin:0 !important;}}
#{i} .steps li span:last-child{{white-space:normal !important;color:var(--head) !important;font-weight:700 !important;}}
#{i} .steps li .nb{{color:#fff !important;font-weight:800 !important;}}
#{i} .steps li small{{color:var(--mut) !important;font-weight:600 !important;}}
#{i} .steps .nb{{flex:none;width:24px;height:24px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font:800 12px/1 "Avenir Next",Arial;color:#fff;background:var(--c,#1A9E9E);margin-top:-2px;}}
#{i} .steps li small{{display:block;font:600 12.5px/1.35 "Avenir Next",Arial;color:var(--mut);margin-top:2px;}}
@media (max-width:560px){{#{i} .steps ol{{grid-template-columns:1fr;grid-template-rows:none;grid-auto-flow:row;}}}}
#{i} .thumb{{width:84px;height:84px;border-radius:16px;background:linear-gradient(150deg,#3A9A9A,#1F5E5E);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;box-shadow:0 8px 18px rgba(15,76,76,.25);}}
#{i} .thumb b{{display:block;font:800 19px/1 "Avenir Next",Arial;letter-spacing:1.5px;}}
#{i} .thumb small{{display:block;font:800 10.5px/1.15 "Avenir Next",Arial;letter-spacing:1.2px;margin-top:5px;}}
#{i} .mock{{margin:0 0 18px;animation:ljfFloat 5.5s ease-in-out infinite;}}
#{i} .mock img{{display:block;width:100%;height:auto;border-radius:14px;box-shadow:0 16px 34px rgba(10,20,25,.16);}}
@keyframes ljfFloat{{0%,100%{{transform:translateY(0);}}50%{{transform:translateY(-8px);}}}}
@media (prefers-reduced-motion:reduce){{#{i} .mock{{animation:none;}}}}
#{i} .price{{display:flex;align-items:baseline;gap:10px;margin:0 0 14px;}}
#{i} .now{{font:800 30px/1 "Avenir Next",Arial;color:var(--head);letter-spacing:-.5px;}}
#{i} .note{{font:700 12px/1.2 "Avenir Next",Arial;color:var(--mut);}}
#{i} .stop{{background:none !important;border:0 !important;box-shadow:none !important;border-radius:0 !important;padding:0 !important;}}
@container (max-width:520px){{
 #{i} .steps{{padding:12px;}} #{i} .steps li{{font-size:12.5px !important;gap:8px;}} #{i} .steps li small{{font-size:11.5px !important;}}
 #{i} .steps .nb{{width:20px;height:20px;font-size:10px;}} #{i} .stop-cta{{font-size:13px;padding:10px 16px;}}
 #{i} .now{{font-size:26px;}} #{i} h3{{font-size:17px;}}
}}
#{i} .mark{{display:flex;justify-content:center;margin:0 0 20px;}}
#{i} .mark .thumb{{width:72px;height:72px;border-radius:14px;}}
#{i} .mark .thumb b{{font-size:16px;}} #{i} .mark .thumb small{{font-size:9.5px;}}
#{i} .stop>.mock{{max-width:780px;margin:0 auto 26px;}}
#{i} .fhero{{text-align:center;max-width:620px;margin:0 auto 22px;}}
#{i} .fhero h3{{font-size:24px;}} #{i} .fhero p{{margin:0;font-size:14.5px;}}
#{i} .steps{{max-width:760px;margin:0 auto 22px;}}
#{i} .price{{justify-content:center !important;}}
#{i} .stop-cta{{display:block;width:250px;max-width:100%;margin:4px auto 0;padding:14px 16px;font-size:15px;border-radius:12px;}}
#{i} .stop-cta.free{{background:linear-gradient(135deg,#1FB0B0,#147F7F) !important;box-shadow:0 8px 18px rgba(26,158,158,.32) !important;}}
@container (max-width:520px){{#{i} .fhero h3{{font-size:20px;}} #{i} .fhero p{{font-size:13.5px;}} #{i} .stop-cta{{width:220px;font-size:14px;padding:12px 14px;}}}}
"""
html = """<div class="stop">
  <div class="mark"><div class="thumb"><b>TRUST</b><small>FREE<br>SHEET</small></div></div>
  <div class="mock"><img src="PASTE-TRUST-IMAGE-URL" alt="The TRUST Sheet on a laptop: what you keep every month and where your money goes" width="1518" height="935"></div>
  <div class="fhero"><span class="stop-sub">Free</span>
  <h3>TRUST Sheet &#8211; Financial Tracker</h3>
  <p>You work hard for your money. Know where it goes, and how much you actually keep.</p></div>
  <div class="steps"><span class="sh">What the TRUST Sheet shows you</span><ol><li><span class="nb" style="--c:#1A9E9E">&#10003;</span><span>What you keep every month<small>Your real number, after every bill</small></span></li><li><span class="nb" style="--c:#8E1F45">&#10003;</span><span>Where your money goes<small>Needs, wants and what you keep</small></span></li><li><span class="nb" style="--c:#1B4D36">&#10003;</span><span>Your keep rate<small>The % of your income you hold on to</small></span></li><li><span class="nb" style="--c:#1A9E9E">&#10003;</span><span>Reclaimable money<small>Small leaks you can turn into savings</small></span></li><li><span class="nb" style="--c:#8E1F45">&#10003;</span><span>Debt to clear<small>Your total, so it stops hiding</small></span></li><li><span class="nb" style="--c:#1B4D36">&#10003;</span><span>What 1 hour of your time is worth<small>Spend with your real hourly value in mind</small></span></li><li><span class="nb" style="--c:#1A9E9E">&#10003;</span><span>Your next step<small>One clear action, every month</small></span></li></ol></div>
  <div class="price"><span class="note">Google Sheets &amp; Excel</span></div>
  <a class="stop-cta free" href="https://www.cybercnslt.com/free-financial-trust-sheet">Get the free sheet</a>
</div>"""
files['04-free-trust-sheet-card.html'] = block(i, 760, css, html, note='Free TRUST Sheet – Financial Tracker card')

# ---------- 04 "Hey, I'm Liliane" story card ----------
i = 'lj-about'
css = STOP.format(i=i) + f"""#{i} .stop{{border-top-color:var(--mag);padding:30px 32px;}}
#{i} .kick{{display:block;font:800 12px/1.2 "Avenir Next",Arial;letter-spacing:2.4px;text-transform:uppercase;color:var(--mut);margin:0 0 8px;}}
#{i} h2{{font:800 24px/1.2 "Avenir Next",Arial;color:var(--head);letter-spacing:-.6px;margin:0;}}
#{i} h2 .nm{{color:var(--magtxt,var(--mag));}}
#{i} .rule{{width:110px;height:5px;border-radius:5px;background:linear-gradient(90deg,var(--turq),var(--mag));margin:14px auto 20px;}}
#{i} h2{{text-align:center;}}
#{i} .who{{background:var(--hl);border-left:5px solid var(--mag);border-radius:0 12px 12px 0;padding:14px 18px;margin:0 0 16px;}}
#{i} .who p{{margin:0;color:var(--ink);font-size:15px;font-weight:600;}}
#{i} .jimg{{margin:0 0 26px;padding-bottom:22px;border-bottom:1px solid var(--cardbd);}}
#{i} .jimg img{{display:block;width:100%;height:auto;}}
#{i} .tn{{position:relative;height:58px;margin-top:2px;}}
#{i} .tn span{{position:absolute;top:0;transform:translateX(-50%);text-align:center;white-space:nowrap;font:800 12px/1.3 "Avenir Next",Arial;letter-spacing:1.6px;text-transform:uppercase;color:var(--turq);}}
html[data-theme="dark"] #{i} .tn span{{color:#35B7B7;}}
#{i} .tn span:first-child{{left:27%;}}#{i} .tn span:last-child{{left:73.5%;}}
#{i} .tn small{{display:block;margin-top:3px;font:600 13px/1.35 "Avenir Next",Arial;letter-spacing:.2px;text-transform:none;color:var(--mut);}}
#{i} .jcap{{margin:10px 0 0;text-align:center;font:600 13.5px/1.5 "Avenir Next",Arial;color:var(--mut);font-style:italic;}}
@media (max-width:480px){{#{i} .tn{{height:52px;}}#{i} .tn span{{font-size:11px;letter-spacing:1px;}}#{i} .tn small{{font-size:11px;}}}}
#{i} p{{font-size:15px;color:var(--ink);margin:0 0 12px;line-height:1.6;}}
#{i} p b{{color:var(--head);font-weight:800;}}
#{i} .by{{margin:18px 0 0;padding-top:14px;border-top:1px solid var(--cardbd);font:700 12.5px/1.5 "Avenir Next",Arial;color:var(--turq);}}
@media (max-width:420px){{#{i} .stop{{padding:24px 20px;}}#{i} h2{{font-size:20px;}}#{i} p,#{i} .who p{{font-size:14px;}}}}
#{i} .stop{{background:none !important;border:0 !important;box-shadow:none !important;border-radius:0 !important;padding:0 !important;}}
"""
html = """<div class="stop">
  <span class="kick" style="text-align:center;margin-bottom:16px">Who I am &amp; why I built this</span>
  <figure class="jimg"><img src="PASTE-JOURNEY-IMAGE-URL" alt="Liliane then as a flight attendant, and now as a cybersecurity consultant" width="1920" height="1080">
    <div class="tn"><span>Then<small>Flight attendant wanting<br>to become a pilot</small></span><span>Now<small>Cybersecurity consultant<br>in the financial sector</small></span></div>
    <p class="jcap">From the cabin to cybersecurity in the financial sector</p></figure>
  <h2>Hey, I'm <span class="nm">Liliane</span>.</h2>
  <div class="rule"></div>
  <div class="who"><p>I'm a full-time cybersecurity consultant at a Big Four firm, working in the financial sector. Alongside my 9&#8211;5, I support my mum, who is 83 and receives care at home after her cerebral haemorrhage.</p></div>
  <p>In my 20s I took out loans for my study fees, made financial decisions I'd make very differently today, traded without really understanding it, and even fell for an online scam. <b>I paid off &#8364;30,000 of debt</b>, not by first earning more, but by understanding my finances and making deliberate changes.</p>
  <p>Most financial advice told me to quit my job, hustle harder or get rich fast. None of it was made for someone with a demanding career and a mum who needs them. <b>So I decided to build the plan I wish I'd had, step by step.</b></p>
  <p class="by">Liliane &#183; cybersecurity consultant, solo-preneur, creator &#183; @cyber_cnslt</p>
</div>"""
files['05-about-liliane-card.html'] = block(i, 760, css, html, note='"Hey, I\'m Liliane" story card')

# ---------- the three road cards: exact journey hub layout (900px canvas, scaled like the journey site) ----------
ROAD = '''<div class="fork"><svg class="forksvg" viewBox="0 -60 900 440" width="900" height="440" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMin meet" role="img" aria-label="Three roads: Cybersecurity, Business, Finances">
  <defs>
    <linearGradient id="ljr-prog" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="350"><stop offset="0" stop-color="#35B7B7"/><stop offset="0.5" stop-color="#1A9E9E"/><stop offset="1" stop-color="#8E1F45"/></linearGradient>
    <linearGradient id="ljr-cyber" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1A9E9E"/><stop offset="1" stop-color="#0F4C4C"/></linearGradient>
    <linearGradient id="ljr-biz" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8E1F45"/><stop offset="1" stop-color="#5E1530"/></linearGradient>
    <linearGradient id="ljr-fin" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#245F46"/><stop offset="1" stop-color="#0F3324"/></linearGradient>
    <clipPath id="ljr-clip"><circle r="40"/></clipPath>
  </defs>
  <path class="road" d="M 450 80 C 450 205, 150 205, 150 350" fill="none" stroke-width="46" stroke-linecap="butt"/>
  <path class="road" d="M 450 80 C 450 205, 750 205, 750 350" fill="none" stroke-width="46" stroke-linecap="butt"/>
  <path class="road" d="M 450 80 L 450 350" fill="none" stroke-width="46" stroke-linecap="butt"/>
  <path class="road" d="M 450 0 L 450 80" fill="none" stroke-width="46" stroke-linecap="round"/>
  <path class="dash" d="M 450 80 C 450 205, 150 205, 150 350" fill="none" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 30" opacity="0.85"/>
  <path class="dash" d="M 450 80 C 450 205, 750 205, 750 350" fill="none" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 30" opacity="0.85"/>
  <path class="dash" d="M 450 80 L 450 350" fill="none" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 30" opacity="0.85"/>
  <path class="dash" d="M 450 0 L 450 80" fill="none" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 30" opacity="0.85"/>
  <path d="M 450 0 L 450 200" fill="none" stroke="url(#ljr-prog)" stroke-width="12" stroke-linecap="round"/>
  <text class="sign-hint" x="300" y="44" text-anchor="end">TURN LEFT</text>
  <text class="sign-hint" x="600" y="44" text-anchor="start">TURN RIGHT</text>
  <circle class="node" cx="450" cy="80" r="9" opacity=".9"/>
  <a class="signpost" href="{J}#cybersecurity"><g transform="translate(150,310)"><rect x="-135" y="-26" width="270" height="52" rx="13" fill="url(#ljr-cyber)" stroke="#ffffff" stroke-width="3"/><text class="sign-lbl" x="0" y="0" text-anchor="middle" dominant-baseline="central">CYBERSECURITY</text></g></a>
  <a class="signpost" href="{J}#business"><g transform="translate(450,310)"><rect x="-135" y="-26" width="270" height="52" rx="13" fill="url(#ljr-biz)" stroke="#ffffff" stroke-width="3"/><text class="sign-lbl" x="0" y="0" text-anchor="middle" dominant-baseline="central">BUSINESS</text></g></a>
  <a class="signpost" href="{J}#finances"><g transform="translate(750,310)"><rect x="-135" y="-26" width="270" height="52" rx="13" fill="url(#ljr-fin)" stroke="#ffffff" stroke-width="3"/><text class="sign-lbl" x="0" y="0" text-anchor="middle" dominant-baseline="central">FINANCES</text></g></a>
  <g class="car">
    <circle r="48" fill="rgba(53,183,183,.22)"><animate attributeName="r" values="43;56;43" dur="1.6s" repeatCount="indefinite"/></circle>
    <circle r="41" fill="#0f151c"/>
    <image href="{K}" x="-40" y="-40" width="80" height="80" clip-path="url(#ljr-clip)"/>
    <circle r="40" fill="none" stroke="#ffffff" stroke-width="4"/>
    <circle r="43.5" fill="none" stroke="#35B7B7" stroke-width="3.5"/>
  </g>
</svg></div>'''.replace('{J}', JOURNEY).replace('{K}', KART)
i = 'lj-roads'
css = f"""#{i}{{max-width:none;padding:0;}}
#{i} .ljr-wrap{{width:100%;overflow:hidden;}}
#{i} .ljr{{width:100%;max-width:900px;margin:0 auto;}}
#{i} .startnote{{text-align:center;padding:6px 24px 0;}}
#{i} .startnote p{{margin:0 auto;max-width:620px;font-size:14px;line-height:1.55;color:var(--mut);font-weight:500;}}
#{i} .startnote p b{{display:block;margin-bottom:4px;font:800 18px/1.3 "Avenir Next",Arial;color:var(--head);}}
#{i} .fork{{position:relative;width:900px;max-width:100%;margin:0 auto;}}
#{i} .forksvg{{display:block;width:100%;height:auto;}}
#{i} .road{{stroke:#2b3139;}} html[data-theme="dark"] #{i} .road{{stroke:#3a4450;}}
#{i} .dash,#{i} .node{{stroke:#ffffff;fill:none;}} #{i} .node{{fill:#ffffff;stroke:none;}}
html[data-theme="dark"] #{i} .dash{{stroke:#d3dce4;}} html[data-theme="dark"] #{i} .node{{fill:#d3dce4;}}
#{i} .sign-lbl{{font-family:"Avenir Next","Helvetica Neue",Arial,sans-serif;font-weight:800;font-size:15px;letter-spacing:1.4px;fill:#fff;}}
#{i} .sign-hint{{font-family:"Avenir Next","Helvetica Neue",Arial,sans-serif;font-weight:800;font-size:11px;letter-spacing:2px;fill:var(--mut);}}
#{i} .signpost{{cursor:pointer;}} #{i} .signpost:hover rect{{filter:brightness(1.08);}}
#{i} .car{{animation:ljrBob 3s ease-in-out infinite;}}
@keyframes ljrBob{{0%,100%{{transform:translate(450px,205px);}}50%{{transform:translate(450px,197px);}}}}
@media (prefers-reduced-motion:reduce){{#{i} .car{{animation:none;transform:translate(450px,205px);}}}}
#{i} .pick{{position:relative;z-index:3;width:100%;max-width:900px;margin:0 auto;padding:0 2.9%;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px;}}
#{i} .pcard{{display:flex;flex-direction:column;background:var(--card);border:1px solid var(--cardbd);border-top:5px solid var(--turq);border-radius:20px;padding:30px 24px 28px;
  text-align:center;box-shadow:0 8px 22px rgba(10,20,25,.08);transition:transform .5s cubic-bezier(.2,.75,.25,1),box-shadow .25s ease;}}
#{i} .pcard:hover{{transform:translateY(-8px) scale(1.04);box-shadow:0 26px 54px rgba(10,20,25,.24);z-index:2;}}
#{i} .pcard.cyber{{border-top-color:#1A9E9E;}}#{i} .pcard.biz{{border-top-color:#8E1F45;}}#{i} .pcard.fin{{border-top-color:#1B4D36;}}
#{i} .pic{{font-size:32px;line-height:1;margin-bottom:10px;}}
#{i} h3{{display:flex;align-items:center;justify-content:center;min-height:2.3em;font:800 24px/1.15 "Avenir Next",Arial;color:var(--head);margin:0 0 10px;letter-spacing:-.4px;}}
#{i} p{{margin:0 0 18px;font-size:14px;color:var(--mut);line-height:1.5;font-weight:500;}}
#{i} .pcta{{display:flex;align-items:center;justify-content:center;width:100%;min-height:46px;margin-top:auto;font:800 13px/1.25 "Avenir Next",Arial;padding:10px 12px;border-radius:12px;color:#fff;letter-spacing:.2px;}}
#{i} .cyber .pcta{{background:linear-gradient(135deg,#1A9E9E,#0F4C4C);box-shadow:0 8px 18px rgba(26,158,158,.30);}}
#{i} .biz .pcta{{background:var(--mag);box-shadow:0 8px 18px rgba(142,31,69,.28);}}
#{i} .fin .pcta{{background:var(--green);box-shadow:0 8px 18px rgba(27,77,54,.28);}}
#{i} .t-short{{display:none;}}
/* narrow screens: the road scales with its viewBox; labels and cards get compact sizes */
@container (max-width:700px){{
 #{i} .sign-lbl{{font-size:24px;letter-spacing:.4px;}} #{i} .sign-hint{{font-size:20px;}}
 #{i} .pick{{gap:10px;}} #{i} .pcard{{padding:16px 8px 12px;border-radius:14px;}}
 #{i} .pic{{font-size:26px;margin-bottom:6px;}} #{i} h3{{font-size:16px;min-height:2.4em;margin-bottom:6px;}}
 #{i} .pcard p{{font-size:12.5px;margin-bottom:10px;}}
 #{i} .pcta{{min-height:38px;font-size:12px;padding:8px 6px;border-radius:10px;}}
 #{i} .pcta .t-full{{display:none;}} #{i} .pcta .t-short{{display:inline;}}
 #{i} .startnote p{{font-size:14px;}} #{i} .startnote p b{{font-size:17px;}}
}}
@container (max-width:460px){{
 #{i} .sign-lbl{{font-size:30px;letter-spacing:0;}} #{i} .sign-hint{{display:none;}}
 #{i} .pcard p{{display:none;}} #{i} h3{{font-size:14.5px;}} #{i} .sign-lbl{{font-size:28px;}}
}}
"""
html = f"""<div class="ljr-wrap"><div class="ljr">
<section class="startnote"><p><b>Start Your Journey Today.</b>Pick the road that fits your journey. You can always come back and try another one.</p></section>
{ROAD}
<section class="pick">
  <a class="pcard cyber" href="{JOURNEY}#cybersecurity"><div class="pic">&#128737;&#65039;</div><h3>Grow Your Career</h3><p>From a non-tech background to your first cyber role.</p><span class="pcta"><span class="t-full">Start Your Cyber Journey</span><span class="t-short">Start Here</span></span></a>
  <a class="pcard biz" href="{JOURNEY}#business"><div class="pic">&#128640;</div><h3>Grow Your Business</h3><p>Build income beside your 9-5, the strategic way.</p><span class="pcta"><span class="t-full">Start Your Business Journey</span><span class="t-short">Start Here</span></span></a>
  <a class="pcard fin" href="{JOURNEY}#finances"><div class="pic">&#128176;</div><h3>Grow Your Wealth</h3><p>See exactly how much money you actually keep.</p><span class="pcta"><span class="t-full">Start Your Finance Journey</span><span class="t-short">Start Here</span></span></a>
</section>
</div></div>"""
script = ''
files['06-three-road-cards.html'] = block(i, 900, css, html, script, note='The 3 roads + road cards (same layout as your journey hub) · put this after the offers')

for n, c in files.items():
    open(os.path.join(OUT, n), 'w').write(c)
    print(n, len(c))
