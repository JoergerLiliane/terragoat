# iCyber Wealth Shop on systeme.io

Files in this folder:
- `shop-systeme-raw-html.html` – the whole shop page as one block of code
- `liliane-portrait.png` – your photo for the top of the page

## 1. Upload your photo (2 min)
1. Upload `liliane-portrait.png` to systeme.io, either through your files/media library or by dropping a temporary Image element on the page and uploading it there.
2. Copy the image's link (a long `https://` address). If the editor doesn't show it, open the uploaded image in a new browser tab and copy the address bar.
3. You can delete the temporary Image element afterwards; the file stays uploaded.

## 2. Create the page (5 min)
1. **Funnels → Create** (or open your existing funnel) → **+ Add step → Custom page**. Name it `Shop`, URL path `shop` → `https://www.cybercnslt.com/shop`.
2. Open the editor and start from a **blank** template.
3. Add a **Section → Row → 1 column**. On the section **and** the row: padding `0`, background **Clear**, width **Full width**.
4. Drag a **Raw HTML** element (sometimes called "Custom HTML" / "Code") into the column.
5. Open `shop-systeme-raw-html.html`, copy **everything**, and paste it into the Raw HTML element.
6. In the pasted code, find `PASTE-YOUR-PHOTO-URL-HERE` and replace it with the photo URL from step 1.
7. Page settings → Background colour `#F5F4EF`. SEO title: `Build Your Wealth Without Quitting Your 9–5 · iCyber`.

## 3. Connect the buttons
The code already contains these links. Change them if your URLs differ:

| Button | Link in the code | What it should be |
|---|---|---|
| Get the bundle → (top card) | `#ic-bundle` | jumps down to the sales section – leave as is |
| Get the bundle for €39 → | `https://www.cybercnslt.com/wealth-roadmap-checkout` | your systeme.io **order form** page (see step 4) |
| Get it free → / Send me the free sheet → | `https://www.cybercnslt.com/trust-sheet` | your existing TRUST Sheet opt-in page |
| Impressum / Datenschutz (footer) | `/impressum`, `/datenschutz` | your legal pages (required in Germany) |

## 4. Set up the paid product (10 min)
1. **Products → Create product** → name `The Wealth Roadmap + TRUST Tracker`. Upload the roadmap PDF and the `.xlsx` tracker as product resources (or deliver via a members' area).
2. **Funnels → your funnel → + Add step → Order form** → URL path `wealth-roadmap-checkout`.
3. In the order form, add a price plan: **€39, one-time**. Check your systeme.io payment and tax settings: prices for EU consumers must include VAT.
4. **+ Add step → Thank you page** after the order form, with a download link or members' area access.
5. Later, when you move to €59, change only the price plan, and update `€39` / `€59` in the Raw HTML block (search for `€39`).

## 5. Test before you share
- Open `cybercnslt.com/shop` on your phone. Tap every button.
- Buy the bundle once in **test mode** and check that the download arrives.
- Put `cybercnslt.com/shop` in your Instagram bio.

## Notes
- The code is self-contained: its styles only apply inside the block, so systeme.io's theme won't break it (and it won't change the rest of your site).
- No reviews or star ratings are shown on purpose. Add real testimonials once your first buyers give feedback – never invented ones.
