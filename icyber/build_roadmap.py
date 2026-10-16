import pickle, re
D = '/tmp/claude-0/-home-user-terragoat/11c993cd-3a5f-5f3f-9b94-f763b4772daf/scratchpad/rm/'
head, S, SCRIPT = pickle.load(open(D + 'parts.pkl', 'rb'))
TP = 'TRUST Tracker Pro'

def rep(s, pairs):
    for a, b in pairs:
        assert a in s, ('MISSING', a[:70])
        s = s.replace(a, b)
    return s

def badge(s, old, new):
    return rep(s, [(old, new)])

FOOT = '<div class="pfoot"><span>The Wealth Roadmap · iCyber</span><span>00</span></div>'

def page(inner, cls=''):
    return f'<section class="page{(" " + cls) if cls else ""}">\n{inner}\n  {FOOT}\n</section>'

def head_stage(n, chips, title, pillar, lead):
    ch = ''.join(f'<span class="chip {c}">{t}</span>' for c, t in chips)
    return (f'  <div class="stagehead"><span class="badge">{n}</span>{ch}</div>\n'
            f'  <h2 class="stitle">{title}</h2>\n  <p class="pillar">{pillar}</p>\n'
            f'  <p class="lead" style="margin-top:14px">{lead}</p>')

def steps(items):
    return '  <ol class="steps">' + ''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in items) + '</ol>'

def foot_notes(heavy, tracker, quick=None):
    s = (f'  <div class="stagefoot"><div class="note heavy"><p class="nl">Heavy-week version</p><p>{heavy}</p></div>'
         f'<div class="note tracker"><p class="nl">In your {TP}</p><p>{tracker}</p></div></div>')
    if quick:
        s += f'\n  <div class="quickwin"><p class="nl">10-minute quick win</p><p>{quick}</p></div>'
    return s

def foot_notes1(heavy, quick):
    return (f'  <div class="stagefoot"><div class="note heavy"><p class="nl">Heavy-week version</p><p>{heavy}</p></div>'
            f'<div class="note tracker"><p class="nl">Your 15 minutes this week</p><p>Read the five laws on page 10, then fill in the hourly-value tool on page 12 with a pen.</p></div></div>'
            f'\n  <div class="quickwin"><p class="nl">10-minute quick win</p><p>{quick}</p></div>')

def checklist_page(n, title, done, tracker, unlock, reflect, extra=''):
    li = ''.join(f'<li>{d}</li>' for d in done)
    rf = ''.join(f'<li>{r}</li>' for r in reflect)
    return page(
        head_stage(f'Stage {n} · Checklist', [('lvl', 'Done when')], title,
                   'Tick every box before you move on. Slow is fine. Skipping is what costs money.',
                   'Each box is something you can see, not something you feel. When all of them are ticked, write today\'s date here: ________.') +
        f'\n  <ul class="checklist" style="margin:18px 0 0;max-width:none">{li}</ul>'
        f'\n  <div class="two"><div class="box"><div class="when">Write it down</div><ol class="tpl">{rf}</ol><div class="lines"></div></div>'
        + (f'<div class="box"><div class="when" style="color:var(--teal)">In your {TP}</div><p class="script">{tracker}</p>' if tracker else '<div class="box">')
        + f'<div class="when"{" style=\"margin-top:14px\"" if tracker else ""}>Next stage unlocks when</div><p class="script">{unlock}</p></div></div>' + extra)

pages = []

# ---------- OPENING ----------
cover = rep(S[0], [('<span><b>6</b> stages</span>', '<span><b>7</b> stages</span>'),
                   ('<span>+ TRUST Tracker</span>', f'<span>+ {TP}</span>'),
                   ('solo-preneur, daughter, creator', 'solo-preneur, creator')])
pages.append(cover)
L1 = rep(S[1], [("That's why I created the TRUST Sheet, and this roadmap that carries you beyond it.",
                         f"That's why I created the free TRUST Sheet, and then this roadmap and {TP}, which carry you far beyond it.")])
cut = L1.index('<p><b>I know that feeling.</b>')
pfoot = L1[L1.index('<div class="pfoot">'):]
pages.append(L1[:cut] + pfoot)
pages.append('<section class="page letter">\n  <p class="kick">My story</p>\n  <h2>Why I built <span class="nm">this roadmap</span></h2>\n  <div class="rule"></div>\n  ' + L1[cut:])
pages.append(rep(S[2], [("The TRUST Tracker (included) does the maths and shows which Freedom Level you've reached. Follow the stages in order: each one makes the next one safe.",
                         f"{TP} (included) does the maths, shows which Freedom Level you've reached and has a tab for every stage. Follow the 7 stages in order: each one makes the next one safe.")]))

pairs = [('1', 'Money mindset: your 9–5 is your wealth engine', 'U · Understand'),
         ('2', 'Know your salary &amp; your numbers', 'T · Track · R · Reclaim'),
         ('3', 'Clear your debts (optional)', 'U · Understand · S · Save'),
         ('4', 'Build a safety net', 'S · Save'),
         ('5', 'Build wealth with smart investing', 'Invest'),
         ('6', 'Build multiple income streams', 'Income Streams'),
         ('7', 'Repeat, automate &amp; buy back time', 'T · Time · Monthly Review')]
prow = ''.join(f'<tr><td>Stage {a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in pairs)
pages.append(page(f'''  <p class="kick">Before you start</p>
  <h2 class="big">How to use this roadmap</h2>
  <div class="rule"></div>
  <p class="lead">Every stage follows the same pattern, so you always know where you are. Read a stage once, do its steps over the following weeks, and only move on when its checklist is complete.</p>
  <div class="weeks" style="grid-template-columns:repeat(5,1fr)">
    <div><span class="m">Page 1</span><b>The stage</b><span>Goal, time frame and the steps, in order.</span></div>
    <div><span class="m">Pages 2–3</span><b>Deep dive</b><span>Why it matters, with numbers, charts and real examples.</span></div>
    <div><span class="m">Page 4</span><b>Your tool</b><span>A worksheet, script or template to use straight away.</span></div>
    <div><span class="m">Page 5</span><b>Checklist</b><span>“Done when” boxes and what unlocks the next stage.</span></div>
    <div><span class="m">Every stage</span><b>Tracker tab</b><span>The {TP} tab that does the maths for you.</span></div>
  </div>
  <div class="tablewrap"><table class="budget"><tr><th>Roadmap stage</th><th>What it is</th><th>{TP} tab</th></tr>{prow}</table></div>
  <div class="ifthen"><p class="nl">Three rules that make it work</p>
    <p><b>One stage at a time.</b> Stage 2 (your career) keeps running in the background, everything else goes in order.</p>
    <p><b>15 minutes a week beats one perfect weekend.</b> Book the slot now, and keep it even when it's only 2 minutes.</p>
    <p><b>The tracker does the maths.</b> You fill in the yellow cells, the KEEP dashboard tells you your level and your next step.</p>
  </div>'''))

journey = '''<div class="journey">
    <div class="jrow"><span class="n">1</span><div><b>Money mindset: your 9–5 is your wealth engine</b><small>The five laws of money, your real hourly value and why your salary is your biggest asset.</small></div><span class="tab">U · Understand</span></div>
    <div class="jrow"><span class="n">2</span><div><b>Know your salary &amp; your numbers</b><small>Track, Reclaim, Understand. What you really keep, where it leaks, and how to grow your pay.</small></div><span class="tab">T · R tabs</span></div>
    <div class="jrow"><span class="n">3</span><div><b>Clear your debts <span style="font-weight:400;color:var(--mut)">(optional)</span></b><small>A small starter buffer first, then the most expensive debt. No debt? Skip to Stage 4.</small></div><span class="tab">U · S tabs</span></div>
    <div class="jrow"><span class="n">4</span><div><b>Build a safety net</b><small>A full emergency fund of 3–6 months of needs, goal pots and an automated payday.</small></div><span class="tab">S · Save</span></div>
    <div class="jrow"><span class="n">5</span><div><b>Build wealth with smart investing</b><small>Compound growth, costs, risk and red flags. Only invest in what you understand.</small></div><span class="tab">Invest</span></div>
    <div class="jrow"><span class="n">6</span><div><b>Build multiple income streams</b><small>One stream, one 90-day test, built in the hours you can truly protect.</small></div><span class="tab">Income Streams</span></div>
    <div class="jrow end"><span class="n">7</span><div><b>Repeat, automate &amp; buy back time</b><small>A system that runs on its own and hours that go back to your family.</small></div><span class="tab">T · Time</span></div>
  </div>'''
mp = S[4]
mp = re.sub(r'<div class="journey">.*?</div>\s*</div>\s*(?=<p style)', journey + '\n  ', mp, flags=re.S)
mp = rep(mp, [('Six stages from “where did it all go?” to real choices', 'Seven stages from “where did it all go?” to real choices'),
              ('(page 07)', '(page 07)')])
assert mp.count('class="jrow') == 7, mp.count('class="jrow')
pages.append(mp)
pages.append(rep(S[5], [('<b>Work on:</b> Stage 1.</p>', '<b>Work on:</b> Stages 1–2.</p>'),
                        ('<b>Work on:</b> starter buffer.', '<b>Work on:</b> Stage 3, starter buffer.'),
                        ('<b>Work on:</b> debt.', '<b>Work on:</b> Stage 3, debt.'),
                        ('<b>Work on:</b> full fund.', '<b>Work on:</b> Stage 4, full fund.'),
                        ('<b>Work on:</b> investing and one stream.', '<b>Work on:</b> Stages 5–6, investing and one stream.'),
                        ('<b>Work on:</b> time.', '<b>Work on:</b> Stage 7, time.'),
                        ('Your TRUST Tracker works out', f'Your {TP} works out')]))
pages.append(rep(S[6], [('<tr><td>Stages 1–2</td><td>15 min a week plus one 2-hour setup session. No extra time beyond that.</td></tr>',
                         '<tr><td>Stages 1–2</td><td>15 min a week plus one 2-hour setup session, and 5 minutes on Fridays for your win file.</td></tr>'),
                        ('<tr><td>Stages 3–4</td><td>1 hour a week: learning, preparing your salary review, reading about investing basics.</td></tr>',
                         '<tr><td>Stages 3–5</td><td>15–30 min a week for transfers and debt, plus 1 hour a week of learning about investing.</td></tr>'),
                        ('<tr><td>Stages 5–6</td><td>2–4 protected hours a week, in two blocks. Never taken from sleep or family time first.</td></tr>',
                         '<tr><td>Stages 6–7</td><td>2–4 protected hours a week, in two blocks. Never taken from sleep or family time first.</td></tr>')]))
pages.append(rep(S[7], [('You\'ll write your own if-then rules on page 12.', 'You\'ll write your own if-then rules in Stage 4.')]))

# ---------- STAGE 1 · MONEY MINDSET ----------
pages.append(page(head_stage('Stage 1', [('time', 'Week 1'), ('lvl', 'Foundation')],
    'Money mindset: your 9–5 is your wealth engine', 'Pillar 1 · Career &amp; Pillar 2 · Financial literacy',
    'Before you track a single euro, change how you look at the one you already earn. Your salary isn\'t only what pays the bills. It\'s the engine that can fund your safety, your investments and, later, your time. This stage takes about two hours, spread over one week.') + '\n' +
    steps([('Write your money why', 'One sentence: who do you want more time and security for, and why? Put it where you\'ll see it every week.'),
           ('Name your money story', 'What did you learn about money growing up? Write down one belief that still drives your choices.'),
           ('Learn the five laws', 'Read page 10 once. Every stage of this roadmap puts one of these laws into practice.'),
           ('Swap one old thought', 'Pick one “old thinking” line from page 10 and write its wealth-mindset version on a sticky note.'),
           ('Find your real hourly value', 'Net pay divided by your real hours, including overtime and commute. The tool on page 12 shows you how.'),
           ('See your salary as an asset', 'Multiply your yearly net pay by the years you\'ll still work. That number is the engine you\'re protecting.'),
           ('Decide what a raise is for', 'Before the next one arrives, decide where it goes: buffer, debt, investing or time. Not your lifestyle first.'),
           ('Book your weekly slot', 'A recurring 15-minute appointment with yourself. Same day, same time, every week.')]) + '\n' +
    foot_notes1('Write your money why in one sentence and stop there. That sentence is enough to carry you into Stage 2.',
               'Open your banking app and look at your last payslip. Write down your exact net pay. That\'s your engine\'s output.')))

mind = rep(S[3], [('<p class="kick">Before the numbers</p>', '<div class="stagehead"><span class="badge">Stage 1 · Deep dive</span><span class="chip lvl">Mindset</span></div>\n  <p class="kick" style="margin-top:14px">Before the numbers</p>'),
                  ('<small>Stage 1</small>', '<small>Stage 2</small>'),
                  ('<small>Stage 2</small></span></div>\n    <div><b>4</b>', '<small>Stages 3–4</small></span></div>\n    <div><b>4</b>'),
                  ('<small>Stages 3–5</small>', '<small>Stages 5–6</small>'),
                  ('<small>Page 16</small>', '<small>Page 30</small>')])
pages.append(mind)

eng = S[13]
eng = rep(eng, [('<span class="badge">Stage 3 · Deep dive</span><span class="chip lvl">Career capital</span>', '<span class="badge">Stage 1 · Deep dive</span><span class="chip lvl">Your engine</span>')])
eng = re.sub(r'<div class="two">.*?</div>\s*</div>\s*(?=<p class="cnote")', '''<div class="two">
    <div class="box"><div class="when">Your salary is an asset</div><p class="script">€2,500 net a month × 12 × 30 working years = <b>€900,000</b>. For most people, their earning power is worth more than any house or investment they'll ever own. That's why Stage 2 grows it and Stage 4 protects it.</p></div>
    <div class="box"><div class="when">Protect the engine</div><ol class="tpl"><li>Your health and sleep: no plan survives burnout</li><li>One skill a year your market pays for</li><li>Five people who'd recommend you</li><li>An updated CV, even when you're happy</li></ol></div>
  </div>
  ''', eng, flags=re.S)
pages.append(eng)

pages.append(page(head_stage('Stage 1 · Your tool', [('lvl', 'Worksheet')], 'Your real hourly value &amp; your money story',
    'Two numbers and three sentences that change every decision after this',
    'Most people only know their salary. Almost nobody knows what one hour of their life is really paid. Once you do, every purchase, every overtime evening and every side project looks different.') + '''
  <div class="formula"><p class="nl">Your real hourly value</p>
    <p><b>Real hours a month</b> = (contract hours + unpaid overtime + commute) × 52 ÷ 12 <span>e.g. (39 + 4 + 5) × 52 ÷ 12 = 208 hours</span></p>
    <p><b>Real hourly value</b> = net pay a month ÷ real hours a month <span>e.g. €2,500 ÷ 208 = €12.02 an hour</span></p>
    <p><b>Keep your first hour</b> = real hourly value × workdays a month <span>e.g. €12.02 × 21 = about €252 a month, paid to your future first</span></p>
  </div>
  <div class="two">
    <div class="box"><div class="when">The real cost of a purchase</div><p class="script">€2,500 net ÷ 208 real hours a month = <b>€12 per hour</b>. A €120 pair of shoes costs you <b>10 hours</b> of your life. Before any purchase over €50, ask: is it worth those hours?</p></div>
    <div class="box"><div class="when">Mine, filled in</div><p class="script">Net pay: €______ ÷ real hours: ______ = <b>€______ an hour</b><br>First hour a month: €______<br>The purchase I'll think twice about: ____________</p></div>
  </div>
  <div class="box" style="margin-top:16px"><div class="when">Your money story · answer honestly</div><ol class="tpl">
    <li>Growing up, money was mostly talked about as… ____________________________</li>
    <li>The belief that still holds me back is… ____________________________</li>
    <li>The wealth-mindset version I'll practise instead is… ____________________________</li>
    <li>My money why: I want more time and security for ________ because ________</li></ol></div>'''))

pages.append(checklist_page(1, 'Money mindset · done when',
    ['I wrote my money why in one sentence and put it where I see it.', 'I know my real hourly value and my “first hour” amount.', 'I read the five laws of money and picked one old thought to replace.',
     'I know what my salary is worth over my working life.', 'I decided where my next raise goes before it arrives.', 'My 15-minute weekly money check is in my calendar.'],
    None,
    "You can say in one sentence why you're doing this, and your weekly slot is booked.",
    ['The one sentence I want to remember from this stage…', 'The day and time of my weekly money check…', 'One person I\'ll tell about my plan…']))

# ---------- STAGE 2 · KNOW YOUR SALARY & NUMBERS ----------
s2 = rep(S[8], [('<span class="badge">Stage 1</span><span class="chip time">Weeks 1–4</span><span class="chip lvl">Goal: Level 1</span>', '<span class="badge">Stage 2</span><span class="chip time">Weeks 1–4</span><span class="chip lvl">Goal: Level 1</span>'),
                ('<h2 class="stitle">See your money</h2>', '<h2 class="stitle">Know your salary &amp; your numbers</h2>'),
                ('<p class="nl">In your tracker</p>', f'<p class="nl">In your {TP}</p>')])
pages.append(s2)
snap = rep(S[9], [('<span class="badge">Stage 1 · Deep dive</span>', '<span class="badge">Stage 2 · Deep dive</span>'),
                  ('<p class="pillar">What a finished Stage 1 looks like</p>', '<p class="pillar">What a finished Stage 2 looks like</p>'),
                  ('Here is a real-looking example from the TRUST Tracker,', f'Here is a real-looking example from {TP},'),
                  ('<div class="box"><div class="when">The real cost of a purchase</div><p class="script">€2,500 net ÷ 208 real hours a month = <b>€12 per hour</b>. A €120 pair of shoes costs you <b>10 hours</b> of your life. Before any purchase over €50, ask: is it worth those hours?</p></div>',
                   '<div class="box"><div class="when">Read your payslip once</div><ol class="tpl"><li>Gross pay: what your contract says</li><li>Tax and social contributions: what leaves before you see it</li><li>Pension or employer benefits: part of your pay, not a cost</li><li>Net pay: the number your plan is built on</li></ol></div>')])
pages.append(snap)
car = rep(S[12], [('<span class="badge">Stage 3</span><span class="chip time">From month 2, ongoing</span><span class="chip lvl">Runs alongside every level</span>', '<span class="badge">Stage 2 · Your salary</span><span class="chip time">From week 2, ongoing</span><span class="chip lvl">Runs alongside every stage</span>'),
                  ('<h2 class="stitle">Grow your career capital</h2>', '<h2 class="stitle">Grow the number at the top</h2>'),
                  ('<p class="nl">In your tracker</p>', f'<p class="nl">In your {TP}</p>')])
pages.append(car)
pages.append(page(head_stage('Stage 2 · Your tool', [('lvl', 'Scripts &amp; templates')], 'Your win file &amp; salary conversation',
    'Prepare once, use every year',
    'A raise is rarely given for working hard. It is given for results someone can see and repeat. These templates turn your everyday work into evidence, and your evidence into a calm, clear conversation.') + '''
  <div class="two">
    <div class="box"><div class="when">Win file template · every Friday</div><ol class="tpl"><li>What I delivered this week</li><li>The number behind it (time, money, risk reduced)</li><li>Who benefited</li><li>Praise or feedback I received</li><li>What I learned</li></ol></div>
    <div class="box"><div class="when">Salary conversation · structure</div><ol class="tpl"><li>Open with your results, not your needs</li><li>Show three wins with numbers</li><li>Name your market range</li><li>Ask clearly: “I'd like to move to €X.”</li><li>If budget is tight, ask for flexibility, training or a date to revisit</li></ol></div>
  </div>
  <div class="box" style="margin-top:16px"><div class="when">Raise prep sheet · fill in before you book the meeting</div><ol class="tpl">
    <li>My market range for this role and city: €______ to €______</li>
    <li>My three strongest wins this year, each with a number: ______ · ______ · ______</li>
    <li>What I'll ask for: €______, or instead: remote days / training / certification / fewer hours</li>
    <li>The date I'll ask (6–8 weeks before budgets are set): ______</li>
    <li>Where the raise goes the day it lands: ______% buffer or debt · ______% investing · ______% time</li></ol></div>
  <div class="ifthen"><p class="nl">If they say “not now”</p>
    <p>Ask: “What would I need to show by when, for this to be a yes?” Write it down and agree a date.</p>
    <p>Ask for what costs them less: a training budget, a title, flexible hours or one remote day.</p>
    <p>Add the answer to your win file. Next year's conversation starts today.</p></div>'''))
pages.append(checklist_page(2, 'Know your salary &amp; your numbers · done when',
    ['Every euro in and out for one normal month is in T · Track.', 'I know my baseline (needs) and my keep rate.', 'I cancelled or renegotiated at least one cost in R · Reclaim.',
     'Reclaimed money moves on payday by standing order.', 'My win file has its first three wins with numbers.', 'I know my market range and the date I\'ll ask for my review.'],
    'T · Track shows your keep rate, R · Reclaim your reclaimable euros, Income Streams logs any raise as “Career”. The KEEP dashboard should now show Level 1 or higher.',
    'What you keep is €0 or more every month (Level 1 · Stable).',
    ['My keep rate today: ______%. My goal in 6 months: ______%', 'The leak I cut and what it saves a year…', 'My review date and my ask…']))

# ---------- STAGE 3 · CLEAR YOUR DEBTS ----------
pages.append(page(head_stage('Stage 3', [('time', 'Months 2–5'), ('lvl', 'Goal: Level 2 → 3'), ('time', 'Optional')],
    'Clear your debts', 'Pillar 2 · TRUST: Understand &amp; Save',
    'This stage is optional: if you have no consumer debt, save your starter buffer and go straight to Stage 4. If you do, your money can still grow while you pay it off, just more slowly. Expensive debt is a leak that works against you every single day, so stopping it is the fastest “return” you\'ll ever earn.') + '\n' +
    steps([('Save a starter buffer first', 'One month of needs in a separate account. Without it, the first broken washing machine goes straight back on the card.'),
           ('List every debt', 'In U · Understand: balance, interest rate, minimum payment. The tracker shows what each one costs you a month.'),
           ('Pay every minimum, always', 'Missed payments add fees and damage your credit. Automate the minimums on payday.'),
           ('Attack Priority 1', 'Every extra euro goes to the highest interest rate. The tracker ranks your debts for you.'),
           ('Stop new debt', 'Remove saved cards from shopping sites. Turn off buy-now-pay-later. Your buffer is for emergencies now.'),
           ('Call your lender', 'Ask for a lower rate or a payment plan. The script on page 22 helps. One call can save hundreds.'),
           ('Roll payments forward', 'When one debt is gone, its whole payment moves to the next. Don\'t let it fade back into spending.'),
           ('Celebrate Level 3', 'Debt-free is a huge milestone. Mark the date. Do something small and free with someone you love.')]) + '\n' +
    foot_notes('Keep the automatic minimums and your extra payment running. Do nothing else. Automation keeps going when you can\'t.',
               'U · Understand ranks your debts, shows months to clear and the interest you pay a year. S · Save tracks your starter buffer.',
               'Look at “Interest you pay / year” on the KEEP dashboard. Write that number on a sticky note. That\'s what this stage wins back.')))
debt = S[11]
debt = rep(debt, [('<span class="badge">Stage 2 · Deep dive</span><span class="chip lvl">Debt &amp; automation</span>', '<span class="badge">Stage 3 · Deep dive</span><span class="chip lvl">Debt maths</span>'),
                  ('<p class="pillar">Pay off debt faster, then let automation do the work</p>', '<p class="pillar">Why a little more each month changes everything</p>')])
debt = debt[:debt.index('<div class="viz" data-id="automation">')] + '''<div class="viz"><p class="nl">What one debt-free year gives back · example</p><div class="hbars"><div class="hb"><span class="hl">Interest paid a year now</span><span class="track"><i class="fee" style="width:100%"></i></span><b>€299</b></div><div class="hb"><span class="hl">Minimum + extra freed up a month</span><span class="track"><i class="" style="width:40%"></i></span><b>€100</b></div><div class="hb"><span class="hl">Freed up a year, for your safety net</span><span class="track"><i class="" style="width:100%"></i></span><b>€1,200</b></div></div><small>Credit card €1,500 at 19.9%, from the tracker example. Once it's gone, the €100 a month you paid moves straight to Stage 4.</small></div>
  ''' + FOOT + '\n</section>'
pages.append(debt)
pages.append(page(head_stage('Stage 3 · Deep dive', [('lvl', 'Know your debt')], 'Not all debt is the same',
    'Which debt to clear first, and which can wait',
    "In my 20s I took out loans for my study fees and made financial decisions I'd make very differently today. Paying off €30,000 taught me one thing above all: the interest rate decides the order, not the size of the balance or how guilty a debt makes you feel.") + '''
  <div class="tablewrap"><table class="budget"><tr><th>Type of debt</th><th>Typical cost</th><th>What to do</th></tr>
    <tr><td>Overdraft</td><td>Often 10–15%+ a year</td><td>Priority. Clear it first and keep a buffer so you don't slide back.</td></tr>
    <tr><td>Credit card balance</td><td>Often 15–20%+ a year</td><td>Priority. Pay more than the minimum, highest rate first.</td></tr>
    <tr><td>Buy now, pay later</td><td>0% until a payment is missed</td><td>Stop new ones. Late fees and stacking several make it expensive.</td></tr>
    <tr><td>Car or consumer loan</td><td>Mid-range</td><td>Pay as agreed. Extra payments once cards are gone, if no early-repayment fee.</td></tr>
    <tr><td>Student loan</td><td>Often low, sometimes tied to income</td><td>Pay as agreed. Rarely worth rushing before your safety net.</td></tr>
    <tr><td>Mortgage</td><td>Usually the lowest</td><td>Not part of this stage. Pay as agreed.</td></tr></table></div>
  <p class="cnote">Rates differ by country, lender and contract. Check the effective yearly rate on your own statements.</p>
  <div class="two">
    <div class="box"><div class="when">Why this stage is optional</div><p class="script">If your only debt is a low-rate student loan or a mortgage, you don't need to clear it before you move on. Save your starter buffer and go to Stage 4. Paying off expensive debt is the priority. Cheap debt can be paid as agreed while your money grows elsewhere.</p></div>
    <div class="box heavy"><div class="when">No shame, only a plan</div><p class="script">Debt is a number, not a judgement of who you are. Most people with debt got there through study, illness, caring for someone, or simply not being taught. You were never meant to figure this out alone.</p></div>
  </div>
  <div class="ifthen red"><p class="nl">Ask for help early if…</p><p>You can't pay the minimums for two months in a row.</p><p>You're using one card to pay another.</p><p>Collection letters are arriving. Free, regulated debt advice exists in most countries (in Germany: Schuldnerberatung).</p></div>'''))
pages.append(page(head_stage('Stage 3 · Your tool', [('lvl', 'Worksheet &amp; script')], 'Your debt payoff plan',
    'One page that shows the way out',
    'Write your debts down in order of interest rate. Seeing the finish line is half the work. Copy these numbers into U · Understand and the tracker will estimate how many months each one takes.') + '''
  <div class="tablewrap"><table class="budget fill"><tr><th>Priority</th><th>Debt</th><th>Balance €</th><th>Interest %</th><th>Minimum €</th><th>Extra €</th><th>Paid off by</th></tr>
    <tr><td>1</td><td>&nbsp;</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>&nbsp;</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>&nbsp;</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>&nbsp;</td><td></td><td></td><td></td><td></td><td></td></tr></table></div>
  <div class="two">
    <div class="box"><div class="when">Script · call your lender</div><p class="script">“Hi, I've been a customer for [X] years and I'm working on paying off my balance faster. Is there a lower interest rate or a repayment plan you can offer me? Other banks offer [Y]%. What can you do for me today?” Write down the name of the person and what they offered.</p></div>
    <div class="box"><div class="when">When a debt is gone</div><ol class="tpl"><li>Close the card or lower the limit</li><li>Move its whole payment to the next debt the same day</li><li>Write the date on this page</li><li>Tell someone. It's a real win</li></ol></div>
  </div>
'''))
pages.append(checklist_page(3, 'Clear your debts · done when',
    ['My starter buffer of one month of needs is saved in a separate account.', 'Every debt is listed with its rate, and I know my Priority 1.', 'All minimums run automatically on payday.',
     'I have no new consumer debt and buy-now-pay-later is switched off.', 'I called at least one lender or provider.', 'Consumer debt (cards, overdraft, BNPL) is €0, or I skipped this stage because I had none.'],
    'U · Understand: total debt and interest per year at €0. S · Save: starter buffer done. The KEEP dashboard shows Level 3 · Debt-free.',
    'Consumer debt is gone (Level 3), or you had none and your starter buffer is full.',
    ['The date I became debt-free…', 'What my old debt payment pays for now…', 'How I\'ll celebrate, for free…']))

# ---------- STAGE 4 · SAFETY NET ----------
pages.append(page(head_stage('Stage 4', [('time', 'Months 3–9'), ('lvl', 'Goal: Level 4')],
    'Build a safety net', 'Pillar 2 · TRUST: Save',
    'When others rely on you, a surprise bill doesn\'t only cost money. It costs sleep. A full emergency fund turns a job loss, a care emergency or a broken car from a crisis into a problem you can handle.') + '\n' +
    steps([('Choose your number of months', '3 months of needs, or 6 if you\'re a carer, the only earner or self-employed. Set it in S · Save.'),
           ('Keep it separate', 'A savings account that is easy to reach in a day or two, but not linked to your everyday card.'),
           ('Automate the transfer', 'A fixed amount on payday, before anything else. Your old debt payment is perfect for this.'),
           ('Create goal pots', 'Christmas, birthdays, car repairs, care costs: predictable “surprises” get their own monthly amount.'),
           ('Write your emergency rule', 'Decide now what counts as an emergency, so you don\'t have to decide in a hard moment.'),
           ('Check your insurance', 'Liability, health and, if people depend on you, income protection or life cover. The cheapest safety net is often a policy.'),
           ('Refill before anything else', 'If you use the fund, refilling it comes before investing or extra spending.'),
           ('Mark Level 4', 'A full fund is real security. Note the date: from here, your money can start working for you.')]) + '\n' +
    foot_notes('Leave the automatic transfer running. Even €25 a month keeps the habit alive.',
               'S · Save shows your target, progress and months to go. The KEEP dashboard turns to Level 4 · Secure when the fund is full.',
               'Rename your savings account to “Safety net – do not touch”. A name changes how you treat money.')))
pages.append(page(head_stage('Stage 4 · Deep dive', [('lvl', 'How big?')], 'How big should your safety net be?',
    'Enough to sleep well, not so much that it stops your money growing',
    'Your emergency fund is insurance, not an investment. It should be boring, separate and easy to reach. Here\'s how to size it for your life, and how long it takes.') + '''
  <div class="tablewrap"><table class="budget"><tr><th>Your situation</th><th>Months of needs</th><th>Example at €1,740 needs</th></tr>
    <tr><td>Stable job, no one depends on you</td><td>3 months</td><td>€5,220</td></tr>
    <tr><td>Carer, parent or single earner</td><td>6 months</td><td>€10,440</td></tr>
    <tr><td>Self-employed or irregular income</td><td>6 months or more</td><td>€10,440+</td></tr></table></div>
  <div class="viz"><p class="nl">3-month emergency fund (€5,220) · €1,200 already saved · months to go</p><div class="hbars"><div class="hb"><span class="hl">€150 a month</span><span class="track"><i class="" style="width:100.0%"></i></span><b>27 months</b></div><div class="hb"><span class="hl">€250 a month</span><span class="track"><i class="" style="width:63.0%"></i></span><b>17 months</b></div><div class="hb"><span class="hl">€400 a month</span><span class="track"><i class="" style="width:40.7%"></i></span><b>11 months</b></div></div><small>Adding the €100 freed up from debt in Stage 3 turns €150 into €250 a month, and saves 10 months.</small></div>
  <div class="two">
    <div class="box"><div class="when" style="color:var(--teal)">It is an emergency if…</div><ol class="tpl"><li>You lose income</li><li>Health or care needs you didn't plan for</li><li>A repair you need to work or live safely</li></ol></div>
    <div class="box heavy"><div class="when">It is not an emergency if…</div><ol class="tpl"><li>It happens every year (that's a goal pot)</li><li>It's on sale</li><li>It can wait 30 days</li></ol></div>
  </div>'''))
auto = S[11]
a0 = auto.index('<div class="viz" data-id="automation">'); a1 = auto.index('<div class="viz"><p class="nl">3-month emergency fund')
pages.append(page(head_stage('Stage 4 · Deep dive', [('lvl', 'Automation')], 'Your automated payday',
    'Set it up once, and let it run while you live your life',
    'Willpower runs out at the end of a long day. Automation doesn\'t. When your transfers happen on payday, before you can spend, saving stops being a decision you have to make every month.') + '\n  ' + auto[a0:a1].strip() + '''
  <div class="viz"><p class="nl">Goal pots · predictable “surprises”</p><div class="hbars"><div class="hb"><span class="hl">Christmas &amp; birthdays</span><span class="track"><i class="" style="width:50%"></i></span><b>€50 a month</b></div><div class="hb"><span class="hl">Care costs &amp; time off</span><span class="track"><i class="" style="width:75%"></i></span><b>€75 a month</b></div><div class="hb"><span class="hl">Holiday with family</span><span class="track"><i class="" style="width:100%"></i></span><b>€100 a month</b></div></div><small>From the S · Save example. When the bill arrives, the money is already there.</small></div>'''))
pages.append(page(head_stage('Stage 4 · Your tool', [('lvl', 'Calculator')], 'Your emergency buffer calculator',
    'Five lines, one number, one date',
    'Fill this in with the numbers from T · Track and S · Save. When you\'re done, you know exactly how big your safety net needs to be and the month it will be full.') + '''
  <div class="formula"><p class="nl">Fill in</p>
    <p><b>1 · My monthly needs (baseline)</b> €__________ <span>From T · Track: rent, bills, food, transport, care, debt minimums</span></p>
    <p><b>2 · Months of safety I want</b> ______ <span>3, or 6 if you're a carer, the only earner or self-employed</span></p>
    <p><b>3 · My target</b> = line 1 × line 2 = €__________</p>
    <p><b>4 · Saved so far</b> €__________ <b style="margin-left:16px">5 · Monthly transfer</b> €__________</p>
    <p><b>Months to go</b> = (line 3 − line 4) ÷ line 5 = ______ <span>My safety net is full in: ______________ (month and year)</span></p>
  </div>
  <div class="ifthen"><p class="nl">Your safety-net rules</p>
    <p><b>If</b> I use the fund, <b>then</b> refilling it comes before investing or anything new.</p>
    <p><b>If</b> I get a bonus or tax refund, <b>then</b> half goes to the fund until it's full.</p>
    <p><b>If</b> something is an annual cost, <b>then</b> it gets a goal pot, not the emergency fund.</p>
  </div>
  <div class="box" style="margin-top:16px"><div class="when">Where I keep it</div><p class="script">Bank: ______________ · Account name: ______________ · Linked to my everyday card: <b>no</b></p></div>'''))
pages.append(checklist_page(4, 'Build a safety net · done when',
    ['I chose 3 or 6 months and know my target in euros.', 'My fund is in a separate account, not linked to my card.', 'A fixed transfer runs on payday.',
     'My predictable costs have their own goal pots.', 'I wrote down what counts as an emergency.', 'My full emergency fund is 100% saved.'],
    'S · Save: progress at 100% and “Done ✓”. The KEEP dashboard shows Level 4 · Secure, and the Invest tab says the first check is “Yes ✓”.',
    'Your full fund is in place (Level 4 · Secure). Now your money can start working for you.',
    ['The month my fund was full…', 'My emergency rule in one sentence…', 'What feels different now…']))

# ---------- STAGE 5 · INVESTING ----------
s5 = rep(S[14], [('<span class="badge">Stage 4</span><span class="chip time">Months 5–9</span><span class="chip lvl">Goal: Level 4</span>', '<span class="badge">Stage 5</span><span class="chip time">Months 8–12</span><span class="chip lvl">Money that works for you</span>'),
                 ('<h2 class="stitle">Secure it and start building wealth</h2>', '<h2 class="stitle">Build wealth with smart investing</h2>'),
                 ('First, complete your emergency fund. Then begin to learn how long-term investing really works.', 'Your safety net is full. Now you can learn how long-term investing really works.'),
                 ('<li><b>Finish your full fund</b><span>3 months of needs, or 6 if you\'re a carer, a single earner or self-employed. Set the months in S · Save.</span></li>', '<li><b>Confirm your safety net</b><span>Full emergency fund and no consumer debt. The Invest tab checks both for you.</span></li>'),
                 ('<p class="nl">In your tracker</p><p>S · Save: full fund progress and months to go. The KEEP dashboard turns to Level 4 when it\'s full.</p>', f'<p class="nl">In your {TP}</p><p>Invest: the readiness check, what time and fees could do, and what you already invest each month.</p>')])
pages.append(s5)
pages.append(rep(S[15], [('<span class="badge">Deep dive</span><span class="chip lvl">Stage 4</span>', '<span class="badge">Stage 5 · Deep dive</span><span class="chip lvl">Compound growth</span>')]) + '\n' + SCRIPT)
pages.append(rep(S[16], [('<span class="badge">Deep dive</span><span class="chip lvl">Stage 4</span>', '<span class="badge">Stage 5 · Deep dive</span><span class="chip lvl">Start now</span>'),
                         ('Open the TRUST Tracker and fill in your net salary on T · Track.', f'Open {TP} and fill in the Invest tab with €100 a month and 25 years.')]))
pages.append(rep(S[17], [('<span class="badge">Stage 4 · Deep dive</span>', '<span class="badge">Stage 5 · Deep dive</span>')]))
pages.append(page(head_stage('Stage 5 · Your tool', [('lvl', 'Before you buy')], 'Only invest in what you understand',
    'The two-sentence test and the words you need',
    'In my 20s I traded without really understanding what I was doing, and I paid for it. Today I use one simple rule: if I can\'t explain an investment to a friend in two sentences, I don\'t buy it. These are the words you need to pass that test.') + '''
  <div class="tablewrap"><table class="budget"><tr><th>Word</th><th>What it means, in plain language</th></tr>
    <tr><td>Diversification</td><td>Spreading money across many companies and countries, so one failure can't sink you.</td></tr>
    <tr><td>Index fund</td><td>A fund that follows a whole market instead of picking winners. Usually low cost.</td></tr>
    <tr><td>Costs (TER)</td><td>What you pay every year, in percent. Small numbers, huge effect over decades.</td></tr>
    <tr><td>Time horizon</td><td>How long until you need the money. Under 5 years: not for the stock market.</td></tr>
    <tr><td>Volatility</td><td>How much the value goes up and down. Normal, and why you need a long horizon.</td></tr>
    <tr><td>Risk you can sleep with</td><td>The drop you could watch without selling. Your nerves are part of the plan.</td></tr></table></div>
  <div class="formula"><p class="nl">The two-sentence test · fill in before you buy</p>
    <p><b>1 · What it is:</b> ______________________________________________</p>
    <p><b>2 · How it makes money, and how it could lose money:</b> ______________________________</p>
    <p><b>Costs a year:</b> ______% · <b>Regulated provider:</b> yes / no · <b>I need this money in:</b> ______ years</p>
  </div>
  <p class="cnote">This page explains concepts. It doesn't recommend any product, fund or provider. For your own situation, speak to a regulated, independent adviser.</p>'''))
pages.append(checklist_page(5, 'Build wealth with smart investing · done when',
    ['The Invest tab readiness check shows “Ready ✓”.', 'I checked what my employer offers (pension, contributions).', 'I can explain what I invest in, in two sentences.',
     'I know the yearly costs, in percent, of everything I hold.', 'A fixed monthly amount runs on payday.', 'I only use regulated providers, and I know the scam red flags.'],
    'Invest: readiness check, monthly amount and value so far. The KEEP dashboard shows “Invested / month”.',
    'Your investing runs on its own, and you understand what you own. Then you\'re ready to add a second income.',
    ['What I invest in, in two sentences…', 'My monthly amount and the date I review it each year…', 'The red flag I\'ll never ignore…']))

# ---------- STAGE 6 · INCOME STREAMS ----------
s6 = rep(S[18], [('<span class="badge">Stage 5</span><span class="chip time">Months 6–12</span><span class="chip lvl">Goal: Level 5</span>', '<span class="badge">Stage 6</span><span class="chip time">Months 6–12</span><span class="chip lvl">Goal: Level 5</span>'),
                 ('<h2 class="stitle">Add one income stream</h2>', '<h2 class="stitle">Build multiple income streams</h2>'),
                 ('<p class="nl">In your tracker</p>', f'<p class="nl">In your {TP}</p>')])
pages.append(s6)
pages.append(rep(S[19], [('<span class="badge">Stage 5 · Deep dive</span>', '<span class="badge">Stage 6 · Deep dive</span>'),
                         ('Job and digital product values come from the TRUST Tracker example;', f'Job and digital product values come from the {TP} example;')]))
pages.append(page(head_stage('Stage 6 · Deep dive', [('lvl', 'Your offer')], 'One offer on one page',
    'Clear beats clever, and one beats five',
    'Most side income fails before the first sale, because the offer is vague. Before you build anything, write it down on one page. If you can\'t fill it in, you\'re not ready to sell yet, and that\'s useful to know.') + '''
  <div class="formula"><p class="nl">Your one-page offer</p>
    <p><b>Who it's for:</b> ______________________________ <span>One kind of person, not “everyone”</span></p>
    <p><b>The problem it solves:</b> ______________________________ <span>In their words, not yours</span></p>
    <p><b>What they get:</b> ______________________________ <span>A result, not a list of features</span></p>
    <p><b>Price:</b> €________ <span>Start simple. You can raise it after the first 10 buyers</span></p>
    <p><b>Where they'll find it:</b> ______________________________ <span>One channel where they already are</span></p>
  </div>
  <div class="two">
    <div class="box"><div class="when">Rules first</div><ol class="tpl"><li>Check your employment contract on side work and conflicts of interest</li><li>Find out how to register and pay tax on side income where you live</li><li>Keep 30% of side income aside for tax until you know your real rate</li></ol></div>
    <div class="box"><div class="when">€ per hour, honestly</div><p class="script">If a stream pays less per hour than your job, it must buy you something else: a skill, an asset that keeps selling, or a path to more time later. If it buys nothing, stop it without guilt.</p></div>
  </div>'''))
wk = ''.join(f'<tr><td>Week {i}</td><td></td><td></td><td></td><td></td></tr>' for i in range(1, 14))
pages.append(page(head_stage('Stage 6 · Your tool', [('lvl', 'Tracker sheet')], 'Your 90-day test, week by week',
    'Print it, stick it on the fridge, fill in one row a week',
    'Euros, not likes. Write down what you did and what came back. At week 13, the numbers make the keep, change or stop decision for you.') + f'''
  <div class="tablewrap"><table class="budget fill"><tr><th>Week</th><th>Hours</th><th>What I did</th><th>People reached</th><th>€ earned</th></tr>{wk}</table></div>
  <div class="formula"><p class="nl">Day 90</p><p><b>Total €</b> ______ ÷ <b>total hours</b> ______ = <b>€ per hour</b> ______ <span>Compare with your real hourly value from Stage 1</span></p><p><b>My decision:</b> keep · change · stop <span>Log it in Income Streams</span></p></div>'''))
pages.append(checklist_page(6, 'Build multiple income streams · done when',
    ['I checked my contract and the tax rules for side income.', 'I picked one stream that fits my skills and hours.', 'Two weekly blocks are protected, not taken from sleep or family.',
     'My one-page offer is written.', 'I finished a 90-day test and made a keep, change or stop decision.', 'Side income has a plan: tax, investing and time.'],
    'Income Streams: status, hours, € per hour and the share of your needs covered. Level 5 · Flexible lights up at 25%.',
    'One stream has a clear result, and extra income covers part of your needs (Level 5 · Flexible at 25%).',
    ['My stream and my decision at day 90…', 'My € per hour vs my job…', 'The next small step…']))

# ---------- STAGE 7 · REPEAT, AUTOMATE & BUY BACK TIME ----------
s7 = rep(S[20], [('<span class="badge">Stage 6</span><span class="chip time">Month 12 onward</span><span class="chip lvl">Goal: Level 6</span>', '<span class="badge">Stage 7</span><span class="chip time">Month 12 onward</span><span class="chip lvl">Goal: Level 6</span>'),
                 ('<h2 class="stitle">Buy back your time</h2>', '<h2 class="stitle">Repeat, automate &amp; buy back time</h2>'),
                 ('Your Stage 3 win file is your evidence.', 'Your Stage 2 win file is your evidence.'),
                 ('<p class="nl">In your tracker</p>', f'<p class="nl">In your {TP}</p>')])
pages.append(s7)
pages.append(rep(S[21], [('<span class="badge">Stage 6 · Deep dive</span>', '<span class="badge">Stage 7 · Deep dive</span>'), ('<h2 class="stitle">Turn money into time</h2>', '<h2 class="stitle">Put a number on your freedom</h2>'), ('Know exactly what your time costs, and buy it back', 'Know what a free day costs, and plan for it')]))
pages.append(rep(S[22], [('<p class="kick">Your system for the long run</p>', '<div class="stagehead"><span class="badge">Stage 7 · Deep dive</span><span class="chip lvl">Repeat</span></div>\n  <p class="kick" style="margin-top:14px">Your system for the long run</p>'),
                         ('Go back to Stage 1 and rebuild your baseline.', 'Go back to Stage 2 and rebuild your baseline.')]))
au = [('Bills and needs', 'Payday', 'Standing orders and direct debits from your bills account'),
      ('Keep your first hour', 'Payday', 'Fixed transfer to your safety net, then to investing'),
      ('Debt extra', 'Payday', 'Fixed extra payment to Priority 1 until it is gone'),
      ('Goal pots', 'Day 2', 'One transfer per pot: gifts, care, holiday, car'),
      ('Investing', 'Day 2', 'A fixed monthly amount, reviewed once a year'),
      ('Side income split', 'When it arrives', 'Tax pot first, then investing and your time goal'),
      ('Saving rate +1–2 points', 'Every raise', 'Raise the transfers before your lifestyle notices')]
atr = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>☐</td></tr>' for a, b, c in au)
pages.append(page(head_stage('Stage 7 · Deep dive', [('lvl', 'Automate')], 'Automate everything you can',
    'Decide once, then let the system carry you',
    'The goal of Stage 7 is a money life that runs on its own while you spend your attention on the people you love. Every line you automate is one less decision on a tired evening.') + f'''
  <div class="tablewrap"><table class="budget"><tr><th>What</th><th>When</th><th>How</th><th>Done</th></tr>{atr}</table></div>
  <div class="two">
    <div class="box"><div class="when">Your yearly money date · 2 hours</div><ol class="tpl"><li>Salary review booked, win file ready</li><li>Saving and investing rate up 1–2 points</li><li>Freedom numbers updated</li><li>Investment costs and risk checked</li><li>Insurance and goal pots reviewed</li></ol></div>
    <div class="box heavy"><div class="when">Lifestyle creep check</div><p class="script">When your income rises, spending quietly rises with it. Once a year, compare your wants in T · Track with last year. If they grew faster than your keep rate, move the difference back to your future.</p></div>
  </div>'''))
pages.append(page(head_stage('Stage 7 · Your tool', [('lvl', 'Buy-back list')], 'Your buy-back-time list',
    'Price your time, then buy back the hours that matter most',
    'Not every hour costs money to get back. Start with the free ones, then use your freedom numbers to decide which paid ones are worth it.') + '''
  <div class="tablewrap"><table class="budget fill"><tr><th>Hour I want back</th><th>Free or paid?</th><th>Cost a month</th><th>Hours a month gained</th><th>Who gets that time</th></tr>
    <tr><td>Unpaid overtime</td><td>Free</td><td>€0</td><td>16</td><td>Family dinners</td></tr>
    <tr><td>Weekly big shop instead of 4 small ones</td><td>Free</td><td>€0</td><td>4</td><td>Sunday walk</td></tr>
    <tr><td>Cleaning help, every two weeks</td><td>Paid</td><td>€80</td><td>6</td><td>Time with mum</td></tr>
    <tr><td>&nbsp;</td><td></td><td></td><td></td><td></td></tr><tr><td>&nbsp;</td><td></td><td></td><td></td><td></td></tr><tr><td>&nbsp;</td><td></td><td></td><td></td><td></td></tr></table></div>
  <div class="box" style="margin-top:16px"><div class="when">Monthly review · 30 minutes</div><ol class="tpl">
    <li>KEEP this month: €______ · keep rate ______% · Freedom Level ______</li>
    <li>Safety net ______% · debt €______ · invested this month €______ · extra income €______</li>
    <li>One win, however small: ______________________________</li>
    <li>Hours I took back this month: ______ and who I spent them with: ______</li>
    <li>Next month's single focus: ______________________________</li></ol></div>'''))
pages.append(checklist_page(7, 'Repeat, automate &amp; buy back time · done when',
    ['Every transfer in the automation table runs on its own.', 'My monthly review happens, even in short form.', 'I mapped my real week and my goal week in T · Time.',
     'I took back at least one free hour every week.', 'My freedom numbers are written down.', 'My yearly money date is in the calendar.'],
    'T · Time: family time gained a year. Monthly Review: one row a month. The KEEP dashboard shows your level, and the 7 Stages tab shows 7 of 7.',
    'There is no next stage. You repeat the cycle once a year, a little higher each time, until work is a choice (Level 6).',
    ['The first hours I took back went to…', 'My Level 6 number (needs a month): €…', 'What “enough” looks like for me…']))

# ---------- CLOSING ----------
months = [('Month 1', 'Mindset &amp; numbers', 'Money why, real hourly value, 2-hour setup, every euro sorted, one leak cut.', ''),
          ('Month 2', 'Starter buffer', 'Separate account, standing transfers. Win file started.', ''),
          ('Month 3', 'Debt order', 'Priority 1 chosen, lender called, no new debt. Skip if you have none.', ''),
          ('Month 4', 'Raise prep', 'Market range researched, review booked, flexibility on the list too.', ''),
          ('Month 5', 'Debt-free push', 'Roll payments forward. Aim for Level 3.', ''),
          ('Month 6', 'Safety net', 'Fund target set, goal pots running, emergency rule written.', ''),
          ('Month 7', 'Pick one stream', 'Contract and tax rules checked. One-page offer written.', ''),
          ('Month 8', 'Learn investing', 'Employer pension checked, two-sentence test, costs understood.', ''),
          ('Month 9', 'Full fund', '3–6 months saved. Level 4: secure. 90-day test starts.', ''),
          ('Month 10', 'Automate wealth', 'Fixed monthly investing amount on payday, if it suits your situation.', ''),
          ('Month 11', 'Day-90 decision', 'Keep, change or stop the stream. Track € per hour.', ''),
          ('Month 12', 'Time map', 'Real week vs goal week. Price the gap. Plan year two.', ' hl')]
mo = ''.join(f'<div class="mo{h}"><span class="m">{a}</span><b>{b}</b><span>{c}</span></div>' for a, b, c, h in months)
yr = S[23]
yr = re.sub(r'<div class="months">.*?</div>\s*(?=<div class="pfoot")', f'<div class="months">{mo}</div>\n  ', yr, flags=re.S)
pages.append(yr)
pages.append(S[24])
gl = [('Baseline', 'What your life really costs a month: your needs. The base of every freedom number.'),
      ('Keep rate', 'What you keep divided by what comes in. The single best number to watch every week.'),
      ('Real hourly value', 'Net pay divided by your real hours, including overtime and commute.'),
      ('Keep your first hour', 'Paying your future the first hour of every workday, on payday, before anything else.'),
      ('Starter buffer', 'One month of needs, saved before you attack debt.'),
      ('Emergency fund', '3–6 months of needs, separate and easy to reach. Insurance, not an investment.'),
      ('Avalanche', 'Paying extra on the debt with the highest interest rate first.'),
      ('Goal pot', 'A small monthly amount for a cost you know is coming: gifts, repairs, care.'),
      ('Compound growth', 'Growth that earns growth of its own. Time is its strongest ingredient.'),
      ('Inflation', 'Prices rising over time, so the same euro buys a little less each year.'),
      ('Costs (TER)', 'What an investment charges every year, in percent.'),
      ('€ per hour', 'What a side stream really pays for the time you put in.'),
      ('Freedom Level', 'Seven levels from Overwhelmed to Free to choose. Your tracker works it out.'),
      ('Freedom number', 'The extra income that would cover your needs, so work becomes a choice.')]
gtr = ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in gl)
pages.append(page(f'''  <p class="kick">Words you'll meet</p>
  <h2 class="big">Your money glossary</h2>
  <div class="rule"></div>
  <p class="lead">Money talk is full of jargon, often on purpose. These are the only words you need for this roadmap, in plain language.</p>
  <div class="tablewrap"><table class="budget"><tr><th>Word</th><th>What it means</th></tr>{gtr}</table></div>'''))
cta = rep(S[25], [('You only need to begin Stage 1.', 'You only need to begin Stage 1.'),
                  ('<li>Open your TRUST Tracker and read the About Me and How to Use tabs (5 minutes).</li>', f'<li>Open {TP} and read the About Me, How to Use and 7 Stages tabs (5 minutes).</li>'),
                  ('<li>Book your 2-hour setup session within the next 7 days.</li>', '<li>Write your money why in one sentence (Stage 1).</li>\n    <li>Book your 2-hour setup session within the next 7 days.</li>'),
                  ('This roadmap and the TRUST Tracker are for education only.', f'This roadmap and {TP} are for education only.')])
pages.append(cta)

# ---------- EXTRAS: fill pages, 7-stage road ----------
import sys as _s; _s.path.insert(0, D); import extras as X
def _ins(p, h):
    i = p.rindex('<div class="pfoot">'); return p[:i] + h + '\n  ' + p[i:]
for _n, _h in X.ADD.items():
    if _h: pages[_n - 1] = _ins(pages[_n - 1], _h)
for _n, (_st, _bad, _good) in X.CHK.items():
    pages[_n - 1] = _ins(pages[_n - 1], X.mistakes(_bad, _good))
    pages[_n - 1] = pages[_n - 1].replace('<h2 class="stitle">', X.strip(_st, 'done') + '\n  <h2 class="stitle">', 1)
for _n, _st in X.OPEN.items():
    pages[_n - 1] = pages[_n - 1].replace('<h2 class="stitle">', X.strip(_st, 'open') + '\n  <h2 class="stitle">', 1)
_m = pages[5]; _a = _m.index('<div class="journey">'); _b = _m.index('<p style', _a)
pages[5] = _m[:_a] + X.bigroad() + '\n  ' + _m[_b:]
def _drop(p, start):
    i = p.index(start); j = i; depth = 0
    for m in re.finditer(r'<div\b|</div>', p[i:]):
        depth += 1 if m.group(0) != '</div>' else -1
        if depth == 0: j = i + m.end(); break
    return p[:i] + p[j:]
pages[29] = _drop(pages[29], '<div class="calc">')
pages[31] = _drop(pages[31], '<div class="ifthen')
pages[47] = pages[47].replace('Five traps for busy people', 'Seven traps for busy people')
pages[48] = pages[48].replace('</table></div>', X.glossary_rows() + '</table></div>', 1)

pages[49] = rep(pages[49], [("<p>© cybercnslt.com · Liliane. For the purchaser's personal use only. Please don't copy, resell or share.</p>", X.COPY)])
# agenda page after the map
def _txt(x): return re.sub(r'<[^>]+>', '', x).strip()
pages.insert(6, 'AGENDA')
_items = []
for _i, _p in enumerate(pages):
    if _p == 'AGENDA' or _i == 0: continue
    _h = re.search(r'<h2[^>]*>(.*?)</h2>', _p, re.S); _t = _h.group(1) if _h else ''
    _t = re.sub(r'\s*·\s*done when', '', _t)
    _bd = re.search(r'<span class="badge">Stage (\d)([^<]*)</span>', _p)
    if _bd:
        _g = int(_bd.group(1)); _r = _bd.group(2)
        _k = 'Checklist' if 'Checklist' in _r else 'Your tool' if 'tool' in _r else 'Deep dive' if _r.strip() else 'The stage'
        if _k == 'Checklist': _t = 'Done when · tick off and unlock the next stage'
    else:
        _g = 0 if _i < 10 else 8; _k = 'Read' if _g == 0 else 'Plan'
    _items.append((_g, _i + 1, _k, _t))
pages[6] = page(X.agenda(_items))
def _pg(title): return next(n for g, n, k, t in _items if title in t)
_refs = {'page 10': 'page %d' % _pg('Wealth starts with your mindset'), 'page 12': 'page %d' % _pg('real hourly value &amp; your money story'),
         'page 22': 'page %d' % _pg('Your debt payoff plan'), '<small>Page 30</small>': '<small>Page %d</small>' % _pg('Time is the strongest'),
         '(page 07)': '(page %02d)' % _pg('Your rhythm')}
_rx = re.compile('|'.join(re.escape(k) for k in _refs))
for _i in range(len(pages)): pages[_i] = _rx.sub(lambda m: _refs[m.group(0)], pages[_i])

# ---------- ASSEMBLE ----------
out = []
n = 0
for p in pages:
    if '<section class="page' in p:
        n += 1
        num = f'{n:02d}'
        p = re.sub(r'<div class="pfoot"><span>The Wealth Roadmap · iCyber</span><span>\d+</span>(?:</span>)*</div>',
                   f'<div class="pfoot"><span>The Wealth Roadmap · © 2026 iCyber · Personal use only</span><span>{num}</span></div>', p)
    out.append(p)
html = head.replace('<title>The Wealth Roadmap</title>', '<title>The Wealth Roadmap</title>') + '\n\n'.join(out) + '\n'
html = html.replace('.checklist{', '.lines{height:0;}\n  .budget.fill td{height:30px;}' + X.CSS + '\n  .checklist{')
_k = html.index('<section'); html = html[:_k] + re.sub(r'(?<=[ >])9–5(?=[ <.,])', '<span class="nb">9–5</span>', html[_k:])
if 'charset' not in html[:600]: html = '<meta charset="utf-8">\n' + html
def _enc(seg, mode):
    if mode == 'css': return ''.join(c if ord(c) < 128 else '\\%x ' % ord(c) for c in seg)
    if mode == 'js': return ''.join(c if ord(c) < 128 else ''.join('\\u%04x' % u for u in __import__('struct').unpack('<' + 'H' * (len(c.encode('utf-16-le')) // 2), c.encode('utf-16-le'))) for c in seg)
    return ''.join(c if ord(c) < 128 else f'&#{ord(c)};' for c in seg)
_parts = re.split(r'(<style[^>]*>.*?</style>|<script[^>]*>.*?</script>)', html, flags=re.S)
html = ''.join(_enc(x, 'css' if x.startswith('<style') else 'js' if x.startswith('<script') else 'html') for x in _parts)
open('/home/user/terragoat/icyber/wealth-roadmap-50.html', 'w').write(html)
print('pages', n, 'size', len(html))
print('TRUST Tracker mentions:', html.count('TRUST Tracker Pro'), '| old name left:', len(re.findall(r'TRUST Tracker(?! Pro)', html)))
