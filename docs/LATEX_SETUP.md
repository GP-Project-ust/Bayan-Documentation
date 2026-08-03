# 📐 دليل LaTeX والبيئة المحلية

> **دليل شامل لإعداد بيئة LaTeX محلية للعمل على مشروع بيان.**

---

## 🎯 الخيارات المتاحة

| الخيار | المميزات | العيوب | الأنسب لـ |
|--------|---------|--------|-----------|
| **Tectonic** (موصى به) | سريع، تلقائي، خفيف | يحتاج إنترنت أول مرة | الجميع |
| **TeX Live** | كامل، قياسي | ثقيل (~5GB) | من يريد تفاصيل |
| **Overleaf** | لا تثبيت، سهل | يحتاج إنترنت، محدود | للتعديلات السريعة |
| **Docker** | معزول، نظيف | يحتاج Docker | للمطورين |

---

## 🚀 الخيار 1: Tectonic (الموصى به — 5 دقائق)

### لماذا Tectonic؟
- ✅ سريع جداً (أسرع من XeLaTeX بـ 3x)
- ✅ يحمل الحزم تلقائياً عند الحاجة
- ✅ خفيف (~30MB فقط)
- ✅ يعمل على Windows/Mac/Linux
- ✅ يدعم XeLaTeX (الذي نستخدمه)

### التثبيت:

#### Windows:
```bash
# الطريقة 1: عبر Chocolatey
choco install tectonic

# الطريقة 2: تحميل مباشر
# نزّل من: https://github.com/tectonic-typesetting/tectonic/releases
# ضع tectonic.exe في C:\Windows\ أو أضفه لـ PATH
```

#### macOS:
```bash
# عبر Homebrew
brew install tectonic
```

#### Linux:
```bash
# عبر Snap
sudo snap install tectonic

# أو نزّل الـ binary
curl -LO https://github.com/tectonic-typesetting/tectonic/releases/latest/download/tectonic-0.14.1-x86_64-unknown-linux-musl.tar.gz
tar -xzf tectonic-*.tar.gz
sudo mv tectonic /usr/local/bin/
```

### الاستخدام:

```bash
# في مجلد المشروع
cd Bayan-Documentation

# ترجمة (ستحمل الحزم تلقائياً أول مرة)
tectonic main.tex

# النتيجة: main.pdf
```

### مزايا Tectonic:
- يكتشف الحزم الناقصة ويحمّلها
- يدير multiple passes تلقائياً (للفهرس والمراجع)
- يعطي رسائل خطأ واضحة

---

## 📦 الخيار 2: TeX Live (للتثبيت الكامل)

### التثبيت:

#### Windows:
1. نزّل من: https://tug.org/texlive/windows.html
2. شغّل `install-tl-windows.exe`
3. اختر **Install** (قد يستغرق ساعة+)
4. بعد التثبيت، أضف `C:\texlive\2024\bin\windows` لـ PATH

#### macOS:
1. نزّل MacTeX: https://www.tug.org/mactex/
2. شغّل المثبّت (~4GB)
3. أعد تشغيل الجهاز

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install texlive-full
# الحجم: ~5GB
```

### الاستخدام:

```bash
# ترجمة بسيطة (دورة واحدة)
xelatex main.tex

# ترجمة كاملة (للفهرس والمراجع)
xelatex main.tex
xelatex main.tex  # مرة ثانية لحل الفهرس

# أو استخدم latexmk (يدير الدورات تلقائياً)
latexmk -xelatex main.tex
```

### تثبيت الخطوط المطلوبة:

مشروعنا يستخدم خط **Amiri** و **Noto Naskh Arabic**:

#### Windows:
1. نزّل Amiri: https://github.com/aliftype/amiri/releases
2. نزّل Noto Naskh Arabic: https://fonts.google.com/noto/specimen/Noto+Naskh+Arabic
3. استخرج ملفات `.ttf` وافتحها (نقرة مزدوجة) → **Install**

#### macOS:
```bash
# عبر Homebrew
brew install --cask font-amiri
brew install --cask font-noto-naskh-arabic
```

#### Linux:
```bash
sudo apt install fonts-hosny-amiri fonts-noto-core
```

بعد تثبيت الخطوط، حدّث ذاكرة الخطوط:
```bash
# Linux
sudo fc-cache -f -v

# macOS
sudo fc-cache -f -v

# Windows: أعد تشغيل الجهاز
```

---

## ☁️ الخيار 3: Overleaf (بدون تثبيت)

### المميزات:
- ✅ لا تثبيت مطلوب
- ✅ يعمل في المتصفح
- ✅ تعاون مباشر (real-time)
- ✅ معاينة فورية للـ PDF

### العيوب:
- ❌ يحتاج إنترنت دائماً
- ❌ الخطة المجانية محدودة (50 مشروع)
- ❌ لا يدعم Git بشكل جيد

### الإعداد:

1. اذهب إلى: https://www.overleaf.com
2. أنشئ حساباً (مجاني)
3. اضغط **New Project → Upload Project**
4. ارفع ملف ZIP للمشروع:
   ```bash
   # في مجلد المشروع
   zip -r bayan-thesis.zip . -x ".git/*"
   ```
5. ارفع الـ ZIP إلى Overleaf
6. من **Menu**:
   - Compiler: **XeLaTeX**
   - Main document: `main.tex`
7. اضغط **Recompile**

### مزامنة مع GitHub:

Overleaf يدعم مزامنة مع GitHub (في الخطة المدفوعة):
1. في Overleaf: Menu → GitHub → Import from GitHub / Export to GitHub
2. اربط حساب GitHub

---

## 🐳 الخيار 4: Docker (للمطورين)

### المميزات:
- ✅ معزول (لا يلوث نظامك)
- ✅ قابل للتكرار (نفس بيئة CI)
- ✅ خفيف (الحجم يعتمد على الصورة)

### التثبيت:

1. ثبّت Docker: https://docs.docker.com/get-docker/
2. استخدم صورة TeX Live الرسمية:

```bash
# ترجمة المشروع
docker run --rm -v "$PWD":/work -w /work texlive/texlive xelatex main.tex

# أو استخدم tectonic (أخف)
docker run --rm -v "$PWD":/work -w /work dxsi/tectonic tectonic main.tex
```

### إنشاء alias (اختياري):

أضف لـ `~/.bashrc` أو `~/.zshrc`:

```bash
alias texlive='docker run --rm -v "$PWD":/work -w /work texlive/texlive'
alias tectonic-docker='docker run --rm -v "$PWD":/work -w /work dxsi/tectonic tectonic'

# الاستخدام:
texlive xelatex main.tex
tectonic-docker main.tex
```

---

## 🔧 إعداد VS Code (موصى به للتعديل)

VS Code هو أفضل محرر لـ LaTeX (مجاني، خفيف، قوي).

### 1. تثبيت VS Code:
- نزّل من: https://code.visualstudio.com/

### 2. تثبيت الإضافات:

افتح VS Code → Extensions (Ctrl+Shift+X) → ابحث عن:

| الإضافة | الوصف |
|--------|------|
| **LaTeX Workshop** | دعم LaTeX كامل (ترجمة، معاينة، تحقق) |
| **LaTeX language support** | تلوين بناء الجملة |
| **Prettier** | تنسيق الكود |
| **GitLens** | دعم Git متقدم |
| **Arabic** | دعم العربية |

### 3. إعدادات VS Code لـ LaTeX:

افترض أنك تستخدم Tectonic. أنشئ ملف `.vscode/settings.json` في مجلد المشروع:

```json
{
  "latex-workshop.latex.tools": [
    {
      "name": "tectonic",
      "command": "tectonic",
      "args": ["main.tex"],
      "args": ["--synctex", "--keep-logs"],
      "env": {}
    }
  ],
  "latex-workshop.latex.recipes": [
    {
      "name": "tectonic",
      "tools": ["tectonic"]
    }
  ],
  "latex-workshop.view.pdf.viewer": "tab",
  "latex-workshop.latex.autoBuild.run": "onSave",
  "editor.wordWrap": "on"
}
```

### 4. اختصارات مفيدة:

| الاختصار | الوظيفة |
|---------|--------|
| `Ctrl+Alt+B` | ترجمة (Build) |
| `Ctrl+Alt+V` | عرض PDF |
| `Ctrl+Alt+J` | الانتقال من الكود لـ PDF (SyncTeX) |
| `Ctrl+Alt+C` | مسح الملفات المؤقتة |

---

## 📝 كيف تعدّل ملف LaTeX

### فتح الملف:

```bash
# افتح المشروع في VS Code
code .

# أو افتح ملف محدد
code chapters/chapter3.tex
```

### بنية ملف LaTeX:

```latex
%==============================================================================
% Chapter 3 — Analysis
%==============================================================================
\chapter[Analysis]{المنهجية وتحليل النظام}
\label{ch:analysis}
\markboth{الفصل الثالث: المنهجية وتحليل النظام}{الفصل الثالث: المنهجية وتحليل النظام}

%------------------------------------------------------------------------------
\section{منهجية التطوير}
\label{sec:methodology}

هذا نص عربي عادي. يمكن كتابة عدة أسطر وسيدمجها LaTeX في فقرة واحدة.

هذه فقرة جديدة (مفصولة بسطر فارغ).

% إدراج نص إنجليزي
النظام يستخدم \EN{LangGraph} للتنسيق.

% قائمة نقطية
\begin{itemize}
  \item عنصر أول
  \item عنصر ثاني
  \item عنصر ثالث
\end{itemize}

% جدول
\begin{table}[!htbp]
  \centering
  \caption{عنوان الجدول.}
  \label{tab:my-table}
  \begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{3cm}|>{\raggedright\arraybackslash}X|}
    \hline
    \textbf{العنوان 1} & \textbf{العنوان 2} \\
    \hline
    قيمة 1 & شرح القيمة 1 \\
    \hline
  \end{tabularx}
\end{table}

% صورة
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.7\textwidth]{my-image.png}
  \caption{عنوان الصورة.}
  \label{fig:my-image}
\end{figure}

% إشارة
كما ناقشنا في القسم~\ref{sec:methodology}، فإن...
الجدول~\ref{tab:my-table} يوضح...
الشكل~\ref{fig:my-image} يبين...
```

### الأوامر المخصصة لمشروعنا:

| الأمر | الوصف | مثال |
|------|------|------|
| `\EN{text}` | نص إنجليزي | `يستخدم \EN{API} للاتصال` |
| `\CODE{code}` | كود برمجي | `استخدم \CODE{print("hello")}` |
| `\textbf{}` | نص عريض | `\textbf{مهم}` |
| `\textit{}` | نص مائل | `\textit{ملاحظة}` |
| `\ref{label}` | إشارة | `القسم~\ref{sec:methodology}` |
| `\cite{key}` | استشهاد | `\cite{vaswani2017attention}` |
| `\label{sec:...}` | تسمية قسم | `\label{sec:methodology}` |

---

## 🐛 استكشاف الأخطاء

### مشكلة: "Error: LaTeX Error: File `xxx.sty' not found"

**السبب:** حزمة LaTeX غير مثبتة.

**الحل (Tectonic):** تلقائي — ستحمل عند الحاجة.

**الحل (TeX Live):**
```bash
# ابحث عن الحزمة
tlmgr search --global --file "xxx.sty"

# ثبّتها
tlmgr install <package-name>
```

### مشكلة: "Error: fontspec Error: The font 'Amiri' cannot be found"

**السبب:** خط Amiri غير مثبت.

**الحل:** ثبّت الخط (راجع قسم "تثبيت الخطوط المطلوبة" أعلاه).

### مشكلة: "Overfull \hbox (XXpt too wide)"

**السبب:** نص أعرض من الصفحة.

**الحل:**
- قلّل حجم الخط: `{\small النص}`
- استخدم `tabularx` بدلاً من `tabular`
- أضف `\sloppy` أو `\hbadness=10000` (مؤقت)

### مشكلة: "Reference `xxx' on page X undefined"

**السبب:** `\label{}` غير معرّف أو الاسم خاطئ.

**الحل:**
1. ابحث عن الـ label: `grep -r "label{xxx}" chapters/`
2. تأكد أن الاسم صحيح
3. أعد الترجمة مرتين (للفهرس)

### مشكلة: "Unicode character xxx not set up for use with LaTeX"

**السبب:** حرف غير مدعوم.

**الحل:** استخدم XeLaTeX (نستخدمه بالفعل) — إن استمر، احذف الحرف.

### مشكلة: "PDF لم يُبنَ بعد push"

تحقق من [Actions](https://github.com/GP-Project-ust/Bayan-Documentation/actions):
1. ابحث عن آخر workflow
2. إن فشل، اقرأ السجل
3. ابحث عن `error:` أو `! `

أو اعرض الـ log محلياً:
```bash
tectonic main.tex 2>&1 | tee build.log
grep -E "^!|error" build.log
```

---

## 📊 أدوات مساعدة

### 1. مولد جداول LaTeX:

- https://www.tablesgenerator.com/latex_tables
- أنشئ جدولاً بصرياً → انسخ كود LaTeX

### 2. محرر معادلات LaTeX:

- https://latex.codecogs.com/editor.html
- اكتب المعادلة → انسخ الكود

### 3. مدقق إملائي عربي:

- https://www.grammarly.com/ (للإنجليزية)
- https://alsharekh.org/ (للعربية)

### 4. محول Markdown → LaTeX:

- https://pandoc.org/
```bash
pandoc input.md -o output.tex
```

---

## ✅ Checklist قبل الترجمة النهائية

قبل كل commit، تأكد من:

- [ ] `tectonic main.tex` ينجح بدون أخطاء
- [ ] لا توجد `?` في الإشارات (`\ref{}` تعمل)
- [ ] لا توجد Overfull hbox كبيرة (> 10pt)
- [ ] PDF يفتح بشكل صحيح
- [ ] الفهرس محدّث
- [ ] قائمة الأشكال/الجداول محدّثة

### سكربت فحص سريع:

```bash
#!/bin/bash
# check.sh — فحص سريع قبل الـ commit

echo "=== Compiling... ==="
tectonic main.tex 2>&1 | tee /tmp/build.log

echo ""
echo "=== Checking for errors ==="
if grep -q "^!" /tmp/build.log; then
  echo "❌ Errors found:"
  grep "^!" /tmp/build.log
  exit 1
else
  echo "✅ No errors"
fi

echo ""
echo "=== Checking for undefined references ==="
if grep -q "undefined" /tmp/build.log; then
  echo "⚠️  Undefined references:"
  grep "undefined" /tmp/build.log
else
  echo "✅ All references defined"
fi

echo ""
echo "=== Checking for Overfull boxes ==="
OVERFULL=$(grep -c "Overfull" /tmp/build.log)
if [ "$OVERFULL" -gt 5 ]; then
  echo "⚠️  $OVERFULL Overfull boxes (consider fixing)"
else
  echo "✅ $OVERFULL Overfull boxes (acceptable)"
fi

echo ""
echo "=== Done ==="
ls -la main.pdf
```

احفظه كـ `check.sh` وشغّله:
```bash
chmod +x check.sh
./check.sh
```

---

## 📚 مراجع لـ LaTeX

- [Overleaf Documentation](https://www.overleaf.com/learn) — شامل جداً
- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)
- [The Not So Short Introduction to LaTeX](https://tobi.oetiker.ch/lshort/lshort.pdf)
- [Arabic LaTeX Guide](https://github.com/aliftype/amiri/wiki)

---

## 🆘 المساعدة

إن واجهت مشكلة:
1. ابحث في [Overleaf Documentation](https://www.overleaf.com/learn)
2. ابحث في [Stack Exchange](https://tex.stackexchange.com/)
3. اسأل في Discord
4. افتح Issue بـ label `bug`
