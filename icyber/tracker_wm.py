"""Add a faint 'iCyber' background picture to every sheet (Excel shows it behind the cells)."""
import zipfile, re, io, shutil, os
from PIL import Image, ImageDraw, ImageFont

def _png():
    W, H = 1400, 900
    im = Image.new('RGBA', (W, H), (255, 255, 255, 255))
    f = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf', 190)
    t = Image.new('RGBA', (W, H), (255, 255, 255, 0))
    d = ImageDraw.Draw(t)
    w = d.textlength('iCyber', font=f)
    d.text(((W - w) / 2, H / 2 - 110), 'iCyber', font=f, fill=(19, 78, 78, 16))
    t = t.rotate(28, resample=Image.BICUBIC)
    im.alpha_composite(t)
    b = io.BytesIO(); im.convert('RGB').save(b, 'PNG', optimize=True); return b.getvalue()

def add_background(path):
    src = zipfile.ZipFile(path); tmp = path + '.tmp'
    out = zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED)
    names = src.namelist(); png = _png()
    sheets = [n for n in names if re.match(r'xl/worksheets/sheet\d+\.xml$', n)]
    for n in names:
        data = src.read(n)
        if n == '[Content_Types].xml' and b'Extension="png"' not in data:
            data = data.replace(b'<Default ', b'<Default Extension="png" ContentType="image/png"/><Default ', 1)
        if n in sheets:
            x = data.decode('utf-8')
            m = re.search(r'<(oleObjects|controls|webPublishItems|tableParts|extLst)\b|</worksheet>', x)
            x = x[:m.start()] + '<picture r:id="rIdWm"/>' + x[m.start():]
            if 'xmlns:r=' not in x[:600]:
                x = x.replace('<worksheet ', '<worksheet xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" ', 1)
            data = x.encode('utf-8')
        out.writestr(n, data)
    out.writestr('xl/media/icyber_watermark.png', png)
    rel = '<Relationship Id="rIdWm" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/icyber_watermark.png"/>'
    for n in sheets:
        rn = n.replace('worksheets/', 'worksheets/_rels/') + '.rels'
        if rn in names:
            continue  # handled below
        out.writestr(rn, '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' + rel + '</Relationships>')
    out.close(); src.close()
    # patch existing rels files (sheets with comments)
    z = zipfile.ZipFile(tmp); out2 = zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED)
    for n in z.namelist():
        d = z.read(n)
        if re.match(r'xl/worksheets/_rels/sheet\d+\.xml\.rels$', n) and b'rIdWm' not in d:
            d = d.replace(b'</Relationships>', rel.encode() + b'</Relationships>')
        out2.writestr(n, d)
    out2.close(); z.close(); os.remove(tmp)
