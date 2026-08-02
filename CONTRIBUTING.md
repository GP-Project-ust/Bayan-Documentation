# دليل المساهمة في وثيقة مشروع بيان

> هذا الدليل يشرح كل ما تحتاج معرفته لإضافة محتوى جديد أو تعديل الوثيقة:
> نصوص، فصول، جداول، صور، مراجع، أكواد برمجية، رياضيات، وأكثر.

## الفهرس

- [بنية المشروع](#بنية-المشروع)
- [كيفية الترجمة محلياً](#كيفية-الترجمة-محلياً)
- [إضافة نص عادي](#إضافة-نص-عادي)
- [إضافة فصل جديد](#إضافة-فصل-جديد)
- [إضافة قسم أو قسم فرعي](#إضافة-قسم-أو-قسم-فرعي)
- [إضافة صورة](#إضافة-صورة)
- [إضافة جدول](#إضافة-جدول)
- [إضافة قائمة نقطية أو رقمية](#إضافة-قائمة-نقطية-أو-رقمية)
- [إضافة كود برمجي](#إضافة-كود-برمجي)
- [إضافة معادلة رياضية](#إضافة-معادلة-رياضية)
- [إضافة مرجع](#إضافة-مرجع)
- [إضافة اختصار](#إضافة-اختصار)
- [إدراج نص إنجليزي داخل سياق عربي](#إدراج-نص-إنجليزي-داخل-سياق-عربي)
- [تنسيقات نصية شائعة](#تنسيقات-نصية-شائعة)
- [مشكلة نسخ النص من PDF](#مشكلة-نسخ-النص-من-pdf)
- [التحقق من التغييرات قبل الرفع](#التحقق-من-التغييرات-قبل-الرفع)

---

## بنية المشروع

```
Bayan-Documentation/
├── main.tex                      ← الملف الرئيسي (إعدادات + ترتيب الفصول)
├── .latexmkrc                    ← إعداد مترجم xelatex
├── chapters/
│   ├── chapter1.tex              ← الفصل الأول: المقدمة
│   ├── chapter2.tex              ← الفصل الثاني: الخلفية النظرية ومراجعة الأدبيات
│   ├── chapter3.tex              ← الفصل الثالث: المنهجية وتحليل النظام
│   ├── chapter4.tex              ← الفصل الرابع: تصميم النظام
│   ├── chapter5.tex              ← الفصل الخامس: تنفيذ واختبار النظام
│   ├── chapter6.tex              ← الفصل السادس: النتائج والمناقشة
│   └── chapter7.tex              ← الفصل السابع: الخاتمة والأعمال المستقبلية
├── frontmatter/
│   ├── cover.tex                 ← صفحة الغلاف (الأسماء، الشعار، العنوان)
│   ├── declaration.tex           ← تصريح الطلاب + إقرار المشرف + تأكيد
│   ├── dedication.tex            ← الإهداء
│   ├── acknowledgment.tex        ← الشكر والتقدير
│   ├── abstract.tex              ← الملخص (عربي + إنجليزي)
│   ├── abbreviations.tex         ← قائمة الاختصارات
│   └── appendices.tex            ← الملاحق (أ: قاموس المصطلحات، ب: المتطلبات،
│                                    ج: كود مصدري، د: لقطات شاشة، هـ: استبيان،
│                                    و: توزيع أدوار الفريق)
├── figures/                      ← كل صور المشروع
│   ├── logo-ust.jpeg             ← شعار جامعة العلوم والتكنولوجيا
│   ├── logo-bayan.png            ← شعار مشروع بيان
│   ├── agile-model.png           ← نموذج أجايل
│   ├── gantt-part1.jpg           ← مخطط جانت الجزء الأول
│   ├── gantt-part2.jpg           ← مخطط جانت الجزء الثاني
│   ├── gantt-part3.jpg           ← مخطط جانت الجزء الثالث
│   ├── gantt-part4.jpg           ← مخطط جانت الجزء الرابع
│   ├── rag-flow.png              ← مخطط تدفق RAG
│   └── multi-agent-arch.png      ← معمارية Multi-Agent
├── references_manual.tex         ← قائمة المراجع بصيغة thebibliography
├── references.bib                ← قاعدة بيانات BibTeX (احتياطية، غير مستخدمة)
├── scripts/
│   └── strip-bidi.py             ← سكربت لتنظيف النص المنسوخ من PDF
└── .github/workflows/
    └── build-pdf.yml             ← GitHub Actions لبناء PDF تلقائياً
```

---

## كيفية الترجمة محلياً

### الطريقة 1: استخدام `latexmk` (مُوصى بها)

```bash
cd Bayan-Documentation
latexmk -xelatex main.tex
```

`latexmk` يُشغّل عدة دورات تلقائياً لحل الفهرس والمراجع المتقاطعة.

### الطريقة 2: استخدام `tectonic` (سريع، يثبّت الحزم تلقائياً)

```bash
cd Bayan-Documentation
tectonic main.tex
```

### الطريقة 3: يدوياً (XeLaTeX)

```bash
xelatex main.tex
xelatex main.tex    # دورة ثانية لحل الفهرس
```

### على Overleaf

1. ارفع ملف ZIP للمشروع عبر **New Project → Upload Project**.
2. من **Menu → Compiler**: اختر **XeLaTeX**.
3. اضغط **Recompile**.

---

## إضافة نص عادي

افتح ملف الفصل المطلوب (مثلاً `chapters/chapter1.tex`) وأضف الفقرة:

```latex
هذا نص عادي يُكتب مباشرة بدون أي تنسيق. يمكن كتابة عدة أسطر
وسيقوم LaTeX بدمجها في فقرة واحدة. الفقرة الجديدة تبدأ بعد
سطر فارغ.

هذه فقرة جديدة لأنها مفصولة بسطر فارغ.
```

**قواعد مهمة:**
- السطر الفارغ = فقرة جديدة.
- المسافات المتعددة تُدمج في مسافة واحدة.
- لإدراج فاصل سطر قسري: `\\` أو `\newline`.
- لإدراج مسافة بعرض محدد: `\quad` (1em)، `\qquad` (2em)، `\,` (مسافة رفيعة).

---

## إضافة فصل جديد

### الخطوة 1: أنشئ ملف الفصل

أنشئ ملفاً جديداً في `chapters/` باسم `chapterN.tex` (مثلاً `chapter7.tex`):

```latex
%==============================================================================
% Chapter 7 — New Chapter Title
%==============================================================================
\chapter[English Title]{العنوان بالعربية}
\label{ch:new-chapter}
\markboth{الفصل السابع: العنوان بالعربية}{الفصل السابع: العنوان بالعربية}

%------------------------------------------------------------------------------
\section{مقدمة الفصل}
\label{sec:new-intro}

اكتب هنا مقدمة الفصل...

%------------------------------------------------------------------------------
\section{القسم الأول}
\label{sec:new-section1}

اكتب هنا محتوى القسم الأول...
```

### الخطوة 2: أضف الفصل لـ `main.tex`

افتح `main.tex` وابحث عن قسم `Main matter`، ثم أضف سطر الإدخال:

```latex
\input{chapters/chapter1}
\input{chapters/chapter2}
\input{chapters/chapter3}
\input{chapters/chapter4}
\input{chapters/chapter5}
\input{chapters/chapter6}
\input{chapters/chapter7}     % ← أضف هذا السطر
```

### ملاحظات:
- **`[English Title]`** يُستخدم في فاصل الفصل (صفحة الفصل المستقلة) وفي عنوان جانبي للصفحات.
- **`{العنوان بالعربية}`** يُستخدم في فهرس المحتويات وفاصل الفصل.
- **`\label{ch:...}`** يُستخدم للإشارة للفصل من أي مكان عبر `\ref{ch:...}`.
- **`\markboth{...}{...}`** يضبط الترويسة العلوية للصفحات داخل الفصل.
- **ترتيب الفصول** يتبع ترتيب `\input{}` في `main.tex`، ليس اسم الملف.

---

## إضافة قسم أو قسم فرعي

```latex
\section{عنوان القسم (\EN{Section Title})}
\label{sec:my-section}

\subsection{عنوان القسم الفرعي (\EN{Subsection})}
\label{subsec:my-subsection}

\subsubsection{عنوان قسم فرعي ثانٍ}
\label{subsubsec:my-subsubsection}
```

**التسلسل:**
- `\section` → رقم مثل `1.1`
- `\subsection` → رقم مثل `1.1.1`
- `\subsubsection` → رقم مثل `1.1.1.1` (بدون رقم افتراضياً، يُفعّل عبر `titlesec`)

**اصطلاحات التسمية:**
- استخدم `\label{sec:...}` للأقسام.
- استخدم `\label{subsec:...}` للأقسام الفرعية.
- استخدم `\label{fig:...}` للصور، `\label{tab:...}` للجداول، `\label{eq:...}` للمعادلات.

**للإشارة لقسم:**
```latex
كما ناقشنا في القسم~\ref{sec:my-section}، فإن...
```
> الـ `~` يمنع كسر السطر بين كلمة "القسم" والرقم.

---

## إضافة صورة

### الخطوة 1: ضع ملف الصورة في `figures/`

أسماء الصور يجب أن تكون وصفية (وليس `image1.png`، `image2.png`...). أمثلة:
- `usecase-diagram.png`
- `erd-schema.png`
- `agent-architecture.png`

الصيغ المدعومة: `.png`، `.jpg`/`.jpeg`، `.pdf`، `.eps`.

### الخطوة 2: اكتب كود LaTeX

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.8\textwidth]{usecase-diagram.png}
  \caption{مخطط حالات الاستخدام لنظام بيان.}
  \label{fig:usecase}
\end{figure}
```

**خيارات الموضع `[!htbp]`:**
- `h` = here (هنا)
- `t` = top (أعلى الصفحة)
- `b` = bottom (أسفل الصفحة)
- `p` = page (صفحة منفصلة للصور)
- `!` = تجاهل قيود LaTeX الداخلية

**أحجام شائعة:**
- `width=0.5\textwidth` (نصف عرض الصفحة)
- `width=0.8\textwidth` (80% من العرض)
- `width=\textwidth` (عرض كامل)
- `height=5cm` (ارتفاع ثابت)
- `scale=0.5` (نصف الحجم الأصلي)

**الإشارة للصورة:**
```latex
كما يوضح الشكل~\ref{fig:usecase}، فإن...
```

### لإضافة صورة بدون رقم (مثل الشعار):

```latex
\begin{center}
  \includegraphics[width=3cm]{logo-bayan.png}
\end{center}
```

---

## إضافة جدول

### جدول بسيط (tabular)

```latex
\begin{table}[!htbp]
  \centering
  \caption{عنوان الجدول.}
  \label{tab:my-table}
  \renewcommand{\arraystretch}{1.4}  % ارتفاع الصفوف
  \begin{tabular}{|c|l|r|}
    \hline
    \textbf{العمود 1} & \textbf{العمود 2} & \textbf{العمود 3} \\
    \hline
    قيمة 1 & قيمة 2 & 100 \\
    \hline
    قيمة 3 & قيمة 4 & 200 \\
    \hline
  \end{tabular}
\end{table}
```

**أنواع الأعمدة:**
- `c` = وسط (center)
- `l` = يسار (left)
- `r` = يمين (right)
- `p{3cm}` = عمود بعرض 3cm مع التفاف النص
- `|` = خط عمودي فاصل

### جدول متقدم (tabularx) — للأعمدة المرنة

```latex
\begin{table}[!htbp]
  \centering
  \caption{جدول بأعمدة مرنة.}
  \label{tab:flexible}
  \small
  \begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{3cm}|>{\raggedright\arraybackslash}X|}
    \hline
    \textbf{العنصر} & \textbf{الوصف} \\
    \hline
    NL2SQL & تحويل اللغة الطبيعية إلى استعلامات SQL. \\
    \hline
    RAG & الاسترجاع المعزز بالتوليد للبحث في المستندات. \\
    \hline
  \end{tabularx}
\end{table}
```

> عمود `X` يأخذ العرض المتبقي تلقائياً. مثالي للنصوص الطويلة.

### جدول طويل يتعدى صفحة (longtable)

```latex
\begin{longtable}{|>{\raggedright\arraybackslash}p{5cm}|>{\raggedright\arraybackslash}p{8cm}|}
\hline
\textbf{البرنامج} & \textbf{الاستخدام} \\
\hline
\endhead

Python & لغة البرمجة الأساسية. \\
\hline
FastAPI & إطار عمل الواجهة الخلفية. \\
\hline

\caption{الأدوات البرمجية.}
\label{tab:software}
\end{longtable}
```

**الإشارة للجدول:**
```latex
كما هو موضح في الجدول~\ref{tab:my-table}، فإن...
```

---

## إضافة قائمة نقطية أو رقمية

### قائمة نقطية (itemize)

```latex
\begin{itemize}
  \item \textbf{العنصر الأول:} شرح تفصيلي للعنصر الأول.
  \item \textbf{العنصر الثاني:} شرح تفصيلي للعنصر الثاني.
  \item \textbf{العنصر الثالث:} شرح تفصيلي للعنصر الثالث.
\end{itemize}
```

### قائمة رقمية (enumerate)

```latex
\begin{enumerate}
  \item الخطوة الأولى: كتابة الكود.
  \item الخطوة الثانية: اختبار الوحدة.
  \item الخطوة الثالثة: النشر.
\end{enumerate}
```

### قائمة وصفية (description)

```latex
\begin{description}
  \item[LLM] النموذج اللغوي الكبير.
  \item[RAG] الاسترجاع المعزز بالتوليد.
  \item[NL2SQL] تحويل اللغة الطبيعية إلى SQL.
\end{description}
```

### قائمة متداخلة

```latex
\begin{itemize}
  \item فئة رئيسية
    \begin{itemize}
      \item عنصر فرعي 1
      \item عنصر فرعي 2
    \end{itemize}
  \item فئة رئيسية أخرى
\end{itemize}
```

---

## إضافة كود برمجي

### كود مضمّن (inline)

```latex
استخدم الأمر \CODE{print("hello")} لطباعة نص.
```

> الأمر `\CODE{}` معرّف في `main.tex` ويستخدم خط DejaVu Sans Mono.

### كود في كتلة منفصلة (verbatim)

```latex
\begin{verbatim}
def hello():
    print("Hello, World!")

hello()
\end{verbatim}
```

### كود مع تنسيق (lstlisting) — يتطلب حزمة `listings`

```latex
\usepackage{listings}
\usepackage{xcolor}

\lstdefinestyle{python}{
  language=Python,
  basicstyle=\ttfamily\small,
  keywordstyle=\color{blue}\bfseries,
  commentstyle=\color{green!50!black},
  stringstyle=\color{red!70!black},
  showstringspaces=false,
  numbers=left,
  numberstyle=\tiny\color{gray},
  frame=single,
  breaklines=true,
}

\begin{lstlisting}[style=python, caption={مثال على دالة بسيطة.}, label={lst:hello}]
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

print(greet("Bayan"))
\end{lstlisting}
```

### كود من ملف خارجي

```latex
\lstinputlisting[style=python, caption={الكود الكامل للوكيل.}]{code/agent.py}
```

---

## إضافة معادلة رياضية

### معادلة مضمّنة (inline)

```latex
السرعة تُحسب بالعلاقة $v = d / t$ حيث $d$ المسافة و $t$ الزمن.
```

### معادلة في سطر منفصل (display)

```latex
\[
  E = mc^2
\]
```

### معادلة مرقمة (equation)

```latex
\begin{equation}
  \label{eq:quadratic}
  x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\end{equation}
```

**الإشارة للمعادلة:**
```latex
كما في المعادلة~\ref{eq:quadratic}، فإن...
```

### معادلات متعددة محاذية (align)

```latex
\begin{align}
  y &= mx + b \\
  a^2 + b^2 &= c^2 \\
  \sin^2\theta + \cos^2\theta &= 1
\end{align}
```

**رموز رياضية شائعة:**
| الرمز | الكود |
|-------|-------|
| $\alpha$ | `\alpha` |
| $\beta$ | `\beta` |
| $\gamma$ | `\gamma` |
| $\sum$ | `\sum` |
| $\prod$ | `\prod` |
| $\int$ | `\int` |
| $\leq$ | `\leq` |
| $\geq$ | `\geq` |
| $\neq$ | `\neq` |
| $\approx$ | `\approx` |
| $\infty$ | `\infty` |
| $\sqrt{x}$ | `\sqrt{x}` |
| $\frac{a}{b}$ | `\frac{a}{b}` |
| $x^{n}$ | `x^{n}` |
| $x_{i}$ | `x_{i}` |

---

## إضافة مرجع

### الطريقة 1: قائمة المراجع اليدوية (الحالية)

افتح `references_manual.tex` وأضف مُدخلاً جديداً:

```latex
\bibitem{key2024}
\textenglish{Author Name, ``Paper Title,'' \textit{Journal Name}, vol.~X, no.~Y, pp.~1--10, 2024. [Online]. Available: \url{https://example.com}}
```

ثم استشهد به في النص:

```latex
كما ذكر \EN{Author}~\cite{key2024}، فإن...
```

**أنواع المراجع الشائعة:**

**ورقة بحثية:**
```latex
\bibitem{vaswani2017attention}
\textenglish{A. Vaswani, N. Shazeer, et al., ``Attention Is All You Need,'' in \textit{Advances in Neural Information Processing Systems (NeurIPS)}, vol.~30, 2017, pp.~5998--6008.}
```

**كتاب:**
```latex
\bibitem{russell2020ai}
\textenglish{S. Russell and P. Norvig, \textit{Artificial Intelligence: A Modern Approach}, 4th ed. Pearson, 2020.}
```

**صفحة ويب:**
```latex
\bibitem{langchain2023}
\textenglish{LangChain, ``LangChain: Building Applications with LLMs through Composability,'' 2023. [Online]. Available: \url{https://github.com/langchain-ai/langchain}}
```

**رسالة ماجستير/دكتوراه:**
```latex
\bibitem{althani2023thesis}
\textenglish{M. Al-Thani, ``Arabic Natural Language Processing for Chatbots,'' Ph.D. dissertation, University of Qatar, 2023.}
```

### الطريقة 2: BibLaTeX + biber (متقدمة)

لتفعيلها:
1. في `main.tex`، أضف في الـ preamble:
   ```latex
   \usepackage[backend=biber, style=ieee, sorting=none]{biblatex}
   \addbibresource{references.bib}
   ```
2. استبدل `\input{references_manual}` بـ `\printbibliography` في نهاية المستند.
3. أضف المراجع في `references.bib` بصيغة BibTeX:
   ```bibtex
   @article{vaswani2017attention,
     author  = {Vaswani, Ashish and Shazeer, Noam and others},
     title   = {Attention Is All You Need},
     journal = {Advances in Neural Information Processing Systems},
     volume  = {30},
     pages   = {5998--6008},
     year    = {2017}
   }
   ```
4. رُم بـ:
   ```bash
   xelatex main.tex
   biber main
   xelatex main.tex
   xelatex main.tex
   ```

---

## إضافة اختصار

افتح `frontmatter/abbreviations.tex` وأضف سطراً للجدول:

```latex
\EN{API}  & واجهة برمجة التطبيقات التي تتيح التواصل بين الأنظمة المختلفة. \\
\hline
\EN{REST} & نمط معماري لبناء واجهات الويب (\EN{Representational State Transfer}). \\
\hline
```

> ترتيب الاختصارات أبجدي (مهم للاحترافية).

---

## إدراج نص إنجليزي داخل سياق عربي

استخدم الأمر `\EN{}` (المعرّف في `main.tex`):

```latex
يعتمد النظام على إطار عمل \EN{FastAPI} لتطوير الواجهة الخلفية،
ويستخدم \EN{LangGraph} لتنسيق الوكلاء.
```

الأمر `\EN{}` يُحوّل النص تلقائياً لاتجاه LTR مع خط Liberation Serif.

**لإدراج نص إنجليزي بدون تنسيق خاص:**
```latex
\textenglish{English text here}
```

**لإدراج رابط:**
```latex
\url{https://github.com/GP-Project-ust/Bayan-Documentation}
```

أو:
```latex
\href{https://github.com/GP-Project-ust/Bayan-Documentation}{Bayan-Documentation}
```

---

## تنسيقات نصية شائعة

| التنسيق | الكود | المثال |
|---------|------|--------|
| **عريض** | `\textbf{نص}` | **نص** |
| *مائل* | `\textit{نص}` أو `\emph{نص}` | *نص* |
| مسطر | `\underline{نص}` | <u>نص</u> |
| `monospace` | `\texttt{نص}` أو `\CODE{نص}` | `نص` |
| نص ملون | `{\color{red}نص}` | نص (أحمر) |
| حجم أكبر | `{\large نص}` | نص (أكبر) |
| حجم أصغر | `{\small نص}` | نص (أصغر) |
| نص إنجليزي | `\EN{English}` | English |
| اقتباس | `` ``نص'' `` | "نص" |
| علامة تجارية | `Microsoft\textsuperscript{\textregistered}` | Microsoft® |
| حقوق محفوظة | `\textcopyright 2024` | © 2024 |

---

## مشكلة نسخ النص من PDF

### المشكلة

عند نسخ نص عربي من ملف PDF الناتج، قد تظهر رموز غريبة (مربعات صغيرة، نقاط، أو رموز غير مفهومة) في المحرر النصي.

### السبب

حزمة `bidi` (التي تدعم الاتجاه من اليمين لليسار) تُدرج أحرف تحكم Unicode غير مرئية في الـ PDF لضبط ترتيب النص بصرياً. هذه الأحرف:
- U+202A (LRE), U+202B (RLE), U+202C (PDF)
- U+202D (LRO), U+202E (RLO)
- U+200E (LRM), U+200F (RLM)

### الحلول

**الحل 1 — للمحررات الحديثة (Word, Google Docs, LibreOffice):**
> فقط انسخ والصق. هذه المحررات تتعامل مع الأحرف تلقائياً وتخفيها.

**الحل 2 — سكربت `strip-bidi.py`:**

```bash
# تنظيف ملف نصي
python3 scripts/strip-bidi.py input.txt -o clean.txt

# تنظيف من pdftotext مباشرة
pdftotext main.pdf - | python3 scripts/strip-bidi.py > clean.txt

# عرض عدد الأحرف المُزالة
pdftotext main.pdf - | python3 scripts/strip-bidi.py --count > /dev/null
```

**الحل 3 — من الحافظة (Linux):**
```bash
xclip -o | python3 scripts/strip-bidi.py | xclip -i
```

---

## التحقق من التغييرات قبل الرفع

### 1. ترجمة محلية للتأكد من السلامة

```bash
latexmk -xelatex main.tex
# أو
tectonic main.tex
```

### 2. افحص ملف PDF الناتج

```bash
# عرض معلومات PDF
pdfinfo main.pdf

# عرض عدد الصفحات
pdfinfo main.pdf | grep Pages

# فحص الخطوط المدمجة
pdffonts main.pdf
```

### 3. ابحث عن أخطاء شائعة

```bash
# ابحث عن إشارات مرجعية غير معرّفة (?? في PDF)
grep -E "\\\\ref\{|\\\\cite\{" main.tex chapters/*.tex | grep -v "label"

# ابحث عن الأقواس غير المتوازنة
grep -cE "\\{[^}]*$" chapters/*.tex
```

### 4. ارفع التعديلات

```bash
git add .
git commit -m "docs: وصف موجز للتعديلات"
git push origin main
```

عند الرفع، سيُشغّل GitHub Actions workflow تلقائياً ويعيد بناء PDF. تابع الحالة من:
`https://github.com/GP-Project-ust/Bayan-Documentation/actions`

---

## نصائح عامة

1. **استخدم UTF-8 دائماً:** كل الملفات بصيغة UTF-8 (الافتراضي في المحررات الحديثة).
2. **حافظ على أسطر قصيرة:** كل سطر ≤ 80 حرف لتسهيل المقارنة (diff) في git.
3. **اجعل كل جملة في سطر مستقل:** هذا يحسّن diff ويسهّل مراجعة التعديلات.
   ```latex
   هذا النص يتكون من جملة واحدة
   تمتد على عدة أسطر.
   
   هذه جملة جديدة.
   ```
4. **استخدم Labels دائماً:** لا تكتب "كما في الفصل 3"، بل "كما في الفصل~\ref{ch:analysis}".
5. **تجنب `\newline` و `\\` في النص العادي:** استخدم سطراً فارغاً للفقرات الجديدة.
6. **افحص ملف الـ log:** عند ظهور خطأ، افتح `main.log` وابحث عن `! ` (علامة تعجب + مسافة).
7. **لا تستخدم رموز Unicode غريبة:** مثل emoji 🎉 — فهي لا تظهر في PDF. استخدم بدائل LaTeX مثل `$\blacklozenge$` للماسات.

---

## المساعدة والأسئلة الشائعة

**س: كيف أغير اسم الطالب في الغلاف؟**
ج: افتح `frontmatter/cover.tex` وعدّل الأسطر التي تحتوي على الأسماء.

**س: كيف أضيف عضواً جديداً للفريق؟**
ج: عدّل 3 ملفات: `cover.tex` (الغلاف)، `declaration.tex` (جدول التوقيعات + جدول التأكيد بالرقم الجامعي).

**س: كيف أغيّر العنوان؟**
ج: في `main.tex`، عدّل `\thesisTitleAR` و `\thesisTitleEN`.

**س: كيف أضيف صورة بدون رقم أسفلها؟**
ج: استخدم `\begin{center}\includegraphics[...]{...}\end{center}` بدون `\caption`.

**س: كيف أجعل صورة تأخذ كامل عرض الصفحة؟**
ج: استخدم `width=\textwidth` في `\includegraphics`.

**س: كيف أضيف فهرساً للأكواد البرمجية؟**
ج: استخدم حزمة `listings` مع خيار `index=true` وراجع وثائقها.

**س: أين أجد الـ PDF الجاهز؟**
ج: بعد كل push لفرع `main`، يبني GitHub Actions الـ PDF تلقائياً ويرفعه كـ artifact في صفحة Actions، كما يعمل commit للـ PDF في المستودع نفسه.
