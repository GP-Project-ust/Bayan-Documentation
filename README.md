# قالب رسالة KAU — مشروع «المساعد الذكي المؤسسي (بيان)»

قالب LaTeX مستند إلى القالب الرسمي لجامعة الملك عبد العزيز (KAU)، مع تكييفه
لمشروع التخرج «مساعد ذكي مؤسسي معتمد على الذكاء الاصطناعي وتحليل البيانات» —
جامعة العلوم والتكنولوجيا، اليمن.

## المحتويات

```
kau_thesis/
├── main.tex                  ← الملف الرئيسي (إعدادات + ترتيب الفصول)
├── .latexmkrc                ← إعداد مترجم xelatex
├── references.bib            ← قاعدة بيانات BibTeX (احتياطية، غير مستخدمة)
├── references_manual.tex     ← المراجع بصيغة thebibliography (تُستخدم حالياً)
├── CONTRIBUTING.md           ← دليل المساهمة والإضافة (مهم لكل عضو)
├── chapters/
│   ├── chapter1.tex          ← الفصل الأول: المقدمة (مكتمل)
│   ├── chapter2.tex          ← الفصل الثاني: الخلفية النظرية ومراجعة الأدبيات (مكتمل)
│   ├── chapter3.tex          ← الفصل الثالث: المنهجية وتحليل النظام (هيكل جاهز)
│   ├── chapter4.tex          ← الفصل الرابع: تصميم النظام (هيكل جاهز)
│   ├── chapter5.tex          ← الفصل الخامس: تنفيذ واختبار النظام (هيكل جاهز)
│   ├── chapter6.tex          ← الفصل السادس: النتائج والمناقشة (هيكل جاهز)
│   └── chapter7.tex          ← الفصل السابع: الخاتمة والأعمال المستقبلية (هيكل جاهز)
├── frontmatter/
│   ├── cover.tex             ← صفحة الغلاف
│   ├── declaration.tex       ← تصريح الطلاب + إقرار المشرف + تأكيد
│   ├── dedication.tex        ← الإهداء
│   ├── acknowledgment.tex    ← الشكر والتقدير
│   ├── abstract.tex          ← الملخص (عربي + إنجليزي)
│   ├── abbreviations.tex     ← قائمة الاختصارات
│   └── appendices.tex        ← الملاحق (أ-و)
├── figures/                  ← كل صور المشروع (9 صور بأسماء وصفية)
│   ├── logo-ust.jpeg         ← شعار الجامعة
│   ├── logo-bayan.png        ← شعار مشروع بيان
│   ├── agile-model.png       ← نموذج أجايل
│   ├── gantt-part1.jpg       ← مخطط جانت الجزء الأول
│   ├── gantt-part2.jpg       ← مخطط جانت الجزء الثاني
│   ├── gantt-part3.jpg       ← مخطط جانت الجزء الثالث
│   ├── gantt-part4.jpg       ← مخطط جانت الجزء الرابع
│   ├── rag-flow.png          ← مخطط تدفق RAG
│   └── multi-agent-arch.png  ← معمارية Multi-Agent
├── scripts/
│   └── strip-bidi.py         ← سكربت لتنظيف النص المنسوخ من PDF
└── .github/workflows/
    └── build-pdf.yml         ← GitHub Actions لبناء PDF تلقائياً
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
- الفصول الجاهزة للملء: **الفصول 3-7** (هياكل عناوين كاملة جاهزة).
- الملاحق: **6 ملاحق** (أ-و) جاهزة للملء.
- عدد الصفحات في PDF الحالي: 57 صفحة.
- الصور: 9 صور مدمجة بأسماء وصفية.
- الجداول: 4 جداول (الأدوات المادية، الأدوات البرمجية، مقارنة الأنظمة، الفجوة البحثية).
- المراجع: 17 مرجعاً بصيغة IEEE.

## دليل المساهمة والإضافة

لإضافة محتوى جديد (فصل، نص، صورة، جدول، مرجع، كود، معادلة، إلخ)، راجع
**[CONTRIBUTING.md](CONTRIBUTING.md)** — دليل شامل باللغة العربية يشرح:

- بنية المشروع وكيفية التنقل بين ملفاته.
- كيفية الترجمة محلياً وعلى Overleaf.
- أمثلة كاملة لكل نوع من المحتوى (نص، فصل، صورة، جدول، كود، معادلة، مرجع).
- حل مشكلة نسخ النص من PDF.
- نصائح للتحقق من التغييرات قبل الرفع.

**كل عضو في الفريق يجب أن يقرأ هذا الدليل قبل البدء بالمساهمة.**
