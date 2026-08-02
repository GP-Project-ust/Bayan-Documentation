# قالب رسالة KAU — مشروع «المساعد الذكي المؤسسي (بيان)»

قالب LaTeX مستند إلى القالب الرسمي لجامعة الملك عبد العزيز (KAU)، مع تكييفه
لمشروع التخرج «مساعد ذكي مؤسسي معتمد على الذكاء الاصطناعي وتحليل البيانات» —
جامعة العلوم والتكنولوجيا، اليمن.

## المحتويات

```
kau_thesis/
├── main.tex                  ← الملف الرئيسي (يُفتح في Overleaf أو يُترجم محلياً)
├── references.bib            ← قاعدة بيانات BibTeX (لمن يريد استخدام biblatex+biber)
├── references_manual.tex     ← المراجع بصيغة thebibliography (تُستخدم حالياً)
├── chapters/
│   ├── chapter1.tex          ← الفصل الأول: المقدمة
│   └── chapter2.tex          ← الفصل الثاني: الخلفية النظرية ومراجعة الأدبيات
├── frontmatter/
│   ├── cover.tex             ← صفحة الغلاف
│   ├── declaration.tex       ← تصريح الطلاب + إقرار المشرف + تأكيد
│   ├── dedication.tex        ← الإهداء
│   ├── acknowledgment.tex    ← الشكر والتقدير
│   ├── abstract.tex          ← الملخص (عربي + إنجليزي)
│   └── abbreviations.tex     ← قائمة الاختصارات
├── figures/                  ← كل صور المشروع (9 صور)
└── README.md                 ← هذا الملف
```

## طريقة الترجمة

### على Overleaf

1. اضغط **New Project → Upload Project** وارفع ملف الـ zip.
2. من إعدادات المشروع (Menu → Compiler): اختر **XeLaTeX**.
3. اضغط **Recompile**.

### محلياً (XeLaTeX)

```bash
cd kau_thesis
xelatex main.tex
xelatex main.tex    # مرة ثانية لحل المراجع المتقاطعة
```

### محلياً (Tectonic — يتعامل مع كل الترجمات تلقائياً)

```bash
cd kau_thesis
tectonic main.tex
```

### عبر GitHub Actions (تلقائياً عند كل Push)

المستودع مزوّد بـ workflow جاهز في:

```
.github/workflows/build-pdf.yml
```

عند كل دفعة (push) لفرع `main`، يقوم الـ workflow تلقائياً بـ:

1. تثبيت XeLaTeX وحزم TeX Live اللازمة + الخطوط العربية (Amiri, Noto Naskh).
2. ترجمة `main.tex` عبر `latexmk -xelatex` (عدة دورات لحل الفهرس والمراجع).
3. رفع `main.pdf` كـ artifact قابل للتنزيل من صفحة الـ Action.
4. عمل commit للـ PDF المُحدّث وإعادته للمستودع تلقائياً.

كما يمكن تشغيله يدوياً من تبويب **Actions → Build Thesis PDF → Run workflow**.

> ملاحظة: الـ workflow يستخدم خطوط النظام فقط (بدون مسارات مُ hardcoded)،
> لذا يعمل على أي بيئة فيها حزم `fonts-hosny-amiri` و `fonts-noto-core` مثبّتة.

## المتطلبات

- **محرك الترجمة:** XeLaTeX (إلزامي لدعم العربية عبر polyglossia + bidi).
- **الخطوط:** Amiri (الأساسي) + Noto Naskh Arabic (احتياطي) + Liberation Serif
  (للنص الإنجليزي) + DejaVu Sans Mono (للكود).
  - تثبيت الخطوط: ضع ملفات `.ttf` في `~/.local/share/fonts/` ثم نفّذ
    `fc-cache -f`.
- **الحزم:** fontspec, polyglossia, bidi, graphicx, tikz, tabularx, longtable,
  booktabs, hyperref, titlesec, fancyhdr, caption, enumitem, amssymb.

## تخصيص المشروع

- **بيانات الغلاف:** عدّل المتغيرات في نهاية `main.tex` (`\thesisTitleAR`،
  `\thesisSupervisorAR`، …).
- **قائمة الطلاب:** عدّل `frontmatter/declaration.tex` و `frontmatter/cover.tex`.
- **إضافة فصول جديدة:** أنشئ `chapters/chapter3.tex` ثم أضف `\input{chapters/chapter3}`
  في `main.tex` بعد الفصل الثاني.
- **تبديل المراجع لـ BibLaTeX+biber:** استبدل `\input{references_manual}` في نهاية
  `main.tex` بـ `\printbibliography`، وأضف `\usepackage[backend=biber,style=ieee]{biblatex}`
  + `\addbibresource{references.bib}` في الـ preamble. (يتطلب تثبيت biber).

## ملاحظات

- استخدم الأمر `\EN{...}` لإدراج نص إنجليزي داخل سياق عربي (يُحوّل تلقائياً لـ LTR).
- استخدم الأمر `\CODE{...}` لإدراج أكواد برمجية بنمط monospace.
- أرقام الصفحات: الغلاف بدون رقم، الصفحات التمهيدية بالأرقام الرومانية، الفصول
  بالأرقام العربية.

## حالة التسليم

- الفصول المنجزة: **الفصل الأول** و**الفصل الثاني** كاملاً.
- عدد الصفحات في PDF الحالي: 37 صفحة.
- الصور: 9 صور مدمجة (شعارات، مخططات، صور الجداول الزمنية، مخططات معمارية).
- الجداول: 4 جداول (الأدوات المادية، الأدوات البرمجية، مقارنة الأنظمة، الفجوة البحثية).
- المراجع: 16 مرجعاً بصيغة IEEE.
