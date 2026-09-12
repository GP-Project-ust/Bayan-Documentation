# مشروع «بيان» — وثيقة رسالة التخرج

مساعد ذكي مؤسسي معتمد على الذكاء الاصطناعي وتحليل البيانات
**جامعة العلوم والتكنولوجيا — كلية الحاسبات — قسم تقنية المعلومات**

وثيقة LaTeX كاملة (عربية RTL) مبنية على تكييف للقالب الرسمي، تُبنى
تلقائياً عبر GitHub Actions عند كل دفعة إلى `main`.

## الحالة الراهنة

| المكوّن | الحالة |
|---|---|
| الفصول 1–3 (مقدمة، خلفية نظرية، منهجية وتحليل) | ✅ مكتملة |
| الفصول 4–7 (تصميم، تنفيذ واختبار، نتائج، خاتمة) | 🏗️ هياكل جاهزة — مشروع التخرج 2 |
| الملاحق أ–و | 🏗️ هياكل جاهزة |
| الصفحات التمهيدية (غلاف، ملخص، إهداء، شكر، إقرار، لجنة) | ✅ مكتملة |

**إحصاءات النسخة الحالية:** 109 صفحات · 31 مرجعاً بنمط IEEE · 14 شكلاً
(12 مخطط TikZ + مخططا جانت) · 28 جدولاً.

## بنية المستودع

```
Bayan-Documentation/
├── main.tex                  ← الإعدادات الكلية + ترتيب المحتوى (المتغيرات في نهايته)
├── .latexmkrc                ← إعداد latexmk/xelatex
├── references.bib            ← المراجع (المصدر الوحيد — 31 مرجعاً)
├── IEEEtran.bst              ← نمط المراجع IEEE
├── CONTRIBUTING.md           ← دليل المساهمة (اقرأه قبل أول تعديل)
├── docs/LATEX_SETUP.md       ← دليل إعداد بيئة LaTeX المحلية
├── chapters/
│   ├── chapter1.tex          ← المقدمة (مكتمل — يتضمن مخططَي جانت التنفيذيين)
│   ├── chapter2.tex          ← الخلفية النظرية ومراجعة الأدبيات (مكتمل)
│   ├── chapter3.tex          ← المنهجية وتحليل النظام (مكتمل)
│   │   └── chapter3/         ← أقسام الفصل الثالث الستة
│   ├── chapter4.tex … chapter7.tex   ← هياكل مشروع التخرج 2
├── frontmatter/              ← الغلاف، الملخص، الإهداء، الشكر، إقرار المشرف،
│                                لجنة المناقشة، المختصرات، الملاحق
├── figures/
│   ├── logo-ust.jpeg         ← شعار الجامعة
│   ├── logo-bayan.png        ← شعار المشروع
│   └── tikz/                 ← 12 مخططاً برمجياً بصيغة TikZ (المصدر الوحيد للأشكال)
├── scripts/strip-bidi.py     ← تنظيف النص المنسوخ من PDF
└── .github/workflows/build-pdf.yml   ← بناء PDF تلقائياً
```

## البناء

### GitHub Actions (تلقائي)

عند كل push إلى `main` يمس أي ملف `tex`/`bib`/`figures`: يُثبَّت TeX Live
مع الخطوط العربية، يُبنى `main.pdf` عبر `latexmk -xelatex`، يُرفع كـ
artifact (30 يوماً)، ويُدفَع تلقائياً إلى المستودع. ويمكن تشغيله يدوياً من
**Actions → Build Thesis PDF → Run workflow**.

### محلياً

```bash
# الخيار الموصى به (يتولى كل الدورات تلقائياً)
latexmk -xelatex main.tex

# أو عبر tectonic
tectonic main.tex

# أو يدوياً (كرر لحل الفهرس والمراجع)
xelatex main.tex && bibtex main && xelatex main.tex && xelatex main.tex
```

### Overleaf

ارفع المستودع كـ zip، ثم اختر **XeLaTeX** من إعدادات المشروع (Menu →
Compiler) واضغط Recompile.

## المتطلبات

- **المحرك:** XeLaTeX (إلزامي للعربية عبر polyglossia + bidi).
- **الخطوط:** Amiri (الأساسي) · Noto Naskh Arabic (المخططات) ·
  Liberation Serif (الإنجليزية) · DejaVu Sans Mono (الأكواد).
  التثبيت: ضع ملفات `.ttf` في `~/.local/share/fonts/` ثم `fc-cache -f`.
  على Debian/Ubuntu: `sudo apt install fonts-hosny-amiri fonts-noto-core`.
- **الحزم:** fontspec, polyglossia, bidi, tikz, tabularx, longtable,
  hyperref, titlesec, fancyhdr, caption, enumitem, amssymb.

## تخصيص سريع

- **بيانات الغلاف والإشراف:** المتغيرات في نهاية `main.tex`
  (`\thesisTitleAR`، `\thesisSupervisorAR`، …).
- **أسماء الطلاب والأرقام الجامعية:** `frontmatter/cover.tex` و
  `frontmatter/declaration.tex` (و`pdfauthor` في `main.tex`).
- **إضافة مرجع:** أضف المدخل إلى `references.bib` ثم `\cite{مفتاحه}`
  في النص — القائمة تتولد آلياً بنمط IEEE.

## ملاحظات مهمة

- النص الإنجليزي داخل الفقرات العربية يُكتب بالأمر `\EN{...}`
  (LTR تلقائياً)، والأكواد بـ `\CODE{...}`.
- كل المخططات مصدرها `figures/tikz/*.tex` — لا تستورد صوراً جاهزة
  للمخططات؛ عدّل مصدر TikZ مباشرة.
- ترقيم الصفحات: الغلاف بلا رقم، التمهيدية رومانية، الفصول عربية.
- عند نسخ نص من PDF قد تظهر محارف اتجاهية زائدة؛ نظّفها بـ
  `python3 scripts/strip-bidi.py`.

## دليل المساهمة

قبل أي تعديل، راجع **[CONTRIBUTING.md](CONTRIBUTING.md)** — يشرح بنية
المشروع، وأمثلة جاهزة لكل نوع محتوى (فصل، جدول، شكل، مرجع، كود،
معادلة)، وقواعد التحقق قبل الرفع. لإعداد بيئة LaTeX محلية راجع
**[docs/LATEX_SETUP.md](docs/LATEX_SETUP.md)**.
