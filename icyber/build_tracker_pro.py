from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from openpyxl.comments import Comment
import sys

DARK="134E4E"; TEAL="1A9E9E"; DEEP="0F6E6E"; BORD="9E1B5E"; TINT="E8F4F2"; TINT2="F2F8F7"; LINE="DDEAE8"; INK="213534"; MUTE="6E8180"; INPUT="FFF7E0"
F="Arial"
EUR='€#,##0;-€#,##0;"–"'
EUR2='€#,##0.00;-€#,##0.00;"–"'
PCT='0.0%;-0.0%;"–"'
thin=Side(style="thin",color=LINE)
BOX=Border(left=thin,right=thin,top=thin,bottom=thin)

wb=Workbook()
def sheet(title,tabcolor,widths):
    ws=wb.create_sheet(title); ws.sheet_properties.tabColor=tabcolor
    ws.sheet_view.showGridLines=False
    for col,w in widths.items(): ws.column_dimensions[col].width=w
    return ws
def header(ws,title,sub,span="B2:H2"):
    ws.row_dimensions[2].height=40
    ws.merge_cells(span); c=ws[span.split(":")[0]]
    c.value=title; c.font=Font(name="Georgia",size=20,bold=True,color="FFFFFF")
    c.fill=PatternFill("solid",fgColor=DARK); c.alignment=Alignment(vertical="center",indent=1)
    for row in ws[span]:
        for x in row: x.fill=PatternFill("solid",fgColor=DARK)
    s=span.replace("2","3")
    ws.merge_cells(s); c=ws[s.split(":")[0]]
    c.value=sub; c.font=Font(name=F,size=10,italic=True,color=MUTE); c.alignment=Alignment(wrap_text=True,vertical="top",indent=1)
    ws.row_dimensions[3].height=32
def label(ws,ref,text,color=TEAL,size=10):
    c=ws[ref]; c.value=text; c.font=Font(name=F,size=size,bold=True,color=color)
def th(ws,row,cols_titles):
    for col,t in cols_titles:
        c=ws[f"{col}{row}"]; c.value=t
        c.font=Font(name=F,size=9,bold=True,color="FFFFFF"); c.fill=PatternFill("solid",fgColor=TEAL)
        c.alignment=Alignment(horizontal="center",vertical="center",wrap_text=True); c.border=BOX
    ws.row_dimensions[row].height=30
def inp(ws,ref,val=None,fmt=None):
    c=ws[ref]
    if val is not None: c.value=val
    c.font=Font(name=F,size=10,color="0000FF"); c.fill=PatternFill("solid",fgColor=INPUT); c.border=BOX
    if fmt: c.number_format=fmt
def calc(ws,ref,formula,fmt=None,bold=False,color=INK,fill=None):
    c=ws[ref]; c.value=formula; c.font=Font(name=F,size=10,bold=bold,color=color); c.border=BOX
    if fill: c.fill=PatternFill("solid",fgColor=fill)
    if fmt: c.number_format=fmt
def text(ws,ref,t,size=10,color=INK,bold=False,italic=False,wrap=True):
    c=ws[ref]; c.value=t; c.font=Font(name=F,size=size,color=color,bold=bold,italic=italic)
    c.alignment=Alignment(wrap_text=wrap,vertical="top")
def dv_list(ws,formula,rng):
    dv=DataValidation(type="list",formula1=formula,allow_blank=True); ws.add_data_validation(dv); dv.add(rng)

wb.remove(wb.active)

# ---------- LISTS (hidden) ----------
L=wb.create_sheet("Lists")
cats=["Housing","Utilities & phone","Groceries","Transport","Insurance","Childcare","Caregiving","Health","Debt payments","Subscriptions","Eating out","Shopping","Fun & hobbies","Gifts","Travel","Other"]
for i,v in enumerate(cats,1): L[f"A{i}"]=v
for i,v in enumerate(["Need","Want"],1): L[f"B{i}"]=v
for i,v in enumerate(["Keep","Cut","Reduce","Renegotiate"],1): L[f"C{i}"]=v
streams=["Career (raise/promotion)","Freelance / consulting","Digital product","UGC","YouTube / content","Brand deals","Affiliate","Investment income","Other"]
for i,v in enumerate(streams,1): L[f"D{i}"]=v
for i,v in enumerate(["Idea","Testing","Earning","Paused"],1): L[f"E{i}"]=v
levels=["Level 0 · Overwhelmed","Level 1 · Stable","Level 2 · Buffered","Level 3 · Debt-free","Level 4 · Secure","Level 5 · Flexible","Level 6 · Free to choose"]
for i,v in enumerate(levels,1): L[f"F{i}"]=v
for i,v in enumerate(["To do","In progress","Done ✓"],1): L[f"G{i}"]=v
for i,v in enumerate(["Yes","No","Not sure"],1): L[f"H{i}"]=v
L.sheet_state="hidden"

# ---------- ABOUT ME ----------
ws=sheet("About Me",BORD,{"A":3,"B":100,"C":3})
ws.row_dimensions[2].height=44
c=ws["B2"]; c.value="Hey, I'm Liliane."; c.font=Font(name="Georgia",size=22,bold=True,color="FFFFFF"); c.fill=PatternFill("solid",fgColor=DARK); c.alignment=Alignment(vertical="center",indent=1)
c=ws["B3"]; c.value="You work hard for your money. But is it creating the life you're working so hard for?"
c.font=Font(name="Georgia",size=14,italic=True,color=TEAL); c.alignment=Alignment(wrap_text=True,vertical="center",indent=1); ws.row_dimensions[3].height=34
def para(r,t,size=10.5,color=INK,bold=False,italic=False,font=F,fill=None,lines=None):
    c=ws[f"B{r}"]; c.value=t; c.font=Font(name=font,size=size,color=color,bold=bold,italic=italic)
    c.alignment=Alignment(wrap_text=True,vertical="top",indent=1)
    if fill: c.fill=PatternFill("solid",fgColor=fill)
    n=lines or max(1,-(-len(t)//105))
    ws.row_dimensions[r].height=max(16,n*15+4)
about=[
 ("k","I'm a full-time cybersecurity consultant at a Big Four firm, working in the financial sector. I work a demanding job, and alongside my 9–5 I support my mum, who receives care at home after her cerebral haemorrhage. Balancing both is demanding, so I know how little time is left at the end of the day. Everything here comes from my own experience: I paid off €30,000 of debt and I'm building wealth beside my career with the same system I share here. I don't teach this from the outside. I've experienced it myself."),
 ("p","You have a demanding career, bills to pay and people who depend on you. You earn a respectable income. Yet despite everything you do, you don't always feel as financially secure or independent as you thought you would."),
 ("q","How do I build a financially secure future without missing out on the people and moments that matter most today?"),
 ("p","I know that feeling. I started as a flight attendant working toward becoming a pilot, until COVID changed those plans. I rebuilt my path in cybersecurity consulting. My income grew, but financial security didn't automatically follow. In my 20s I took on loans for my study fees, made wrong financial decisions and even fell for an online scam: I was heavily into trading without knowing much about it. My rule since then: only invest in what you understand. I paid off €30,000 of debt not by first earning more, but by understanding my finances and making deliberate changes. Now in my 30s, this is what I wish someone had told me in my 20s."),
 ("h","WHY I REALLY BUILT THIS"),
 ("q2","My mum is 83. When she had her cerebral haemorrhage, I realised how valuable time really is, and how little of it I had left. For years I worked long hours and stayed late almost every single day, because I believed climbing the corporate ladder was what success meant. But true success is realising what truly matters in life, and then taking the steps, one by one, that lead you there. We only get this one life. I want to spend as much time with her as I possibly can. Not someday, but now."),
 ("p","Most of the financial advice out there told me to quit my job, hustle harder or get rich fast. That's unrealistic unless you're willing to risk your financial security, and when people depend on you, that's not a risk worth taking. None were made for someone with a demanding career and a mum who needs them. I wish I'd had a clear, honest plan for the few hours I actually had left, when I wasn't already exhausted from work and every other responsibility around me. So I decided to build it for myself, step by step. You shouldn't need a wake-up call to start. Begin before yours comes, or before it's too late."),
 ("p","That's why I created TRUST Tracker Pro, the full version of my free TRUST Sheet, built to work hand in hand with The Wealth Roadmap. No judgment. No unrealistic promises. No complicated jargon. Just a practical system for making your money work toward the life you actually want."),
 ("h","WHO THIS IS FOR"),
 ("b","✓  Your financial progress doesn't reflect the effort you put into your career."),
 ("b","✓  You balance work, family or caregiving, and need a system that fits your limited time."),
 ("b","✓  You earn a decent income and want clarity on what you keep, spend, save and owe."),
 ("b","✓  You want a strong foundation before building wealth or extra income streams."),
 ("b","✓  You want financial independence for a reason: more choices and more time with the people you love."),
 ("m","Not for anyone looking for overnight wealth or guaranteed returns."),
 ("h","THE METHOD · KEEP + TRUST"),
 ("k","KEEP = Know your Earnings to Escape your Paycheck. Your salary can be the foundation of your financial future. It doesn't have to define your limits."),
 ("b","T · Track: know your numbers. What comes in, what goes out, what you actually keep."),
 ("b","R · Reclaim: find where money slips away and redirect it toward what matters to you."),
 ("b","U · Understand: see your position clearly, including debt and the real value of your hour."),
 ("b","S · Save: build resilience, set priorities and prepare for your future."),
 ("b","T · Time: see how money and time connect, and why independence is really about choices."),
 ("m","Knowing your numbers is the beginning, not the goal. TRUST is the foundation for debt freedom, wealth building and additional income."),
 ("h","HOW IT FOLLOWS THE ROADMAP"),
 ("p","The Wealth Roadmap has 7 stages. Each stage uses one or two tabs in this tracker. The 7 Stages tab shows which tab belongs to which stage, and lets you tick off each stage when it is done."),
 ("h","WEALTH STARTS WITH YOUR MINDSET"),
 ("p","Becoming wealthy starts with how you think about money and with understanding the laws of money. Money management is a skill you learn, not a talent you're born with."),
 ("b","1 · Spend less than you earn. The gap is where all wealth begins."),
 ("b","2 · Pay yourself first. Your future gets paid on payday, before bills and wants."),
 ("b","3 · Protect what you have. A safety net and no expensive debt."),
 ("b","4 · Make your money work for you. Only invest in what you understand."),
 ("b","5 · Give it time. Compound growth rewards patience more than luck."),
 ("h","YOUR NEXT STEP"),
 ("p","Head to the How to Use tab, then the 7 Stages tab. In about 20 minutes you'll have your first financial snapshot. You don't need everything figured out today. You just need somewhere meaningful to start."),
 ("c","Financial freedom isn't about quitting your 9–5. It's about using your career as the engine to fuel your financial independence, build multiple income streams, and create the freedom to spend more time with the people you love."),
 ("s","Build your options without quitting your 9–5.  Know your money. Build your wealth. Reclaim your time.\n— Liliane · iCyber · @cyber_cnslt · cybercnslt.com"),
 ("d","Educational information only, not individualised financial or investment advice. TRUST Tracker Pro helps you organise and understand your finances; it doesn't guarantee financial outcomes. Your financial information stays in your own copy of the workbook unless you choose to share it."),
 ("h","COPYRIGHT & HOW THIS WAS MADE"),
 ("p","© 2026 iCyber. All rights reserved. TRUST Tracker Pro and The Wealth Roadmap are licensed for the personal use of the purchaser only. Copying, sharing, reselling, redistributing or publishing them, in full or in part, is not permitted without written permission."),
 ("p","All ideas, the 7-stage structure, the KEEP and TRUST methods, the frameworks and the stories are my own original work. Some text and design elements were created with the help of AI tools, then reviewed, edited and approved by me.")
]
r=5
for kind,t in about:
    if kind=="p": para(r,t)
    elif kind=="q": para(r,t,size=12,color=BORD,italic=True,font="Georgia",fill=TINT,lines=2)
    elif kind=="h": r+=1; para(r,t,size=10,color=BORD,bold=True)
    elif kind=="q2": para(r,t,color=BORD,bold=True,fill="F7E7EF",lines=6)
    elif kind=="b": para(r,t,lines=1)
    elif kind=="m": para(r,t,color=MUTE,italic=True)
    elif kind=="k": para(r,t,color=DARK,bold=True,fill=TINT2)
    elif kind=="c": r+=1; para(r,t,size=13,color=TEAL,italic=True,font="Georgia",fill=TINT,lines=4)
    elif kind=="s": para(r,t,color=DEEP,bold=True,lines=2)
    elif kind=="d": r+=1; para(r,t,size=8.5,color=MUTE,lines=2)
    r+=1

# ---------- HOW TO USE ----------
ws=sheet("How to Use",BORD,{"A":3,"B":26,"C":70,"D":3})
header(ws,"How to Use","About 20 minutes to set up, 15 minutes a week to run. Built for busy weeks.","B2:C2")
rows=[
("FIRST SNAPSHOT · ABOUT 20 MINUTES",None),
("1 · Fill the yellow cells","Every cell with a pale yellow background and blue text is yours to edit. Everything else calculates itself. The rows already filled in are EXAMPLES: overwrite or delete them."),
("2 · Go tab by tab, in order","T Track → R Reclaim → U Understand → S Save → T Time. Then Invest and Income Streams when your roadmap stage gets there. The 7 Stages tab shows which tab belongs to which stage."),
("3 · Read your KEEP dashboard","It shows what you keep, your Freedom Level (0–6) and the one next step that matters now."),
("4 · Review once a month","Copy this month's dashboard numbers into Monthly Review. 12 rows, one per month. Watch your level climb."),
("",None),
("EVERY WEEK · 15 MINUTES",None),
("Weekly money check","Open KEEP and look at what you keep. Add new costs or income. Move this week's saving or debt payment."),
("Heavy week?","Caring for someone, deadlines, illness: open the KEEP dashboard, look at one number, close it. That counts. The system is built to pause without breaking."),
("",None),
("COLOUR KEY",None),
("Yellow cell, blue text","Your input"),
("Black text","Calculated: please don't overwrite"),
("Bordeaux text","Money going out or still owed (debt)"),
("",None),
("Copyright","© 2026 iCyber. All rights reserved. TRUST Tracker Pro and The Wealth Roadmap are licensed for the personal use of the purchaser only. Copying, sharing, reselling, redistributing or publishing them, in full or in part, is not permitted without written permission."),
("How this was made","All ideas, the 7-stage structure, the KEEP and TRUST methods, the frameworks and the stories are my own original work. Some text and design elements were created with the help of AI tools, then reviewed, edited and approved by me."),
]
r=5
for a,b in rows:
    if b is None and a:
        label(ws,f"B{r}",a,BORD,11)
    else:
        text(ws,f"B{r}",a,bold=True,color=DARK); text(ws,f"C{r}",b)
        if b and len(b)>80: ws.row_dimensions[r].height=15*((len(b)//80)+1)
    r+=1
inp(ws,"B16","Yellow cell, blue text"); ws["B16"].font=Font(name=F,size=10,color="0000FF",bold=True)
ws["B18"].font=Font(name=F,size=10,bold=True,color=BORD)

# ---------- TRACK ----------
ws=sheet("T · Track",TEAL,{"A":3,"B":30,"C":22,"D":12,"E":14,"F":34})
header(ws,"T · Track","Roadmap stage 2 · List what comes in and what goes out in a normal month. Yearly costs? Divide by 12. Debt minimum payments are a Need. Don't list savings transfers here: what's left over is what you KEEP.","B2:F2")
label(ws,"B5","MONEY IN (net, per month)")
th(ws,6,[("B","Source"),("C","Note"),("E","€ / month")])
inc=[("Salary (net)","Main job",2500),("Side income","Total from Income Streams tab",None),("Benefits / allowances","e.g. child benefit, care allowance",0)]
for i in range(7,13):
    for col in "BC": inp(ws,f"{col}{i}")
    inp(ws,f"E{i}",fmt=EUR)
for i,(a,b,v) in enumerate(inc,7):
    ws[f"B{i}"]=a; ws[f"C{i}"]=b
    if v is not None: ws[f"E{i}"]=v
calc(ws,"E8","='Income Streams'!G23",EUR,color="008000")
ws["E8"].comment=Comment("Pulled automatically from the Income Streams tab. Overwrite only if you prefer to enter it here.","iCyber")
text(ws,"B13","Total money in",bold=True,color=DARK); calc(ws,"E13","=SUM(E7:E12)",EUR,bold=True,fill=TINT)

label(ws,"B15","MONEY OUT (per month)")
th(ws,16,[("B","Expense"),("C","Category"),("D","Need / Want"),("E","€ / month"),("F","Note")])
ex=[("Rent / mortgage","Housing","Need",900),("Electricity, internet, phone","Utilities & phone","Need",140),("Groceries","Groceries","Need",320),("Public transport / fuel","Transport","Need",90),("Insurance","Insurance","Need",80),("Care support for mum","Caregiving","Need",150),("Credit card minimum","Debt payments","Need",60),("Streaming & apps","Subscriptions","Want",45),("Eating out & takeaway","Eating out","Want",120),("Clothes & shopping","Shopping","Want",100)]
for i in range(17,57):
    for col in "BCDF": inp(ws,f"{col}{i}")
    inp(ws,f"E{i}",fmt=EUR)
for i,(a,b,c,v) in enumerate(ex,17):
    ws[f"B{i}"]=a; ws[f"C{i}"]=b; ws[f"D{i}"]=c; ws[f"E{i}"]=v
ws["F17"]="Example rows: overwrite with yours"
dv_list(ws,'"Housing,Utilities & phone,Groceries,Transport,Insurance,Childcare,Caregiving,Health,Debt payments,Subscriptions,Eating out,Shopping,Fun & hobbies,Gifts,Travel,Other"',"C17:C56"); dv_list(ws,'"Need,Want"',"D17:D56")
text(ws,"B58","Needs (your baseline)",bold=True,color=DARK); calc(ws,"E58",'=SUMIF(D17:D56,"Need",E17:E56)',EUR,bold=True,fill=TINT)
text(ws,"B59","Wants",bold=True,color=DARK); calc(ws,"E59",'=SUMIF(D17:D56,"Want",E17:E56)',EUR,bold=True,fill=TINT)
text(ws,"B60","of which caregiving",color=MUTE); calc(ws,"E60",'=SUMIF(C17:C56,"Caregiving",E17:E56)',EUR)
text(ws,"B61","Unsorted (pick Need or Want)",color=BORD); calc(ws,"E61","=SUM(E17:E56)-E58-E59",EUR,color=BORD)
text(ws,"B62","KEEP (in − needs − wants)",bold=True,color=TEAL); calc(ws,"E62","=E13-E58-E59",EUR,bold=True,color=TEAL,fill=TINT)
text(ws,"B63","Keep rate",bold=True,color=TEAL); calc(ws,"E63","=IF(E13>0,E62/E13,0)",PCT,bold=True,color=TEAL,fill=TINT)
ws.freeze_panes="B5"

# ---------- RECLAIM ----------
ws=sheet("R · Reclaim",TEAL,{"A":3,"B":30,"C":14,"D":15,"E":14,"F":14,"G":30})
header(ws,"R · Reclaim","Roadmap stage 2 · Go through bank statements for 10 minutes. Every subscription, fee and contract goes here. Decide: Keep, Cut, Reduce or Renegotiate. One call to a provider can be worth hundreds a year.","B2:G2")
th(ws,5,[("B","Subscription / cost"),("C","Now € / month"),("D","Decision"),("E","New € / month"),("F","Reclaimed € / month"),("G","Next action")])
rc=[("Second streaming service",13,"Cut",0,"Cancel before renewal on the 15th"),("Gym (not used since spring)",35,"Reduce",15,"Switch to off-peak plan"),("Mobile contract",40,"Renegotiate",25,"Call and ask for current tariff"),("Cloud storage",3,"Keep",3,"")]
for i in range(6,31):
    for col in "BDG": inp(ws,f"{col}{i}")
    inp(ws,f"C{i}",fmt=EUR); inp(ws,f"E{i}",fmt=EUR)
    calc(ws,f"F{i}",f'=IF(OR(C{i}="",D{i}="",D{i}="Keep"),0,MAX(0,C{i}-(E{i})))',EUR,color=TEAL)
for i,(a,b,c,d,e) in enumerate(rc,6):
    ws[f"B{i}"]=a; ws[f"C{i}"]=b; ws[f"D{i}"]=c; ws[f"E{i}"]=d; ws[f"G{i}"]=e
dv_list(ws,'"Keep,Cut,Reduce,Renegotiate"',"D6:D30")
text(ws,"B32","Reclaimable per month",bold=True,color=DARK); calc(ws,"F32","=SUM(F6:F30)",EUR,bold=True,color=TEAL,fill=TINT)
text(ws,"B33","Reclaimable per year",bold=True,color=DARK); calc(ws,"F33","=F32*12",EUR,bold=True,color=TEAL,fill=TINT)
text(ws,"B35","Rule: reclaimed money gets a job the same day. Move it to your buffer or debt before it disappears into everyday spending.",italic=True,color=MUTE)
ws.merge_cells("B35:G35"); ws.row_dimensions[35].height=30

# ---------- UNDERSTAND ----------
ws=sheet("U · Understand",TEAL,{"A":3,"B":28,"C":14,"D":12,"E":14,"F":13,"G":15,"H":14,"I":12})
header(ws,"U · Understand","Roadmap stages 1–3 · Debt first: what you owe, what it costs you each month, and which one to attack first (highest interest = highest priority). Then: what is one hour of your working life really worth?","B2:I2")
th(ws,5,[("B","Debt"),("C","Balance €"),("D","Interest % / year"),("E","Minimum € / month"),("F","Extra € / month"),("G","Interest cost € / month"),("H","Months to clear"),("I","Priority")])
dbt=[("Credit card",1500,0.199,60,40),("Overdraft",0,0.12,0,0)]
for i in range(6,16):
    inp(ws,f"B{i}"); inp(ws,f"C{i}",fmt=EUR); inp(ws,f"D{i}",fmt="0.0%"); inp(ws,f"E{i}",fmt=EUR); inp(ws,f"F{i}",fmt=EUR)
    calc(ws,f"G{i}",f'=IF((C{i})>0,C{i}*(D{i})/12,0)',EUR2,color=BORD)
    calc(ws,f"H{i}",f'=IF((C{i})<=0,"",IF((E{i})+(F{i})<=G{i},"Payment too low",ROUNDUP(IF((D{i})=0,C{i}/((E{i})+(F{i})),NPER(D{i}/12,-((E{i})+(F{i})),C{i})),0)))',"0")
    calc(ws,f"I{i}",f'=IF((C{i})<=0,"",COUNTIFS($C$6:$C$15,">0",$D$6:$D$15,">"&(D{i}))+1)',"0",bold=True,color=BORD)
for i,(a,b,c,d,e) in enumerate(dbt,6):
    ws[f"B{i}"]=a; ws[f"C{i}"]=b; ws[f"D{i}"]=c; ws[f"E{i}"]=d; ws[f"F{i}"]=e
text(ws,"B17","Total debt",bold=True,color=DARK); calc(ws,"C17","=SUM(C6:C15)",EUR,bold=True,color=BORD,fill=TINT)
text(ws,"B18","Interest you pay / month",bold=True,color=DARK); calc(ws,"C18","=SUM(G6:G15)",EUR2,bold=True,color=BORD,fill=TINT)
text(ws,"B19","Interest you pay / year",bold=True,color=DARK); calc(ws,"C19","=C18*12",EUR,bold=True,color=BORD,fill=TINT)
text(ws,"D17","Priority 1 = highest interest rate. Send every extra euro there, pay minimums on the rest. Months to clear is an estimate with fixed payments.",italic=True,color=MUTE)
ws.merge_cells("D17:I19")

label(ws,"B22","WHAT ONE HOUR OF YOUR LIFE IS WORTH")
th(ws,23,[("B","Item"),("C","Value")])
text(ws,"B24","Net money in / month"); calc(ws,"C24","='T · Track'!E7",EUR,color="008000")
ws["C24"].comment=Comment("Your net salary from T · Track (row 7).","iCyber")
text(ws,"B25","Contract hours / week"); inp(ws,"C25",39,"0.0")
text(ws,"B26","Unpaid overtime / week"); inp(ws,"C26",4,"0.0")
text(ws,"B27","Commute hours / week"); inp(ws,"C27",5,"0.0")
text(ws,"B28","Real hours / month",bold=True); calc(ws,"C28","=((C25)+(C26)+(C27))*52/12","0.0")
text(ws,"B29","Your real hourly value",bold=True,color=TEAL); calc(ws,"C29","=IF(C28>0,C24/C28,0)",EUR2,bold=True,color=TEAL,fill=TINT)
text(ws,"B30","Workdays / month"); inp(ws,"C30",21,"0")
text(ws,"B31","Keep your first hour / month",bold=True,color=TEAL); calc(ws,"C31","=C29*(C30)",EUR,bold=True,color=TEAL,fill=TINT)
text(ws,"D24","Keep your first hour: the first hour of every workday is paid to you, not to your bills. Set up a standing transfer for this amount on payday. If it's too much right now, start with a quarter of it.",italic=True,color=MUTE)
ws.merge_cells("D24:I28")
text(ws,"D29","Before any purchase over €50, divide the price by your real hourly value. That's how many hours of your life it costs.",italic=True,color=MUTE)
ws.merge_cells("D29:I31")

# ---------- SAVE ----------
ws=sheet("S · Save",TEAL,{"A":3,"B":32,"C":15,"D":14,"E":15,"F":15,"G":14})
header(ws,"S · Save","Roadmap stages 3–4 · The order matters. First a 1-month buffer, then clear consumer debt, then a full emergency fund (3 months; 6 if you're a carer, self-employed or the only earner). Then goals.","B2:G2")
label(ws,"B5","EMERGENCY FUND")
th(ws,6,[("B","Item"),("C","Value")])
text(ws,"B7","Monthly needs (baseline)"); calc(ws,"C7","='T · Track'!E58",EUR,color="008000")
text(ws,"B8","Months of safety you want"); inp(ws,"C8",3,"0")
text(ws,"B9","Starter buffer (1 month)",bold=True); calc(ws,"C9","=C7",EUR,bold=True)
text(ws,"B10","Full emergency fund target",bold=True); calc(ws,"C10","=C7*(C8)",EUR,bold=True,fill=TINT)
text(ws,"B11","Saved so far"); inp(ws,"C11",1200,EUR)
text(ws,"B12","Progress",bold=True,color=TEAL); calc(ws,"C12","=IF(C10>0,MIN(1,(C11)/C10),0)",PCT,bold=True,color=TEAL,fill=TINT)
text(ws,"B13","Monthly transfer to it"); inp(ws,"C13",250,EUR)
text(ws,"B14","Months until full fund",bold=True); calc(ws,"C14",'=IF((C11)>=C10,"Done ✓",IF((C13)>0,ROUNDUP((C10-(C11))/C13,0),"Add a transfer"))',"0")
text(ws,"D7","Keep it separate from your everyday account, easy to reach within a day or two, and boring. This money is insurance, not an investment.",italic=True,color=MUTE)
ws.merge_cells("D7:G10")

label(ws,"B17","GOAL POTS (sinking funds)")
th(ws,18,[("B","Goal"),("C","Target €"),("D","Saved €"),("E","€ / month"),("F","Months left"),("G","Progress")])
gl=[("Care costs & time off",1500,300,75),("Christmas & birthdays",600,100,50),("Holiday with family",1800,250,100)]
for i in range(19,29):
    inp(ws,f"B{i}"); inp(ws,f"C{i}",fmt=EUR); inp(ws,f"D{i}",fmt=EUR); inp(ws,f"E{i}",fmt=EUR)
    calc(ws,f"F{i}",f'=IF((C{i})=0,"",IF((D{i})>=C{i},"Done ✓",IF((E{i})>0,ROUNDUP((C{i}-(D{i}))/E{i},0),"–")))',"0")
    calc(ws,f"G{i}",f'=IF((C{i})>0,MIN(1,(D{i})/C{i}),0)',PCT,color=TEAL)
for i,(a,b,c,d) in enumerate(gl,19):
    ws[f"B{i}"]=a; ws[f"C{i}"]=b; ws[f"D{i}"]=c; ws[f"E{i}"]=d
text(ws,"B30","Total monthly to goal pots",bold=True); calc(ws,"E30","=SUM(E19:E28)",EUR,bold=True,fill=TINT)
text(ws,"B31","Total monthly saving (fund + pots)",bold=True,color=TEAL); calc(ws,"E31","=(C13)+E30",EUR,bold=True,color=TEAL,fill=TINT)
text(ws,"B32","Still unassigned from KEEP",bold=True,color=DARK); calc(ws,"E32","='T · Track'!E62-E31",EUR,bold=True,fill=TINT)
text(ws,"B33","If 'still unassigned' is negative, your plan spends more than you keep. Lower a transfer until it's zero or positive.",italic=True,color=MUTE)
ws.merge_cells("B33:G33")

# ---------- TIME ----------
ws=sheet("T · Time",TEAL,{"A":3,"B":30,"C":14,"D":14,"E":40})
header(ws,"T · Time","Roadmap stage 7 · A week has 168 hours. Map a realistic one, including care and recovery. Then decide which hours you'll protect for the people you love, and how many (if any) go to building options.","B2:E2")
th(ws,5,[("B","Area"),("C","Hours / week now"),("D","Hours / week goal"),("E","What would change it?")])
tm=[("Sleep",49,52,"Phone out of the bedroom"),("Paid work (incl. overtime)",43,40,"Stop answering email after 7pm"),("Commute",5,5,""),("Caregiving",10,10,"Ask sibling for one fixed day"),("Household & admin",10,8,"One big shop per week"),("Family & friends time",12,16,"Protected Sunday afternoon"),("Health & movement",3,4,"Walk at lunch"),("Building options (learning / side income)",3,4,"Two 2-hour blocks, Tue & Sat"),("Rest & yourself",10,10,"")]
for i in range(6,18):
    inp(ws,f"B{i}"); inp(ws,f"C{i}",fmt="0.0"); inp(ws,f"D{i}",fmt="0.0"); inp(ws,f"E{i}")
for i,(a,b,c,d) in enumerate(tm,6):
    ws[f"B{i}"]=a; ws[f"C{i}"]=b; ws[f"D{i}"]=c; ws[f"E{i}"]=d
text(ws,"B19","Hours planned",bold=True); calc(ws,"C19","=SUM(C6:C17)","0.0",bold=True); calc(ws,"D19","=SUM(D6:D17)","0.0",bold=True)
text(ws,"B20","Unplanned hours (of 168)",bold=True,color=TEAL); calc(ws,"C20","=168-C19","0.0",bold=True,color=TEAL,fill=TINT); calc(ws,"D20","=168-D19","0.0",bold=True,color=TEAL,fill=TINT)
text(ws,"B22","Family time gained / week",bold=True,color=BORD); calc(ws,"C22",'=SUMIF(B6:B17,"Family*",D6:D17)-SUMIF(B6:B17,"Family*",C6:C17)',"0.0",bold=True,color=BORD,fill=TINT)
text(ws,"B23","Family time gained / year",bold=True,color=BORD); calc(ws,"C23","=C22*52","0",bold=True,color=BORD,fill=TINT)
text(ws,"B25","Negative unplanned hours mean the week doesn't fit. Something has to go before anything new comes in. Never take side-project hours out of sleep or family first.",italic=True,color=MUTE)
ws.merge_cells("B25:E26"); ws.row_dimensions[25].height=24
text(ws,"B28","Your hourly value at work",bold=True); calc(ws,"C28","='U · Understand'!C29",EUR2,color="008000")
text(ws,"B29","Value of the work hours you want back / year",bold=True); calc(ws,"C29",'=MAX(0,SUMIF(B6:B17,"Paid work*",C6:C17)-SUMIF(B6:B17,"Paid work*",D6:D17))*52*C28',EUR,bold=True,fill=TINT)
text(ws,"D28","This is roughly what extra income or savings would need to replace if you reduced your paid hours to your goal. A concrete target for the Income Streams tab.",italic=True,color=MUTE)
ws.merge_cells("D28:E30")

# ---------- INCOME STREAMS ----------
ws=sheet("Income Streams",DEEP,{"A":3,"B":30,"C":24,"D":11,"E":12,"F":14,"G":14,"H":13,"I":30})
header(ws,"Income Streams","Roadmap stages 2 + 6 · Build one stream at a time, beside your career. Log every stream here, including a raise you negotiated. Watch € per hour: a stream that pays less than your job per hour must be buying you something else (skills, assets, freedom later).","B2:I2")
th(ws,5,[("B","Stream"),("C","Type"),("D","Status"),("E","Hours / week"),("F","Started (month)"),("G","€ / month (net)"),("H","€ per hour"),("I","Next small step")])
st=[("Salary raise negotiated","Career (raise/promotion)","Earning",0,"2026-03",150,"Prepare next review in March"),("Cybersecurity starter guide","Digital product","Testing",3,"2026-08",60,"Post 3 reels pointing to it"),("UGC for a skincare brand","UGC","Idea",0,"",0,"Make 2 sample videos")]
for i in range(6,22):
    for col in "BCDFI": inp(ws,f"{col}{i}")
    inp(ws,f"E{i}",fmt="0.0"); inp(ws,f"G{i}",fmt=EUR)
    calc(ws,f"H{i}",f'=IF((E{i})>0,(G{i})/(E{i}*52/12),IF((G{i})>0,"no time logged",""))',EUR2,color=TEAL)
for i,(a,b,c,d,e,f,g) in enumerate(st,6):
    ws[f"B{i}"]=a; ws[f"C{i}"]=b; ws[f"D{i}"]=c; ws[f"E{i}"]=d; ws[f"F{i}"]=e; ws[f"G{i}"]=f; ws[f"I{i}"]=g
dv_list(ws,'"Career (raise/promotion),Freelance / consulting,Digital product,UGC,YouTube / content,Brand deals,Affiliate,Investment income,Other"',"C6:C21"); dv_list(ws,'"Idea,Testing,Earning,Paused"',"D6:D21")
text(ws,"B23","Total extra income / month",bold=True,color=TEAL); calc(ws,"G23",'=SUMIF(C6:C21,"<>Career (raise/promotion)",G6:G21)',EUR,bold=True,color=TEAL,fill=TINT)
text(ws,"B24","Career growth / month (in salary)",bold=True); calc(ws,"G24",'=SUMIF(C6:C21,"Career (raise/promotion)",G6:G21)',EUR,bold=True,fill=TINT)
text(ws,"B25","Hours / week on streams",bold=True); calc(ws,"E25","=SUM(E6:E21)","0.0",bold=True,fill=TINT)
text(ws,"B26","Share of your needs covered by extra income",bold=True,color=BORD); calc(ws,"G26","=IF('T · Track'!E58>0,G23/'T · Track'!E58,0)",PCT,bold=True,color=BORD,fill=TINT)
text(ws,"B28","A raise already shows up in your net salary on T · Track, so it is counted separately and not added to side income twice.",italic=True,color=MUTE)
ws.merge_cells("B28:I28")

# ---------- KEEP DASHBOARD ----------
ws=sheet("KEEP Dashboard",BORD,{"A":3,"B":30,"C":18,"D":4,"E":34,"F":18})
header(ws,"KEEP — Know your Earnings to Escape your Paycheck","Your month on one page. Nothing to fill in here: it reads every other tab.","B2:F2")
label(ws,"B5","YOUR FREEDOM LEVEL",BORD,11)
ws.merge_cells("B6:C7"); ws.merge_cells("E6:F7")
c=ws["B6"]; c.value='=CHOOSE(C9+1,"Level 0 · Overwhelmed","Level 1 · Stable","Level 2 · Buffered","Level 3 · Debt-free","Level 4 · Secure","Level 5 · Flexible","Level 6 · Free to choose")'; c.font=Font(name="Georgia",size=18,bold=True,color="FFFFFF"); c.fill=PatternFill("solid",fgColor=DARK); c.alignment=Alignment(vertical="center",indent=1)
ws["C7"].fill=PatternFill("solid",fgColor=DARK)
c=ws["E6"]; c.font=Font(name=F,size=10,color=INK); c.fill=PatternFill("solid",fgColor=TINT); c.alignment=Alignment(wrap_text=True,vertical="center",indent=1)
c.value=('=CHOOSE(C9+1,'
 '"Next step: more goes out than comes in. Use R · Reclaim and cut wants until KEEP is at least €0.",'
 '"Next step: build a starter buffer of one month of needs before anything else.",'
 '"Next step: clear consumer debt, highest interest first (Priority 1 on U · Understand).",'
 '"Next step: grow the buffer into your full emergency fund on S · Save.",'
 '"Next step: you are secure. Stage 5: learn investing basics on the Invest tab, then start ONE income stream.",'
 '"Next step: extra income covers 25%+ of needs. Keep investing; decide what time you want back.",'
 '"You have choices. Extra income covers your baseline. Decide on your terms how much you want to work.")')
ws.row_dimensions[6].height=28; ws.row_dimensions[7].height=28
text(ws,"B9","Level number"); calc(ws,"C9",'=IF(C14<0,0,IF(C22<C13,1,IF(C20>0,2,IF(C22<C23,3,IF(C25<0.25*C13,4,IF(C25<C13,5,6))))))',"0",bold=True)

label(ws,"B11","MONEY")
items=[("Money in / month","='T · Track'!E13",EUR,INK),("Needs (baseline)","='T · Track'!E58",EUR,DARK),("What you KEEP / month","='T · Track'!E62",EUR,TEAL),("Keep rate","='T · Track'!E63",PCT,TEAL),("Wants","='T · Track'!E59",EUR,BORD),("Reclaimable / month","='R · Reclaim'!F32",EUR,TEAL),("Reclaimable / year","='R · Reclaim'!F33",EUR,TEAL)]
for i,(a,f,fm,col) in enumerate(items,12):
    text(ws,f"B{i}",a); calc(ws,f"C{i}",f,fm,bold=True,color=col,fill=TINT2)
# rows 12..19
label(ws,"B19","SAFETY")
saf=[("Debt to clear","='U · Understand'!C17",EUR,BORD),("Interest you pay / year","='U · Understand'!C19",EUR,BORD),("Emergency fund saved","='S · Save'!C11",EUR,TEAL),("Emergency fund target","='S · Save'!C10",EUR,DARK),("Fund progress","='S · Save'!C12",PCT,TEAL)]
for i,(a,f,fm,col) in enumerate(saf,20):
    text(ws,f"B{i}",a); calc(ws,f"C{i}",f,fm,bold=True,color=col,fill=TINT2)
# rows 20..24 ; extra income row 25
text(ws,"B25","Extra income / month"); calc(ws,"C25","='Income Streams'!G23",EUR,bold=True,color=TEAL,fill=TINT2)
text(ws,"B26","Invested / month"); calc(ws,"C26","=Invest!D38",EUR,bold=True,color=TEAL,fill=TINT2)
text(ws,"B27","Roadmap stages done"); calc(ws,"C27","='7 Stages'!D14",None,bold=True,color=BORD,fill=TINT2)
label(ws,"E11","TIME & OPTIONS")
tim=[("1 hour of your life is worth","='U · Understand'!C29",EUR2,DARK),("Keep your first hour / month","='U · Understand'!C31",EUR,TEAL),("Hours / week on income streams","='Income Streams'!E25","0.0",INK),("Needs covered by extra income","='Income Streams'!G26",PCT,BORD),("Family time gained / week (goal)","='T · Time'!C22","0.0",BORD),("Unassigned KEEP after savings plan","='S · Save'!E32",EUR,INK),("Career growth / month","='Income Streams'!G24",EUR,TEAL)]
for i,(a,f,fm,col) in enumerate(tim,12):
    text(ws,f"E{i}",a); calc(ws,f"F{i}",f,fm,bold=True,color=col,fill=TINT2)
label(ws,"E20","THE FREEDOM LADDER",BORD)
lad=["0 · Overwhelmed: more out than in","1 · Stable: KEEP is €0 or more","2 · Buffered: 1 month of needs saved","3 · Debt-free: consumer debt cleared","4 · Secure: full emergency fund","5 · Flexible: extra income ≥ 25% of needs","6 · Free to choose: extra income ≥ needs"]
for i,t in enumerate(lad,21):
    text(ws,f"E{i}",t,wrap=False); ws.merge_cells(f"E{i}:F{i}")
ws.column_dimensions["G"].width=18
for i in range(21,28): calc(ws,f"G{i}",f'=IF($C$9={i-21},"◀ you are here","")',None,bold=True,color=BORD)
text(ws,"B29","Your career is the engine. Keep your first hour, and keep going. — Liliane",italic=True,color=DEEP,wrap=False)
text(ws,"B30","Educational tool. Not financial advice.",size=8,color=MUTE,wrap=False)

# ---------- 7 STAGES ----------
ws=sheet("7 Stages",BORD,{"A":3,"B":6,"C":40,"D":30,"E":46,"F":15,"G":14})
header(ws,"Your 7 stages","The Wealth Roadmap, one row per stage. Use the tabs listed, tick the stage off when the 'done when' is true, and write the date. Then move to the next stage.","B2:G2")
th(ws,5,[("B","#"),("C","Stage"),("D","Tabs to use"),("E","Done when"),("F","Status"),("G","Date done")])
stg=[("Money mindset: your 9–5 is your wealth engine","U · Understand (real hourly value)","You know your real hourly value and have written your money why."),
("Know your salary & your numbers","T · Track, R · Reclaim, Income Streams (Career)","KEEP shows your keep rate, one leak is cut and your win file is started."),
("Clear your debts (optional)","U · Understand, S · Save (starter buffer)","1 month of needs saved and consumer debt is €0 (Level 3)."),
("Build a safety net","S · Save","Your full emergency fund is 100% (Level 4)."),
("Build wealth with smart investing","Invest","A fixed monthly amount runs on payday and you can explain what you own."),
("Build multiple income streams","Income Streams","One stream finished its 90-day test with a keep, change or stop decision."),
("Repeat, automate & buy back time","T · Time, Monthly Review","Transfers run on their own and you have taken back your first hours.")]
for k,(a,b,c) in enumerate(stg):
    i=6+k; ws.row_dimensions[i].height=34
    text(ws,f"B{i}",k+1,bold=True,color=BORD); ws[f"B{i}"].alignment=Alignment(horizontal="center",vertical="top"); text(ws,f"C{i}",a,bold=True,color=DARK); text(ws,f"D{i}",b,color=TEAL); text(ws,f"E{i}",c)
    inp(ws,f"F{i}","To do"); inp(ws,f"G{i}")
dv_list(ws,'"To do,In progress,Done"',"F6:F12")
text(ws,"C14","Stages done",bold=True,color=DARK); calc(ws,"D14",'=COUNTIF(F6:F12,"Done")&" of 7"',None,bold=True,color=TEAL,fill=TINT)
text(ws,"C16","Stage 3 is optional: if you have no consumer debt, save the starter buffer and go straight to stage 4. Your money still grows while you pay debt off, just more slowly.",italic=True,color=MUTE)
ws.merge_cells("C16:G16"); ws.row_dimensions[16].height=30

# ---------- INVEST ----------
ws=sheet("Invest",DEEP,{"A":3,"B":34,"C":16,"D":16,"E":16,"F":16,"G":30})
header(ws,"Invest","Roadmap stage 5 · Only after your full emergency fund, and only in what you understand. This tab is for learning and planning. It does not recommend any product, fund or provider.","B2:G2")
label(ws,"B5","BEFORE YOU INVEST · CHECK")
th(ws,6,[("B","Question"),("C","Answer")])
text(ws,"B7","Full emergency fund in place?"); calc(ws,"C7","=IF('S · Save'!C12>=1,\"Yes ✓\",\"Not yet\")",None,bold=True,color=TEAL)
text(ws,"B8","Consumer debt cleared?"); calc(ws,"C8","=IF(('U · Understand'!C17)<=0,\"Yes ✓\",\"Not yet\")",None,bold=True,color=TEAL)
text(ws,"B9","Money not needed for 5+ years?"); inp(ws,"C9","Yes")
text(ws,"B10","Can you explain it in two sentences?"); inp(ws,"C10","Not sure")
text(ws,"B11","Provider is regulated (e.g. BaFin register)?"); inp(ws,"C11","Yes")
dv_list(ws,'"Yes,No,Not sure"',"C9:C11")
text(ws,"B12","Ready to start?",bold=True,color=DARK); calc(ws,"C12",'=IF(AND(C7="Yes ✓",C8="Yes ✓",C9="Yes",C10="Yes",C11="Yes"),"Ready ✓","Not yet: finish the checks")',None,bold=True,color=BORD,fill=TINT)
text(ws,"D7","If any answer is not 'Yes', fix that first. Learning counts as progress.",italic=True,color=MUTE); ws.merge_cells("D7:G9")

label(ws,"B14","WHAT TIME COULD DO · ILLUSTRATION ONLY")
th(ws,15,[("B","Item"),("C","Value")])
text(ws,"B16","Monthly amount"); inp(ws,"C16",100,EUR)
text(ws,"B17","Starting amount"); inp(ws,"C17",0,EUR)
text(ws,"B18","Years"); inp(ws,"C18",25,"0")
text(ws,"B19","Hypothetical yearly growth"); inp(ws,"C19",0.05,"0.0%")
text(ws,"B20","Yearly costs (fees)"); inp(ws,"C20",0.005,"0.00%")
text(ws,"B21","You pay in",bold=True); calc(ws,"C21","=(C17)+(C16)*12*(C18)",EUR,bold=True)
text(ws,"B22","Value before fees",bold=True,color=TEAL); calc(ws,"C22","=IF((C19)=0,C21,FV((C19)/12,(C18)*12,-(C16),-(C17)))",EUR,bold=True,color=TEAL,fill=TINT)
text(ws,"B23","Value after fees",bold=True,color=TEAL); calc(ws,"C23","=IF((C19)-(C20)=0,C21,FV(((C19)-(C20))/12,(C18)*12,-(C16),-(C17)))",EUR,bold=True,color=TEAL,fill=TINT)
text(ws,"B24","What the fees cost you",bold=True,color=BORD); calc(ws,"C24","=C22-C23",EUR,bold=True,color=BORD,fill=TINT)
text(ws,"D16","Change the yellow cells to see how time, amount and fees change the result. Fixed growth is a simplification: real returns go up and down, aren't guaranteed, and you can lose money. Taxes and inflation are not included.",italic=True,color=MUTE); ws.merge_cells("D16:G20")

label(ws,"B27","WHAT YOU ALREADY INVEST")
th(ws,28,[("B","Account / plan"),("C","Type"),("D","€ / month"),("E","Value now €"),("F","Yearly costs %"),("G","Note")])
iv=[("Workplace pension","Employer plan",100,2400,0.006,"Employer adds €50 a month"),("Long-term plan","Monthly savings plan",50,600,0.002,"Review once a year")]
for i in range(29,37):
    inp(ws,f"B{i}"); inp(ws,f"C{i}"); inp(ws,f"D{i}",fmt=EUR); inp(ws,f"E{i}",fmt=EUR); inp(ws,f"F{i}",fmt="0.00%"); inp(ws,f"G{i}")
for i,(a,b,c,d,e,f) in enumerate(iv,29):
    ws[f"B{i}"]=a; ws[f"C{i}"]=b; ws[f"D{i}"]=c; ws[f"E{i}"]=d; ws[f"F{i}"]=e; ws[f"G{i}"]=f
ws["G30"]="Example rows: overwrite with yours"
text(ws,"B38","Invested / month",bold=True,color=TEAL); calc(ws,"D38","=SUM(D29:D36)",EUR,bold=True,color=TEAL,fill=TINT)
text(ws,"B39","Invested so far",bold=True,color=TEAL); calc(ws,"E39","=SUM(E29:E36)",EUR,bold=True,color=TEAL,fill=TINT)
text(ws,"B41","Rule: automate a fixed amount on payday, review once a year, and never invest money you might need within 5 years.",italic=True,color=MUTE)
ws.merge_cells("B41:G41")

# ---------- MONTHLY REVIEW ----------
ws=sheet("Monthly Review",DEEP,{"A":3,"B":11,"C":13,"D":13,"E":13,"F":13,"G":11,"H":14,"I":13,"J":13,"K":22,"L":34})
header(ws,"Monthly Review","Once a month, 15 minutes: copy the numbers from KEEP into a new row. The level calculates itself. Write one win, however small.","B2:L2")
th(ws,5,[("B","Month"),("C","Money in"),("D","Needs"),("E","Wants"),("F","KEEP"),("G","Keep rate"),("H","Emergency fund"),("I","Debt"),("J","Extra income"),("K","Level"),("L","One win this month")])
for n,i in enumerate(range(6,18)):
    inp(ws,f"B{i}")
    for col in "CDEHIJ": inp(ws,f"{col}{i}",fmt=EUR)
    inp(ws,f"L{i}")
    calc(ws,f"F{i}",f'=IF(C{i}="","",C{i}-(D{i})-(E{i}))',EUR,color=TEAL)
    calc(ws,f"G{i}",f'=IF((C{i})>0,F{i}/C{i},"")',PCT,color=TEAL)
    calc(ws,f"K{i}",f'=IF(C{i}="","",CHOOSE(1+IF(F{i}<0,0,IF((H{i})<(D{i}),1,IF((I{i})>0,2,IF((H{i})<(D{i})*\'S · Save\'!$C$8,3,IF((J{i})<0.25*(D{i}),4,IF((J{i})<(D{i}),5,6)))))),"Level 0 · Overwhelmed","Level 1 · Stable","Level 2 · Buffered","Level 3 · Debt-free","Level 4 · Secure","Level 5 · Flexible","Level 6 · Free to choose"))',None,color=BORD)
ex=[("Sep 2026",2500,1650,330,1000,1500,0,"Cancelled 2 subscriptions"),("Oct 2026",2560,1640,265,1200,1400,60,"First €60 from my guide")]
for i,(m,a,b,c,h,d,j,w) in enumerate(ex,6):
    ws[f"B{i}"]=m; ws[f"C{i}"]=a; ws[f"D{i}"]=b; ws[f"E{i}"]=c; ws[f"H{i}"]=h; ws[f"I{i}"]=d; ws[f"J{i}"]=j; ws[f"L{i}"]=w
ws.freeze_panes="C6"

for s in wb.worksheets:
    s.sheet_view.zoomScale=110
order=["About Me","How to Use","7 Stages","T · Track","R · Reclaim","U · Understand","S · Save","Invest","Income Streams","T · Time","KEEP Dashboard","Monthly Review"]
wb.remove(wb["Lists"])
wb._sheets=[wb[n] for n in order]
wb.active=wb.sheetnames.index("About Me")
# ---------- COPYRIGHT LINE + PRINT FOOTER ON EVERY TAB ----------
for _ws in wb.worksheets:
    _c=_ws["B1"]; _c.value="© 2026 iCyber · For the purchaser's personal use only · Copying or reselling is not permitted"
    _c.font=Font(name=F,size=8,italic=True,color=MUTE); _c.alignment=Alignment(vertical="center")
    _ws.row_dimensions[1].height=16
    _ws.oddFooter.center.text="© 2026 iCyber · Personal use only · Copying or reselling is not permitted"
    _ws.oddFooter.center.size=8
    _ws.oddHeader.right.text="iCyber"; _ws.oddHeader.right.size=9

# ---------- AUTO-FIT: no cut-off text (measured with Arial-metric fonts, +12% for Apple Numbers) ----------
import math as _m, re as _re, copy as _cp
from functools import lru_cache as _lru
from PIL import ImageFont as _IF
from openpyxl.utils import get_column_letter as _L
_FD="/usr/share/fonts/truetype/"
@_lru(None)
def _font(name,sz,b,i):
    if name=="Georgia": f=_FD+"liberation/LiberationSerif-"+("BoldItalic" if b and i else "Bold" if b else "Italic" if i else "Regular")+".ttf"; mult=1.12
    else: f=_FD+"liberation/LiberationSans-"+("BoldItalic" if b and i else "Bold" if b else "Italic" if i else "Regular")+".ttf"; mult=1.0
    return _IF.truetype(f,int(round(sz*4/3*10))),mult
def _pw(s,c):
    f=c.font; fo,mult=_font(f.name or "Arial",f.sz or 11,bool(f.b),bool(f.i))
    return fo.getlength(s)/10*mult*1.12
def _txt(c):
    v=c.value
    if v is None: return ""
    if isinstance(v,str) and v.startswith("="):
        lits=[x for x in _re.findall(r'"([^"]*)"',v) if x] or [""]
        best=max(lits,key=len); num="€100,000.00" if "0.00" in (c.number_format or "") else "€100,000"
        return best if len(best)>len(num) else num
    if isinstance(v,(int,float)): return "€100,000.00" if "0.00" in (c.number_format or "") else "€"+f"{v:,.0f}"
    return str(v)
def _lines(s,cap,c):
    n=0
    for para in str(s).split("\n"):
        cur=""; n+=1
        for word in para.split(" "):
            t=(cur+" "+word) if cur else word
            if _pw(t,c)>cap and cur: n+=1; cur=word
            else: cur=t
    return n
for ws in wb.worksheets:
    def W(col): return ws.column_dimensions[_L(col)].width or 8.43
    def PX(w): return w*7+5
    mtop={(m.min_row,m.min_col):m for m in ws.merged_cells.ranges}
    inner={(r,c) for m in ws.merged_cells.ranges for r in range(m.min_row,m.max_row+1) for c in range(m.min_col,m.max_col+1)}
    def pad(c): return 8+9*(c.alignment.indent or 0)
    for row in ws.iter_rows():
        for c in row:
            if c.value is None or (c.row,c.column) in inner or c.alignment.wrap_text: continue
            need=_pw(_txt(c),c)+pad(c)
            if need<=PX(W(c.column)): continue
            nb=ws.cell(c.row,c.column+1).value
            boxed=bool(c.border.right.style) or c.fill.fill_type=="solid"
            if nb is None and not boxed and not isinstance(c.value,(int,float)) and not str(c.value).startswith("="): continue
            w=_m.ceil((need-5)/7)
            if w<=50: ws.column_dimensions[_L(c.column)].width=w
            else: a=_cp.copy(c.alignment); a.wrap_text=True; c.alignment=a
    for (r,col),m in mtop.items():
        c=ws.cell(r,col)
        if c.value is None or c.alignment.wrap_text: continue
        w=PX(sum(W(x) for x in range(m.min_col,m.max_col+1)))
        need=_pw(_txt(c),c)+pad(c)
        if need>w:
            if (c.font.sz or 11)>=14: f=_cp.copy(c.font); f.sz=max(12,_m.floor(c.font.sz*w/need)); c.font=f
            else: a=_cp.copy(c.alignment); a.wrap_text=True; c.alignment=a
    for row in ws.iter_rows():
        for c in row:
            if c.value is None or not c.alignment.wrap_text: continue
            if (c.row,c.column) in inner and (c.row,c.column) not in mtop: continue
            if (c.row,c.column) in mtop:
                m=mtop[(c.row,c.column)]; w=PX(sum(W(x) for x in range(m.min_col,m.max_col+1))); rows=list(range(m.min_row,m.max_row+1))
            else: w=PX(W(c.column)); rows=[c.row]
            n=_lines(_txt(c),w-pad(c),c); sz=c.font.sz or 11
            need=n*sz*1.3+5
            have=sum((ws.row_dimensions[r].height or 15) for r in rows)
            if need>have:
                last=rows[-1]; ws.row_dimensions[last].height=round((ws.row_dimensions[last].height or 15)+(need-have),1)

wb.save(sys.argv[1])
import tracker_wm; tracker_wm.add_background(sys.argv[1])
