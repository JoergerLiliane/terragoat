import math

TP = 'TRUST Tracker Pro'
SHORT = ['Mindset', 'Numbers', 'Debts', 'Safety net', 'Investing', 'Income', 'Time']
FULL = [('Money mindset: your 9–5', 'is your wealth engine', 'The five laws of money, your real hourly value and why your salary is your biggest asset.', 'U · Understand'),
        ('Know your salary', '&amp; your numbers', 'What you really keep, where it leaks, and how to grow the number at the top.', 'T · Track · R · Reclaim'),
        ('Clear your debts', '<i>optional</i>', 'A small starter buffer first, then the most expensive debt. No debt? Go to Stage 4.', 'U · Understand · S · Save'),
        ('Build a safety net', '', 'A full emergency fund of 3–6 months of needs, goal pots and an automated payday.', 'S · Save'),
        ('Build wealth with', 'smart investing', 'Compound growth, costs, risk and red flags. Only invest in what you understand.', 'Invest'),
        ('Build multiple', 'income streams', 'One stream, one 90-day test, built in the hours you can truly protect.', 'Income Streams'),
        ('Repeat, automate', '&amp; buy back time', 'A system that runs on its own, and hours that go back to the people you love.', 'T · Time · Monthly Review')]
GRAD = ['g1', 'g2', 'g3']

CSS = '''
  .nb{white-space:nowrap;}
  .rstrip{margin:12px 0 2px;background:var(--white);border:1px solid var(--line);border-radius:14px;padding:4px 8px 0;}
  .rstrip svg{display:block;width:100%;height:auto;}
  .bigroad{position:relative;margin:12px 0 0;height:780px;}
  .bigroad svg{position:absolute;left:0;top:0;width:700px;height:780px;}
  .bigroad .lb{position:absolute;left:236px;width:464px;transform:translateY(-50%);border-left:4px solid var(--c);padding:3px 0 3px 12px;}
  .bigroad .lb b{display:block;font:800 15px/1.25 var(--sans);color:var(--teal);}
  .bigroad .lb b i{font-weight:600;color:var(--mut);}
  .bigroad .lb small{display:block;font-size:12.6px;line-height:1.4;color:var(--body);margin-top:3px;}
  .bigroad .lb em{display:inline-block;margin-top:5px;font:800 10.5px/1 var(--sans);font-style:normal;letter-spacing:1px;text-transform:uppercase;color:var(--bord-dk);background:var(--bord-tint);padding:4px 8px;border-radius:9px;}
  .bigroad .tagS,.bigroad .tagG{position:absolute;transform:translate(-50%,-50%);font:800 11px/1 var(--sans);letter-spacing:2px;text-transform:uppercase;padding:8px 13px;border-radius:16px;color:#fff;white-space:nowrap;}
  .bigroad .tagS{background:var(--teal);} .bigroad .tagG{background:linear-gradient(135deg,var(--bord),var(--bord-dk));}
  .mist{margin-top:16px;display:grid;grid-template-columns:1fr 1fr;gap:12px;}
  .mist>div{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:14px 16px;}
  .mist .nl{font:800 12px/1.3 var(--sans);letter-spacing:1.5px;text-transform:uppercase;color:var(--bord-dk);margin:0 0 8px;}
  .mist .ok .nl{color:var(--teal);}
  .mist ul{margin:0;padding-left:18px;font-size:13.2px;color:var(--body);line-height:1.5;} .mist li{margin:5px 0;}
  .grid50{display:grid;grid-template-columns:repeat(25,1fr);gap:4px;margin-top:8px;}
  .grid50 i{display:block;aspect-ratio:1;border:1.5px solid var(--turq);border-radius:4px;}
  .grid50 i.f{background:var(--turq);}
  .grid50 i.h{border-color:var(--bord);}
  .acc{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-top:8px;align-items:stretch;}
  .acc div{position:relative;background:var(--turq-tint);border-radius:10px;padding:10px 10px;font-size:12.4px;line-height:1.4;color:var(--body);}
  .acc div b{display:block;color:var(--teal);font-size:13px;margin-bottom:3px;}
  .acc div.in{background:var(--teal);color:#dff0f0;} .acc div.in b{color:#fff;}
  .acc div.sp{background:var(--bord-tint);} .acc div.sp b{color:var(--bord-dk);}
  .acc div:not(:last-child)::after{content:"›";position:absolute;right:-8px;top:50%;transform:translateY(-50%);font:800 18px/1 var(--sans);color:var(--bord);}
  .wish{margin-top:16px;background:var(--white);border:1px solid var(--line);border-radius:14px;padding:16px 20px;}
  .wish .nl{font:800 12px/1.3 var(--sans);letter-spacing:1.5px;text-transform:uppercase;color:var(--bord-dk);margin:0 0 8px;}
  .wish p{margin:6px 0;font-size:14px;}
'''


def strip(cur, mode='open'):
    """Horizontal 7-stage road. mode 'open': stage cur is 'You are here'. mode 'done': stage cur is ticked, next is highlighted."""
    W, H, x0, x1, yc, amp = 700, 84, 26, 674, 36, 11
    pts = []
    for k in range(0, 161):
        x = x0 + (x1 - x0) * k / 160
        y = yc + amp * math.sin((x - x0) / (x1 - x0) * math.pi * 3.5)
        pts.append(f'{x:.1f},{y:.1f}')
    d = 'M ' + ' L '.join(pts)
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="The 7 stages of the roadmap, stage {cur} highlighted">',
           '<defs><linearGradient id="sg1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1A9E9E"/><stop offset="1" stop-color="#134E4E"/></linearGradient>'
           '<linearGradient id="sg2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9E1B5E"/><stop offset="1" stop-color="#6B1440"/></linearGradient></defs>',
           f'<path d="{d}" fill="none" stroke="#2b3139" stroke-width="13" stroke-linecap="round"/>',
           f'<path d="{d}" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-dasharray="2 12" opacity=".9"/>']
    hl = cur if mode == 'open' else min(cur + 1, 7)
    for i in range(7):
        n = i + 1
        x = x0 + 30 + (x1 - x0 - 60) * i / 6
        y = yc + amp * math.sin((x - x0) / (x1 - x0) * math.pi * 3.5)
        done = n < cur or (mode == 'done' and n == cur)
        if n == hl and not (mode == 'done' and cur == 7):
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="17" fill="url(#sg2)" stroke="#fff" stroke-width="3.5"/>')
            out.append(f'<text x="{x:.1f}" y="{y + 5.5:.1f}" text-anchor="middle" font-family="Helvetica Neue,Arial" font-size="15" font-weight="800" fill="#fff">{n}</text>')
            tag = 'YOU ARE HERE' if mode == 'open' else 'NEXT'
            tw = 92 if mode == 'open' else 46
            ty = y - 26 if y > 28 else y + 26
            out.append(f'<rect x="{x - tw / 2:.1f}" y="{ty - 10:.1f}" width="{tw}" height="17" rx="8.5" fill="#9E1B5E"/>')
            out.append(f'<text x="{x:.1f}" y="{ty + 2.5:.1f}" text-anchor="middle" font-family="Helvetica Neue,Arial" font-size="9.5" font-weight="800" letter-spacing="1.2" fill="#fff">{tag}</text>')
        elif done:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="url(#sg1)" stroke="#fff" stroke-width="3"/>')
            out.append(f'<text x="{x:.1f}" y="{y + 4.5:.1f}" text-anchor="middle" font-family="Helvetica Neue,Arial" font-size="13" font-weight="800" fill="#fff">✓</text>')
        else:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="#fff" stroke="#1A9E9E" stroke-width="3"/>')
            out.append(f'<text x="{x:.1f}" y="{y + 4.5:.1f}" text-anchor="middle" font-family="Helvetica Neue,Arial" font-size="12.5" font-weight="800" fill="#134E4E">{n}</text>')
        col = '#6B1440' if n == hl else ('#134E4E' if done else '#54636b')
        out.append(f'<text x="{x:.1f}" y="{H - 12}" text-anchor="middle" font-family="Helvetica Neue,Arial" font-size="11" font-weight="{800 if n == hl else 700}" fill="{col}">{SHORT[i]}</text>')
    out.append('</svg>')
    return '<div class="rstrip">' + ''.join(out) + '</div>'


def bigroad():
    CX, A, Y0, Y1 = 118, 74, 735, 50
    segs = 7
    h = (Y0 - Y1) / segs
    d = f'M {CX} {Y0}'
    pins = []
    for k in range(segs):
        y = Y0 - h * k
        y2 = y - h
        sx = (-1 if k % 2 else 1) * A
        d += f' C {CX + sx} {y - h * .12:.1f}, {CX + sx} {y2 + h * .12:.1f}, {CX} {y2:.1f}'
        pins.append((CX + 0.75 * sx, y - h / 2))
    cols = ['#1A9E9E', '#9E1B5E', '#245F46']
    svg = ['<svg viewBox="0 0 700 780" role="img" aria-label="The roadmap as a road: seven stages from Start to Time freedom">',
           '<defs><linearGradient id="bg1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1A9E9E"/><stop offset="1" stop-color="#134E4E"/></linearGradient>'
           '<linearGradient id="bg2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9E1B5E"/><stop offset="1" stop-color="#6B1440"/></linearGradient>'
           '<linearGradient id="bg3" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#245F46"/><stop offset="1" stop-color="#0F3324"/></linearGradient></defs>']
    for i, (x, y) in enumerate(pins):
        svg.append(f'<line x1="{x + 24:.1f}" y1="{y:.1f}" x2="228" y2="{y:.1f}" stroke="{cols[i % 3]}" stroke-width="2" stroke-dasharray="3 5" opacity=".6"/>')
    svg.append(f'<path d="{d}" fill="none" stroke="#2b3139" stroke-width="30" stroke-linecap="round"/>')
    svg.append(f'<path d="{d}" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 20" opacity=".9"/>')
    for i, (x, y) in enumerate(pins):
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="19" fill="url(#bg{i % 3 + 1})" stroke="#fff" stroke-width="4"/>')
        svg.append(f'<text x="{x:.1f}" y="{y + 6:.1f}" text-anchor="middle" font-family="Helvetica Neue,Arial" font-size="16" font-weight="800" fill="#fff">{i + 1}</text>')
    svg.append('</svg>')
    lbl = []
    for i, (x, y) in enumerate(pins):
        a, b, desc, tab = FULL[i]
        lbl.append(f'<div class="lb" style="top:{y:.0f}px;--c:{cols[i % 3]}"><b>{a} {b}</b><small>{desc}</small><em>{TP} · {tab}</em></div>')
    tags = (f'<span class="tagS" style="left:{CX}px;top:{Y0 + 22}px">Start</span>'
            f'<span class="tagG" style="left:{CX}px;top:{Y1 - 24}px">🏁 Time freedom</span>')
    return '<div class="bigroad">' + ''.join(svg) + ''.join(lbl) + tags + '</div>'


def mistakes(bad, good, bad_t='Common mistakes at this stage', good_t="Liliane's tip"):
    b = ''.join(f'<li>{x}</li>' for x in bad)
    g = ''.join(f'<li>{x}</li>' for x in good)
    return (f'<div class="mist"><div><p class="nl">{bad_t}</p><ul>{b}</ul></div>'
            f'<div class="ok"><p class="nl">{good_t}</p><ul>{g}</ul></div></div>')


def box2(t1, items1, t2, items2, heavy2=False):
    l1 = ''.join(f'<li>{x}</li>' for x in items1)
    l2 = ''.join(f'<li>{x}</li>' for x in items2)
    return (f'<div class="two"><div class="box"><div class="when">{t1}</div><ol class="tpl">{l1}</ol></div>'
            f'<div class="box{" heavy" if heavy2 else ""}"><div class="when">{t2}</div><ol class="tpl">{l2}</ol></div></div>')


def ifthen(title, ps, red=False):
    return f'<div class="ifthen{" red" if red else ""}"><p class="nl">{title}</p>' + ''.join(f'<p>{p}</p>' for p in ps) + '</div>'


def table(head, rows, cls='budget'):
    th = ''.join(f'<th>{h}</th>' for h in head)
    tr = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<div class="tablewrap"><table class="{cls}"><tr>{th}</tr>{tr}</table></div>'


# ---------------- page additions (page number -> html added before the footer) ----------------
ADD = {}

ADD[3] = '''<div class="wish"><p class="nl">Three things I wish I'd known at 25</p>
  <p><b>1 · Income is not wealth.</b> What you keep, and what you do with it, decides your future, not your salary on its own.</p>
  <p><b>2 · Understanding comes before investing.</b> Every expensive mistake I made started with something I didn't fully understand.</p>
  <p><b>3 · Time is the real currency.</b> The goal was never more money. It was more hours with the people I love, while they're still here.</p></div>'''

ADD[5] = box2('Your 2-hour setup · have this ready',
              ['Your last payslip and last 3 months of bank statements', 'Your banking app, logged in', 'A list of debts: balance, rate, minimum', 'Your calendar, to book the weekly slot', f'{TP}, open on the About Me tab'],
              'Where each number lives',
              ['Net pay: payslip or bank statement', 'Fixed costs: standing orders and direct debits', 'Subscriptions: card statement, app stores', 'Debt rates: loan contract or card statement', 'Pension: your annual statement or HR portal'])

ADD[7] = table(['Answer in order · stop at the first “no”', 'If no, you are at'],
               [['Do you keep €0 or more at the end of a normal month?', 'Level 0 · Overwhelmed'],
                ['Do you have one month of needs saved, separately?', 'Level 1 · Stable'],
                ['Is your consumer debt (cards, overdraft, BNPL) at €0?', 'Level 2 · Buffered'],
                ['Is your full emergency fund (3–6 months of needs) saved?', 'Level 3 · Debt-free'],
                ['Does extra income cover at least 25% of your needs?', 'Level 4 · Secure'],
                ['Does extra income cover all of your needs?', 'Level 5 · Flexible'],
                ['All yes?', 'Level 6 · Free to choose']]) + \
    f'<p class="cnote">Find your level in 60 seconds. {TP} runs exactly this test on the KEEP dashboard every time you update your numbers, so you never have to work it out by hand again.</p>'

ADD[8] = box2('Good slots for busy people', ['Sunday evening, before the week starts', 'Payday lunch break', 'The commute home (on the train, not driving)', 'Friday, right after you update your win file'],
         'Make it stick', ['Same day, same time, as a recurring appointment', 'Pair it with something you enjoy: tea, music', 'Tell one person when your slot is', 'Tick it off in Monthly Review'])

ADD[9] = box2('What this means for your plan', ['Learn the basics once: Stage 1 and the glossary', 'Automate decisions, so worry doesn\'t make them', 'Expect about two months before habits feel easy', 'Keep it simple: one number, one focus, one stream'],
              'Built into this roadmap', ['Payday transfers instead of willpower', 'A 15-minute weekly rhythm', 'A heavy-week version on every stage', 'Checklists you can see, not feelings you guess'])

ADD[11] = '<div class="quickwin"><p class="nl">Practise the laws this week</p><p>Pick law 1 or 2 and do one thing about it before Sunday: move €20 to savings on payday, or skip one want and write down what you kept. Small proof beats big intentions.</p></div>'

ADD[12] = box2('Three ways to grow your engine this year', ['A salary review with evidence (your win file, Stage 2)', 'One skill or certification your market pays more for', 'A bigger role, project or internal move, even sideways'],
               'Before you ask, check', ['Your market range: salary surveys, job ads, recruiters', 'What a new title would pay elsewhere', 'Benefits worth money: pension, training, remote days', 'When budgets are set in your company']) + \
    ifthen('If you\'re not ready to ask yet', ['<b>Start the win file today.</b> In three months you\'ll have twelve wins with numbers, and the conversation writes itself.',
                                             '<b>Ask for feedback first:</b> “What would make me ready for the next level?” That answer is your plan.',
                                             '<b>Decide now</b> where the raise goes when it comes: buffer, debt, investing or time.'])

ADD[13] = table(['Price', 'At €12 an hour, it costs you', 'Worth it?'],
                [['€4 coffee to go', '20 minutes', '☐ yes ☐ no'], ['€60 dinner out', '5 hours', '☐ yes ☐ no'], ['€120 pair of shoes', '10 hours', '☐ yes ☐ no'],
                 ['€900 new phone', '75 hours, almost two working weeks', '☐ yes ☐ no'], ['€1,500 family holiday', '125 hours', '☐ yes ☐ no']]) + \
    '<p class="cnote">Some things are worth every hour, like the holiday with your family. The point isn\'t to say no to everything, it\'s to say yes on purpose.</p>'

ADD[16] = '<div class="weeks" style="grid-template-columns:repeat(5,1fr)">' + ''.join(
    f'<div><span class="m">{a}</span><b>{b}</b><span>{c}</span></div>' for a, b, c in [
        ('0:00–0:20', 'Gather', 'Payslip, 3 months of statements, debt letters.'),
        ('0:20–1:00', 'Enter', 'Money in, then every cost, in T · Track.'),
        ('1:00–1:30', 'Sort', 'Need or want, one line at a time. No judging.'),
        ('1:30–1:50', 'Reclaim', 'Subscriptions and contracts into R · Reclaim.'),
        ('1:50–2:00', 'Automate', 'One standing order on payday. Done.')]) + '</div>' + \
    '<p class="cnote">Your 2-hour setup session, minute by minute. Stop at any line and continue next week: the tracker keeps your place.</p>'

ADD[18] = box2('Wins that count · with numbers', ['“Automated a report: saves the team 6 hours a month”', '“Closed 14 audit findings before the deadline”', '“Trained 3 new colleagues, all productive in 4 weeks”', '“Reduced vendor costs by €8,000 a year”'],
               'Wins that don\'t count yet', ['“Worked late a lot”: effort, not a result', '“Was very busy”: add what came out of it', '“Helped the team”: who, how, what changed?', 'Turn each into a number before you use it'])

ADD[19] = ''
ADD[21] = box2('Where the extra €40 a month can come from', ['One cancelled subscription from R · Reclaim', 'Cooking twice more a week instead of takeaway', 'Selling one thing you no longer use', 'Your next raise, before you get used to it'],
               'Keep the debt from coming back', ['Card removed from shopping sites and apps', 'Buy-now-pay-later switched off', 'Starter buffer for real surprises', 'Goal pots for the costs you know are coming'])

ADD[23] = box2('Your monthly debt check · 5 minutes', ['All minimums paid automatically?', 'Extra payment went to Priority 1?', 'New balance written in U · Understand', 'Any new debt? If yes, why, and the fix'],
               'Find extra for Priority 1', ['Reclaimed money from Stage 2', 'Tax refund or bonus: at least half', 'Side income, after its tax pot', 'Rounding up every payment to the next €10']) + \
    ifthen('If you\'re tempted to use the card again', ['<b>Wait 48 hours.</b> Most urges are gone by then.',
                                                       '<b>Check your goal pots first.</b> If it\'s a known cost, it should have a pot.',
                                                       '<b>Use the starter buffer for real emergencies only</b>, and refill it before any extra payment.'])

ADD[23] += '<div class="formula"><p class="nl">My debt-free date</p><p><b>Total debt</b> €______ ÷ <b>(minimums + extra a month)</b> €______ = about ______ months <span>Add a few months for interest. U · Understand calculates it exactly, debt by debt. My debt-free month: ______________</span></p></div>'

ADD[26] = table(['Where to keep it', 'Good for a safety net?', 'Why'],
                [['Current account', 'No', 'Too easy to spend by accident, often no interest.'],
                 ['Separate savings or instant-access account', 'Yes', 'Easy to reach in a day or two, kept apart from daily spending.'],
                 ['Fixed-term deposit', 'Only part of it', 'Better rate, but locked. Keep at least one month instantly available.'],
                 ['Shares or funds', 'No', 'Can be down exactly when you need them. That\'s Stage 5 money.']]) + \
    ifthen('If you\'re starting from zero', ['<b>Aim for €500 first.</b> It covers most small emergencies and builds the habit.',
                                           '<b>Then one month of needs</b> (your starter buffer), then the full fund.',
                                           '<b>Any amount counts.</b> €25 a month is a habit; the amount can grow later.'])

ADD[28] = ('<div class="wish"><p class="nl">Colour in one box for every 2% of your target</p><div class="grid50">' +
           ''.join('<i class="h"></i>' if k in (24, 49) else '<i></i>' for k in range(50)) +
           '</div><p class="cnote" style="margin-top:8px">The pink boxes are your milestones: halfway, and the full fund. Stick this page on the fridge.</p></div>' +
           box2('Five ways to fill it faster', ['Half of every bonus or tax refund', 'Your old debt payment, from Stage 3', 'Reclaimed costs from R · Reclaim', 'Selling what you no longer use', '1–2% of every raise'],
                'Milestones to celebrate, for free', ['€500: small emergencies are covered', 'One month of needs: starter buffer done', '50%: a walk somewhere you love', '100%: Level 4 · Secure. Write down the date', 'Tell someone. It matters.']))

ADD[34] = box2('Ask any provider before you sign', ['Who regulates you, and where can I check that?', 'What does it cost a year, all in, in percent?', 'How do I get my money out, and how long does it take?', 'What happens to my money if you go bankrupt?'],
               'Walk away if…', ['They promise high returns with little risk', 'They push you to decide today', 'You can\'t find them in the official register', 'They contacted you first, on social media'], heavy2=True) + \
    '<p class="cnote">In Germany you can check providers in the BaFin company database. Other countries have their own regulator registers.</p>'

ADD[37] = box2('Your 3 protected hours a week', ['Block 1 · 90 minutes: create (write, build, record)', 'Block 2 · 90 minutes: show up (share, talk, sell)', 'Same two slots every week, in your calendar', 'Never taken from sleep or family time first'],
               'What to log every Friday', ['Hours spent this week', 'People reached or conversations had', 'Euros earned, if any', 'One thing you learned about your buyers']) + \
    ifthen('Protect the test', ['<b>No new ideas until day 90.</b> Write them on a “later” list instead.', '<b>Heavy week?</b> Do one 30-minute block. The test pauses, it doesn\'t fail.', '<b>Tell one person</b> your day-90 date. It makes stopping or keeping a real decision.'])

ADD[38] = '''<div class="formula" style="border-color:var(--bord)"><p class="nl">Example · filled in</p>
    <p><b>Who it's for:</b> women moving into cybersecurity from another career</p>
    <p><b>The problem:</b> “I don't know where to start, and I'm scared I'm too late.”</p>
    <p><b>What they get:</b> a 30-day starter plan, with the first certification and a CV template</p>
    <p><b>Price:</b> €29 · <b>Where they'll find it:</b> Instagram, where I already share my story</p></div>''' + \
    ifthen('Price check', ['<b>Too cheap</b> if you\'d be annoyed to sell it 50 times.', '<b>About right</b> if the first 10 buyers say yes without a long discussion.', '<b>Raise it</b> after 10 happy buyers, not before the first.'])

ADD[39] = ifthen('Day-90 decision rules', ['<b>Keep</b> if € per hour is rising and you enjoy it, even if it\'s still below your job.',
                                          '<b>Change</b> if people are interested but not buying: fix the offer, the price or the channel.',
                                          '<b>Stop</b> if nobody bites after 90 days of real effort. That\'s data, not failure.'])

ADD[42] = '<div class="quickwin"><p class="nl">10-minute quick win</p><p>Write your baseline × 12 on a sticky note and put it on your fridge. That one number is your “enough”: the amount that makes work a choice.</p></div>'

ADD[43] = box2('Book them now · 4 recurring appointments', ['Weekly: ______ (day) at ______ (time)', 'Monthly: the ______ of each month', 'Quarterly: January, April, July, October', 'Yearly money date: ______ (6–8 weeks before your salary review)'],
               'Keep the rhythm when life is full', ['Every appointment has a 2-minute version', 'Move it, never delete it', 'The yearly date is the one never to skip', 'Do the monthly review with your partner, if you share costs'])

ADD[44] = ('<div class="wish"><p class="nl">Your money flow on payday</p><div class="acc">'
           '<div class="in"><b>Salary</b>arrives in your main account</div>'
           '<div><b>Bills</b>needs and debt minimums leave automatically</div>'
           '<div><b>Safety net</b>your first hour, before anything else</div>'
           '<div><b>Investing</b>a fixed amount on day 2</div>'
           '<div class="sp"><b>Spending</b>what\'s left is yours, guilt-free</div>'
           '</div><p class="cnote" style="margin-top:8px">Four or five accounts sound complicated, but they make every decision automatic. Most banks let you open sub-accounts for free.</p></div>')

ADD[44] += ifthen('Before you automate', ['<b>Pick a date 1–2 days after payday</b>, so the salary has always arrived.', '<b>Start smaller than you think.</b> Raise the amount after three months that worked.', '<b>Keep one month of needs in the bills account</b>, so a late salary never bounces a payment.'])

ADD[45] = box2('Free hours to take back first', ['Unpaid overtime: leave on time twice a week', 'Notifications off after 7 pm', 'One big shop instead of several small ones', 'Batch cooking on Sunday', 'Saying no to one meeting a week'],
               'Paid help worth checking', ['Cleaning help every two weeks', 'Grocery delivery', 'A laundry service in heavy months', 'Care support, so you can be family, not only a carer', 'Childcare for one fixed afternoon']) + \
    '<div class="formula"><p class="nl">Is it worth buying?</p><p><b>Cost a month ÷ hours gained a month = € per hour bought</b> <span>e.g. €80 ÷ 6 hours = €13.33. If that\'s close to your real hourly value and the hours go to the people you love, it\'s usually worth it.</span></p></div>'

ADD[47] = ('<div class="weeks">' + ''.join(f'<div><span class="m">{a}</span><b>{b}</b><span>{c}</span></div>' for a, b, c in [
    ('End of month 3', 'Checkpoint 1', 'Level 1 or 2. Keep rate known, win file running.'),
    ('End of month 6', 'Checkpoint 2', 'Debt-free or close. Safety net growing.'),
    ('End of month 9', 'Checkpoint 3', 'Level 4 · Secure. Investing set up.'),
    ('End of month 12', 'Checkpoint 4', 'One stream tested. Time map done. Year two planned.')]) + '</div>' +
    ifthen('If life swallows a month', ['<b>Repeat it.</b> The plan is 12 focus months, not 12 calendar months.',
                                       '<b>Keep the automation running</b>, even if nothing else happens.',
                                       '<b>Most people need 12 to 18 months.</b> Caring, illness and busy seasons are part of the plan, not a failure of it.']) +
    '<div class="box" style="margin-top:16px"><div class="when">My year in one sentence</div><p class="script">In 12 months, I want to be at Level ______, with ______ more hours a week for ______________________.</p></div>')

ADD[48] = ('<div class="two"><div class="box"><div class="when">Trap · comparing yourself online</div><p class="script">Other people\'s highlights make your progress look small. <b>Fix:</b> compare only with your own Monthly Review from three months ago.</p></div>'
           '<div class="box"><div class="when">Trap · doing it alone</div><p class="script">Money stays a private worry and decisions stay hard. <b>Fix:</b> share your Freedom Level with one person you trust, or your partner, once a month.</p></div></div>'
           '<div class="box" style="margin-top:16px"><div class="when">My trap plan</div><ol class="tpl"><li>The trap I fall into most is… ______________________________</li><li>The early sign I\'ll watch for is… ______________________________</li><li>My fix, in one sentence: ______________________________</li></ol></div>')

ADD[48] += '<div class="quickwin"><p class="nl">10-minute quick win</p><p>Read the seven traps again and circle the one you recognise most. Tell one person about it this week. A trap you can name is a trap you can avoid.</p></div>'

GL_MORE = [('Net pay', 'What actually lands in your account after tax and social contributions.'),
           ('Gross pay', 'Your salary before anything is taken off. The number in your contract.'),
           ('Needs and wants', 'Needs keep your life running; wants make it nicer. Both are fine, as long as you know which is which.'),
           ('Reclaim', 'Cutting, reducing or renegotiating a cost, and moving the difference to your future.'),
           ('Standing order', 'An automatic transfer you set up once that runs on the same day every month.'),
           ('Diversification', 'Spreading money across many investments so one failure can\'t sink you.'),
           ('Index fund', 'A fund that follows a whole market instead of trying to pick winners.'),
           ('Volatility', 'How much an investment\'s value goes up and down. Normal, and why you need time.'),
           ('Lifestyle creep', 'Spending that quietly rises with every raise, until the raise is gone.')]


def glossary_rows():
    return ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in GL_MORE)


# checklist pages: road strip + mistakes/tips
CHK = {14: (1, ['Skipping the money why because it feels “soft”', 'Calculating hourly value with contract hours only', 'Waiting for a calm week to start'],
            ['Your why is what gets you through heavy weeks. Write it first.', 'Count overtime and commute: that\'s your real hour.', 'Start this week, with 15 minutes.']),
       19: (2, ['Guessing numbers instead of checking statements', 'Cutting everything at once, then giving up', 'Treating a raise as permission to spend'],
            ['Use real statements. Your memory is kinder than your bank.', 'Cut one leak at a time, and move it on payday.', 'Give the raise a job before it arrives.']),
       24: (3, ['Paying off debt with no buffer, then borrowing again', 'Splitting extra money across every debt', 'Closing old cards before the balances are paid'],
            ['Starter buffer first, always.', 'All extra goes to Priority 1: the highest rate.', 'Pay first, then close or lower the limit.']),
       29: (4, ['Keeping the fund in your current account', 'Using it for holidays and Christmas', 'Investing before it\'s full'],
            ['Separate account, with a name that reminds you why.', 'Known costs get goal pots, not the fund.', 'Full fund first. Then Stage 5.']),
       35: (5, ['Buying what a friend or influencer recommends', 'Checking your investments every day', 'Stopping your monthly amount when markets fall'],
            ['If you can\'t explain it in two sentences, don\'t buy it.', 'Look once a year, on your money date.', 'Falling prices mean you buy more for the same money.']),
       40: (6, ['Starting three streams at once', 'Counting likes instead of euros', 'Taking side hours from sleep or family'],
            ['One stream, one test, one number.', 'Track € per hour. Euros decide.', 'Family hours first, side hours second.']),
       46: (7, ['Letting automation run without ever checking it', 'Spending every freed-up hour on more work', 'Forgetting to raise your saving rate'],
            ['Check it monthly, change it yearly.', 'Name who gets each hour you take back.', 'Add 1–2 points with every raise.'])}
OPEN = {10: 1, 15: 2, 20: 3, 25: 4, 30: 5, 36: 6, 41: 7}


TIMES = {1: 'Week 1', 2: 'Weeks 1–4', 3: 'Months 2–5 · optional', 4: 'Months 3–9', 5: 'Months 8–12', 6: 'Months 6–12', 7: 'Month 12 onward'}
NAMES = ['Money mindset: your 9–5 is your wealth engine', 'Know your salary &amp; your numbers', 'Clear your debts', 'Build a safety net',
         'Build wealth with smart investing', 'Build multiple income streams', 'Repeat, automate &amp; buy back time']
CSS += '''
  .agenda{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px;}
  .ag{background:var(--paper);border:1px solid var(--line);border-top:3px solid var(--c,var(--turq));border-radius:12px;padding:8px 12px 6px;}
  .ag h4{margin:0;font:800 13.4px/1.3 var(--sans);color:var(--teal);display:flex;gap:8px;align-items:baseline;}
  .ag h4 span.n{flex:none;width:22px;height:22px;border-radius:50%;display:inline-grid;place-items:center;color:#fff;font-size:11.5px;background:var(--c,var(--turq));transform:translateY(5px);}
  .ag .tm{display:block;font:800 10.5px/1.2 var(--sans);letter-spacing:1px;text-transform:uppercase;color:var(--bord-dk);margin:2px 0 3px 30px;}
  .ag ol{list-style:none;margin:0;padding:0 0 0 30px;}
  .ag li{display:grid;grid-template-columns:20px 66px 1fr;gap:5px;font-size:11.2px;line-height:1.28;color:var(--body);padding:2px 0;border-top:1px dashed var(--line);}
  .ag li b{color:var(--teal);font-variant-numeric:tabular-nums;} .ag li i{font-style:normal;color:var(--mut);font-size:11px;text-transform:uppercase;letter-spacing:.5px;padding-top:1px;}
'''


def agenda(items):
    """items: list of (group, pageno, kind, title). group 0 = opening, 1..7 stages, 8 = closing."""
    cols = ['#1A9E9E', '#9E1B5E', '#245F46']
    cards = []
    for g in range(0, 9):
        rows = [x for x in items if x[0] == g]
        if not rows:
            continue
        li = ''.join(f'<li><b>{n:02d}</b><i>{k}</i><span>{t}</span></li>' for _, n, k, t in rows)
        if g == 0:
            head, tm, c = '<span class="n">★</span><span>Before you start</span>', 'Read once · about 30 minutes', '#134E4E'
        elif g == 8:
            head, tm, c = '<span class="n">🏁</span><span>Your year &amp; next steps</span>', 'Keep coming back', '#6B1440'
        else:
            head, tm, c = f'<span class="n">{g}</span><span>{NAMES[g - 1]}</span>', TIMES[g], cols[(g - 1) % 3]
        cards.append(f'<div class="ag" style="--c:{c}"><h4>{head}</h4><span class="tm">{tm}</span><ol>{li}</ol></div>')
    return ('  <p class="kick">Your agenda</p>\n  <h2 class="big">Every stage, page by page</h2>\n  <div class="rule"></div>\n'
            '  <p class="lead" style="margin:0">Every stage has the same parts: the steps, deep dives, a tool to fill in and a checklist that unlocks the next stage.</p>\n'
            '  <div class="agenda">' + ''.join(cards) + '</div>')

CSS += '''
  .page{isolation:isolate;}
  .page::before{content:"iCyber";position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-32deg);font:italic 800 210px/1 var(--serif);color:rgba(19,78,78,.05);pointer-events:none;z-index:-1;white-space:nowrap;}
  .page.cover::before{color:rgba(255,255,255,.035);}
'''
COPY = ('<p><b>Copyright.</b> © 2026 iCyber. All rights reserved. The Wealth Roadmap and TRUST Tracker Pro are licensed for the personal use of the purchaser only. '
        'Copying, sharing, reselling, redistributing or publishing them, in full or in part, is not permitted without my written permission.</p>'
        '<p><b>How this was made.</b> All ideas, the 7-stage structure, the KEEP and TRUST methods, the frameworks and the stories in these products are my own original work. '
        'Some text and design elements were created with the help of AI tools, then reviewed, edited and approved by me.</p>')
