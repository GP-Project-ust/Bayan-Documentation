# 👥 دليل أعضاء الفريق (Member Guide)

> **هذا الدليل لكل أعضاء الفريق.**
> اقرأه كاملاً قبل البدء بأي مهمة.

---

## 📌 روابط مهمة

| الرابط | الوصف |
|--------|------|
| https://github.com/GP-Project-ust/Bayan-Documentation | المستودع الرئيسي |
| https://github.com/orgs/GP-Project-ust/projects/4 | لوحة المشروع (Board) |
| https://github.com/GP-Project-ust/Bayan-Documentation/issues | المهام (Issues) |
| https://github.com/GP-Project-ust/Bayan-Documentation/pulls | طلبات الدمج (PRs) |

---

## 🚀 الإعداد الأولي (مرة واحدة — 30 دقيقة)

### 1. تثبيت Git

#### على Windows:
1. نزّل Git من: https://git-scm.com/download/win
2. شغّل المثبّت (اترك الإعدادات الافتراضية)
3. تحقق: افتح **Command Prompt** واكتب:
   ```bash
   git --version
   ```
   يجب أن يظهر: `git version 2.XX.X`

#### على macOS:
```bash
# إن لم يكن مثبتاً
xcode-select --install
```

#### على Linux:
```bash
sudo apt install git       # Ubuntu/Debian
sudo dnf install git       # Fedora
```

### 2. إنشاء حساب GitHub

1. اذهب إلى: https://github.com/signup
2. أنشئ حساباً باسمك الحقيقي (مثل: `ahmed-mutawakel`)
3. أضف صورتك الشخصية (مهم للتعرف)
4. أضف بريدك الإلكتروني

### 3. قبول دعوة المستودع

1. ستصلك دعوة بالبريد أو إشعار في GitHub
2. اقبل الدعوة لتصبح عضواً في `GP-Project-ust`

### 4. إعداد Git محلياً

افتح **Terminal** (أو Git Bash على Windows) واكتب:

```bash
# اسمك وبريدك (نفس بريد GitHub)
git config --global user.name "اسمك الكامل"
git config --global user.email "your-email@example.com"

# تفعيل دعم العربية في أسماء الملفات
git config --global core.quotepath false

# تعيين المحرر الافتراضي (اختياري)
git config --global core.editor "code --wait"  # لـ VS Code
```

### 5. إنشاء Personal Access Token

GitHub لم يعد يدعم كلمات المرور للـ push. تحتاج Token:

1. اذهب إلى: https://github.com/settings/tokens
2. انقر **Generate new token (classic)**
3. اكتب Note: `Bayan thesis`
4. مدة الصلاحية: 90 يوماً (أو أكثر)
5. اختر الصلاحيات:
   - ✅ `repo` (كامل)
   - ✅ `workflow`
6. انقر **Generate token**
7. **انسخ الـ Token** (لن تراه مرة أخرى!)
8. احفظه في مكان آمن

### 6. استنساخ المستودع

```bash
# أنشئ مجلد للمشاريع
mkdir ~/projects
cd ~/projects

# استنساخ المستودع
git clone https://github.com/GP-Project-ust/Bayan-Documentation.git

# ادخل إلى المجلد
cd Bayan-Documentation

# تحقق
git branch
# يجب أن يظهر: * main
```

عند الـ clone، ستحتاج لإدخال:
- Username: اسم مستخدم GitHub
- Password: الـ Token الذي أنشأته (ليس كلمة مرور GitHub)

### 7. تثبيت LaTeX (للتعديل المحلي)

#### الخيار 1: TeX Live (موصى به — عبر Docker)

```bash
# تثبيت Docker من: https://docs.docker.com/get-docker/

# بعد تثبيت Docker، شغّل:
docker run --rm -v "$PWD":/work -w /work texlive/texlive xelatex main.tex
```

#### الخيار 2: TeX Live محلياً (ثقيل ~5GB)

- **Windows:** نزّل من https://tug.org/texlive/ وشغّل `install-tl-windows.exe`
- **macOS:** نزّل MacTeX من https://www.tug.org/mactex/
- **Linux:** `sudo apt install texlive-full`

#### الخيار 3: استخدام Overleaf (أسهل — بدون تثبيت)

1. اذهب إلى: https://www.overleaf.com
2. أنشئ حساباً
3. ارفع ملف ZIP للمشروع
4. عدّل في المتصفح مباشرة
5. اختر Compiler: **XeLaTeX**

> **ملاحظة:** لتعديلات بسيطة، استخدم Overleaf. لتعديلات كبيرة أو اختبار كامل، استخدم التثبيت المحلي.

---

## 🌖 سير العمل اليومي (Daily Workflow)

### 1. ابدأ يومك بتحديث المستودع

```bash
# انتقل لفرع main
git checkout main

# اسحب آخر التحديثات
git pull origin main
```

### 2. تحقق من مهامك

1. اذهب إلى [Issues](https://github.com/GP-Project-ust/Bayan-Documentation/issues)
2. ابحث عن Issues مسندة إليك (Assignees: you)
3. أو اذهب إلى [Project Board](https://github.com/orgs/GP-Project-ust/projects/4) واعرض "Todo"

### 3. ابدأ العمل على مهمة

```bash
# أنشئ فرعاً جديداً (مهم جداً!)
git checkout -b ch3/section-3.3-ahmed

# غيّر status في الـ Board:
# اذهب لـ Project Board → اسحب البطاقة لـ "In Progress"
# أو في الـ Issue: غيّر Label من status: ready لـ status: in-progress
```

### 4. اعمل على الملفات

افترض أنك تعمل على `chapters/chapter3.tex`:

```bash
# افتح الملف في محررك (VS Code مثلاً)
code chapters/chapter3.tex

# اكتب/عدّل المحتوى...
# احفظ الملف
```

### 5. اختبر الترجمة (إن أمكن)

```bash
# إن كان لديك LaTeX مثبت:
xelatex main.tex
xelatex main.tex  # مرتين لحل الفهرس

# أو استخدم latexmk:
latexmk -xelatex main.tex

# أو استخدم Tectonic (أبسط):
# نزّله من: https://tectonic-typesetting.github.io/
tectonic main.tex
```

### 6. احفظ التغييرات (Commit)

```bash
# شاهد ما الذي تغيّر
git status

# شاهد التفاصيل
git diff

# أضف الملفات المعدّلة
git add chapters/chapter3.tex

# أو أضف كل شيء
git add .

# احفظ (commit) برسالة واضحة
git commit -m "feat: add §3.3 functional requirements FR-01 to FR-05 (refs #3)"
```

#### صيغة رسالة الـ Commit:

```
<type>: <description> (refs #XX)
```

| النوع | الاستخدام |
|------|-----------|
| `feat` | إضافة ميزة/قسم جديد |
| `fix` | إصلاح خطأ |
| `docs` | توثيق |
| `style` | تنسيق فقط |
| `refactor` | إعادة هيكلة |

**أمثلة:**
- `feat: add §3.3 functional requirements (refs #3)`
- `fix: correct table overflow in §3.2 (refs #2)`
- `docs: update README with new structure`

### 7. ارفع التغييرات (Push)

```bash
# ارفع فرعك إلى GitHub
git push origin ch3/section-3.3-ahmed

# المرة الأولى لهذا الفرع، استخدم -u:
git push -u origin ch3/section-3.3-ahmed
```

### 8. افتح Pull Request

1. اذهب إلى: https://github.com/GP-Project-ust/Bayan-Documentation/pulls
2. انقر **New pull request**
3. اختر فرعك (`ch3/section-3.3-ahmed`) مقارنة بـ `main`
4. اكتب العنوان: `[§3.3] تحليل المتطلبات الوظيفية وغير الوظيفية`
5. في الوصف، اكتب:
   ```markdown
   ## 📌 الوصف
   إضافة قسم §3.3 تحليل المتطلبات (30 FR + 20 NFR).

   ## 🔗 Issue المرتبط
   Closes #3

   ## ✅ Checklist
   - [x] الترجمة ناجحة
   - [x] تمت المراجعة الذاتية
   - [x] الإشارات المتقاطعة تعمل
   ```
6. في الجهة اليمنى:
   - **Reviewers:** اختر عضوين على الأقل
   - **Labels:** `status: needs-review`
   - **Milestone:** `الفصل الثالث — التحليل`
7. انقر **Create pull request**

### 9. حدّث الـ Board

في [Project Board](https://github.com/orgs/GP-Project-ust/projects/4):
- اسحب البطاقة لـ **Review**

### 10. أرسل إشعاراً

في Discord/Telegram:
```
PR #XX جاهز للمراجعة: [رابط]
القسم: §3.3 تحليل المتطلبات
الرجاء المراجعة في أقرب وقت.
```

---

## 🔍 كيف تراجع PR لزميل؟

### الخطوات:

1. اذهب إلى [Pull Requests](https://github.com/GP-Project-ust/Bayan-Documentation/pulls)
2. اختر PR تراجعه
3. انقر **Files changed**
4. راجع كل تغيير:
   - الأخضر (+) = مضاف
   - الأحمر (-) = محذوف
5. للتعلّق على سطر:
   - مرّر فوقه
   - انقر **+** الأزرق
   - اكتب تعليقك
   - انقر **Add single comment** أو **Start a review**
6. عند الانتهاء، انقر **Review changes** (أعلى الصفحة):
   - **Comment**: تعليقات فقط
   - **Approve**: موافقة (جاهز للدمج)
   - **Request changes**: يحتاج تعديل

### قواعد المراجعة:

- ✅ كن بنّاءً (لا تنتقد، اقترح)
- ✅ كن محدداً (أشر للسطر بالضبط)
- ✅ اشرح السبب (وليس فقط "غيّر هذا")
- ✅ مدح الجيد قبل نقد السيء
- ❌ لا تكن قاسياً
- ❌ لا تتجاهل
- ❌ لا تؤجل (راجع خلال 24 ساعة)

### مثال على تعليق جيد:
```
✅ ممتاز: تنظيم الجدول واضح والتصنيف منطقي.

💡 اقتراح: في السطر 45، قد يكون من الأفضل استخدام \textbf{} 
لإبراز أسماء الوكلاء (Supervisor Agent) كما هو الحال في §1.5.

❓ سؤال: هل يوجد سبب لاستخدام tabularx بدلاً من tabular 
في الجدول الكبير؟ قد يسبب overflow.
```

---

## 🌿 إدارة الفروع (Branches)

### قاعدة ذهبية:
> **لا تعمل أبداً على فرع `main` مباشرة.**

### إنشاء فرع جديد:

```bash
# من main محدّث
git checkout main
git pull origin main

# أنشئ فرعاً جديداً
git checkout -b ch3/section-3.3-ahmed
```

### قواعد التسمية:

| النوع | الصيغة | مثال |
|------|--------|------|
| قسم فصل | `chX/section-X.Y-name` | `ch3/section-3.3-ahmed` |
| إصلاح | `fix/issue-XX-desc` | `fix/issue-12-table` |
| توثيق | `docs/description` | `docs/update-readme` |

### التبديل بين الفروع:

```bash
# شاهد كل الفروع
git branch

# انتقل لفرع
git checkout ch3/section-3.3-ahmed

# ارجع لـ main
git checkout main
```

### مزامنة فرعك مع main:

عندما يتم دمج تغييرات في main من قبل آخرين:

```bash
# على فرعك
git checkout ch3/section-3.3-ahmed

# اسحب آخر main
git fetch origin

# ادمج main في فرعك
git merge origin/main

# أو استخدم rebase (أنظف تاريخاً)
git rebase origin/main

# ارفع
git push origin ch3/section-3.3-ahmed
```

### حذف فرع بعد الدمج:

```bash
# بعد دمج PR، احذف الفرع محلياً
git checkout main
git pull origin main
git branch -d ch3/section-3.3-ahmed

# أو احذفه من GitHub أيضاً
git push origin --delete ch3/section-3.3-ahmed
```

---

## 📝 التعامل مع LaTeX

### بنية المشروع:

```
Bayan-Documentation/
├── main.tex                  ← الملف الرئيسي
├── chapters/
│   ├── chapter1.tex          ← الفصل الأول (مكتمل)
│   ├── chapter2.tex          ← الفصل الثاني (مكتمل)
│   ├── chapter3.tex          ← الفصل الثالث (ستعمل عليه)
│   └── ...
├── frontmatter/
│   ├── cover.tex             ← الغلاف
│   ├── abstract.tex          ← الملخص
│   └── ...
├── figures/                  ← الصور
├── references_manual.tex     ← المراجع
└── .latexmkrc                ← إعداد الترجمة
```

### كيف تعدّل ملف LaTeX:

1. افتح الملف في محرر:
   - **VS Code** (مع إضافة LaTeX Workshop) — موصى به
   - **TeXstudio** — ممتاز لـ LaTeX
   - **Overleaf** — عبر المتصفح
   - **Sublime Text** + LaTeXTools

2. اكتب المحتوى بالعربية مع استخدام الأوامر:

```latex
\section{عنوان القسم} \label{sec:my-section}

هذا نص عربي عادي. يمكن إدراج كلمة إنجليزية: \EN{API}.

\begin{itemize}
  \item عنصر أول
  \item عنصر ثاني
\end{itemize}

\begin{table}[!htbp]
  \centering
  \caption{عنوان الجدول}
  \label{tab:my-table}
  \begin{tabularx}{\textwidth}{|X|c|}
    \hline
    \textbf{العمود 1} & \textbf{العمود 2} \\
    \hline
    قيمة 1 & 100 \\
    \hline
  \end{tabularx}
\end{table}
```

### أوامر مهمة في مشروعنا:

| الأمر | الاستخدام |
|------|----------|
| `\EN{text}` | نص إنجليزي وسط عربي |
| `\CODE{code}` | كود برمجي |
| `\ref{label}` | إشارة لقسم/جدول/شكل |
| `\cite{key}` | استشهاد بمرجع |
| `\label{sec:...}` | تسمية للإشارة |
| `\textbf{text}` | نص عريض |
| `\textit{text}` | نص مائل |

### اختبر ترجمتك:

قبل فتح PR، تأكد أن الكود يُترجم بدون أخطاء:

```bash
# الطريقة 1: tectonic (الأسرع)
tectonic main.tex

# الطريقة 2: latexmk
latexmk -xelatex main.tex

# الطريقة 3: xelatex يدوياً
xelatex main.tex
xelatex main.tex  # مرتين لحل الفهرس
```

إن ظهر خطأ، ابحث في `main.log` عن `! `:

```bash
grep "^!" main.log
```

---

## 🚫 مشاكل شائعة وحلولها

### مشكلة: "Git يرفض الـ push"

```
! [rejected] main -> main (fetch first)
```

**الحل:**
```bash
git pull origin main
# حل التعارضات إن وجدت
git push origin main
```

### مشكلة: "نسيت إنشاء فرع"

```bash
# عملت على main بدلاً من فرع
# أنشئ فرعاً من التغييرات الحالية
git checkout -b ch3/section-3.3-ahmed
git add .
git commit -m "feat: add §3.3 (refs #3)"
git push -u origin ch3/section-3.3-ahmed

# أعد main لحالته
git checkout main
git reset --hard origin/main
```

### مشكلة: "تعارض في الدمج"

عندما يظهر:
```
CONFLICT (content): Merge conflict in chapters/chapter3.tex
```

**الحل:**
1. افتح الملف في محررك
2. ابحث عن `<<<<<<<` و `=======` و `>>>>>>>`
3. احذف العلامات واحتفظ بالنسخة الصحيحة
4. احفظ
5. ثم:
```bash
git add chapters/chapter3.tex
git commit
git push
```

### مشكلة: "PDF لم يُبنَ بعد الدمج"

1. اذهب إلى [Actions](https://github.com/GP-Project-ust/Bayan-Documentation/actions)
2. ابحث عن آخر workflow
3. إن فشل، اقرأ السجل وابحث عن `error:`
4. افتح Issue بـ label `bug`

---

## 📋 قائمة التحقق قبل فتح PR (Checklist)

قبل فتح Pull Request، تأكد من:

- [ ] الكود يُترجم بدون أخطاء (`tectonic main.tex` ينجح)
- [ ] لا توجد أخطاء Overfull hbox كبيرة
- [ ] الإشارات المتقاطعة تعمل (`\ref{}` لا تُرجع `??`)
- [ ] كل جدول/شكل له `\label{}`
- [ ] استخدمت `[!htbp]` لكل figures/tables
- [ ] راجعت الكود بنفسي (self-review)
- [ ] رسالة الـ commit واضحة وبالصيغة الصحيحة
- [ ] ربطت الـ PR بالـ Issue (`Closes #XX`)
- [ ] حددت Reviewers (عضوين على الأقل)
- [ ] غيّرت Label إلى `status: needs-review`
- [ ] حدّثت الـ Board (نقلت البطاقة لـ Review)

---

## 💬 التواصل

### متى تستخدم GitHub Issues؟
- للمهام الرسمية
- للأخطاء (bugs)
- لطلب مراجعة

### متى تستخدم Discord/Telegram؟
- للأسئلة السريعة
- للتنسيق اليومي
- للمساعدة العاجلة

### متى تستخدم GitHub Discussions؟
- للأسئلة العامة
- للنقاشات الطويلة
- لاقتراحات الأفكار

---

## 🆘 عند الحاجة للمساعدة

1. **ابحث أولاً** في:
   - [PROJECT_RULES.md](../PROJECT_RULES.md)
   - [CONTRIBUTING.md](../CONTRIBUTING.md)
   - [Issues](https://github.com/GP-Project-ust/Bayan-Documentation/issues) الموجودة

2. **اسأل الفريق** في Discord/Telegram

3. **افتح Issue** بـ label `question` إن لم تجد حلاً

4. **اسأل القائد** (أحمد المتوكل) مباشرة إن كانت مشكلة تقنية

---

## 📚 مراجع للتعلم

- [Git Tutorial (عربي)](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
- [GitHub Docs](https://docs.github.com/en)
- [LaTeX Tutorial](https://www.latex-tutorial.com/)
- [Overleaf Documentation](https://www.overleaf.com/learn)

---

## ✅ الخطوات الأولى لك (افعلها اليوم)

1. [ ] ثبّت Git على جهازك
2. [ ] أنشئ حساب GitHub (إن لم يكن لديك)
3. [ ] اقبل دعوة المستودع
4. [ ] أنشئ Personal Access Token
5. [ ] استنسخ المستودع محلياً
6. [ ] اقرأ [PROJECT_RULES.md](../PROJECT_RULES.md)
7. [ ] اقرأ Issue خاصتك (#1 إلى #5)
8. [ ] ثبّت LaTeX أو استخدم Overleaf
9. [ ] أنشئ فرعاً لمهمتك
10. [ ] ابدأ القراءة والكتابة!

---

**مرحباً بك في الفريق! 🎉** نحن متحمسون للعمل معك. لا تتردد في طلب المساعدة متى احتجت. 🚀
