# 👑 دليل قائد الفريق (Leader Guide)

> **هذا الدليل مخصّص للقائد التقني للمشروع.**
> اقرأه كاملاً قبل البدء بإدارة الفريق.

---

## 📌 روابط مهمة (احفظها في المفضلة)

| الرابط | الوصف |
|--------|------|
| https://github.com/orgs/GP-Project-ust/projects/4 | **Project Board** — لوحة Kanban |
| https://github.com/GP-Project-ust/Bayan-Documentation/issues | الـ Issues |
| https://github.com/GP-Project-ust/Bayan-Documentation/pulls | الـ Pull Requests |
| https://github.com/GP-Project-ust/Bayan-Documentation/milestones | الـ Milestones |
| https://github.com/GP-Project-ust/Bayan-Documentation/labels | الـ Labels |
| https://github.com/GP-Project-ust/Bayan-Documentation/actions | الـ CI/CD (PDF التلقائي) |

---

## 🎯 دورك كقائد

أنت لست مجرد "مدير" — أنت:
1. **منسّق** بين الأعضاء
2. **مراجع أول** لكل PR
3. **حلّال مشاكل** تقنية
4. **نقطة اتصال** مع المشرف
5. **محرّك** للفريق (تحفيز + متابعة)

---

## 📋 المهام الأسبوعية للقائد

### كل صباح (10 دقائق):

1. ✅ افتح [Project Board](https://github.com/orgs/GP-Project-ust/projects/4)
2. ✅ تحقق من:
   - هل أحد الـ Issues في "Blocked"؟
   - هل هناك PRs تنتظر مراجعتك؟
   - هل أحد أرسل تعليقاً على Issue؟
3. ✅ تحقق من [Actions](https://github.com/GP-Project-ust/Bayan-Documentation/actions) — هل نجحت آخر ترجمة PDF؟

### كل أسبوع (1 ساعة):

1. 📊 راجع تقدم الفريق:
   - كم Issue اكتمل؟
   - كم PR مفتوح؟
   - هل أحد متأخر؟
2. 🤝 تواصل مع أي عضو متأخر (بشكل ودي)
3. 📝 حدّث المشرف (د. نبيل) برسالة قصيرة:
   ```
   د. نبيل،
   تقدم الفريق هذا الأسبوع:
   - ✅ اكتمل: §3.1، §3.2
   - 🔄 قيد العمل: §3.3 (أحمد)
   - ⏳ بانتظار البدء: §3.4، §3.5، §3.6
   - 📄 PDF الحالي: [رابط]
   ```
4. 🗓️ خطط لأسبوع القادم:
   - ما الذي يجب إنجازه؟
   - من سيعمل على ماذا؟

### كل نهاية مرحلة (Milestone):

1. 🎉 احتفل بإنجاز الفريق (رسالة شكر في Discord)
2. 📊 اكتب تقريراً مختصراً:
   - ما الذي سلك جيداً؟
   - ما الذي لم يسلُك؟
3. 🔄 خطّط للمilestone التالي

---

## 🚀 الإعداد الأولي (مرة واحدة)

### 1. تثبيت Git محلياً

```bash
# تحقق من تثبيت Git
git --version

# إن لم يكن مثبتاً، نزّله من: https://git-scm.com/downloads
```

### 2. استنساخ المستودع

```bash
# أنشئ مجلد للمشروع
mkdir ~/bayan-thesis
cd ~/bayan-thesis

# استنساخ المستودع
git clone https://github.com/GP-Project-ust/Bayan-Documentation.git
cd Bayan-Documentation

# تحقق من الفرع الحالي
git branch
# يجب أن يظهر: * main
```

### 3. إعداد Git محلياً

```bash
# اسمك وبريدك
git config user.name "Ahmed Al-Mutawakel"
git config user.email "ahmed@example.com"

# تفعيل دعم Unicode (للعربية)
git config --global core.quotepath false
```

### 4. إعداد مصادقة GitHub

```bash
# استخدم Personal Access Token بدلاً من كلمة المرور
# عند الـ push، أدخل:
# - Username: your-github-username
# - Password: your-personal-access-token (وليس كلمة مرور GitHub)

# أو استخدم Git Credential Manager:
# https://github.com/git-ecosystem/git-credential-manager
```

---

## 🌿 إدارة الفروع (Branches)

### قواعد التسمية:

| النوع | الصيغة | مثال |
|------|--------|------|
| قسم فصل | `ch3/section-X.Y-name` | `ch3/section-3.3-ahmed` |
| إصلاح | `fix/issue-XX-description` | `fix/issue-12-table-overflow` |
| توثيق | `docs/description` | `docs/update-readme` |
| ميزة | `feat/description` | `feat/add-risk-matrix` |

### حماية فرع `main`:

كمسؤول، يمكنك حماية `main`:
1. اذهب إلى: Settings → Branches → Add rule
2. Branch name pattern: `main`
3. فعّل:
   - ✅ Require a pull request before merging
   - ✅ Require approvals (2 على الأقل)
   - ✅ Require status checks to pass (CI)

---

## 📝 إدارة الـ Issues

### كيف تُسند Issue لعضو؟

1. افتح الـ Issue
2. في الجهة اليمنى، ابحث عن **Assignees**
3. انقر **assign yourself** أو ابحث عن اسم العضو
4. اضغط **Save**

### كيف تغيّر الأولوية؟

1. افتح الـ Issue
2. في **Labels** (يمين)، أضف/أزل:
   - `priority: critical` (للأهم)
   - `priority: high` (افتراضي لمعظم المهام)
   - `priority: medium`
   - `priority: low`

### كيف تغيّر الحالة في الـ Board؟

1. اذهب إلى [Project Board](https://github.com/orgs/GP-Project-ust/projects/4)
2. اسحب وأفلت البطاقة بين الأعمدة:
   - Backlog → Todo → In Progress → Review → Done

> **ملاحظة:** الأعضاء يمكنهم تحديث status خاصتهم، لكن القائد هو من ينقل لـ "Done".

---

## 🔀 إدارة Pull Requests

### قواعد المراجعة:

| نوع PR | عدد المراجعين | القائد يراجع؟ |
|--------|--------------|---------------|
| قسم صغير (§3.1, §3.7) | 2 | ✅ نعم |
| قسم كبير (§3.3) | 3 | ✅ نعم |
| إصلاح خطأ | 1 | 🟡 اختياري |
| توثيق | 1 | ❌ لا |

### كيف تراجع PR؟

1. افتح الـ PR
2. انقر **Files changed**
3. مرّر على كل سطر:
   - الأخضر (+) = سطر مضاف
   - الأحمر (-) = سطر محذوف
4. للتعلّق على سطر: مرّر فوقه وانقر **+**
5. عند الانتهاء، اختر:
   - **Comment** (تعليقات فقط)
   - **Approve** (موافقة)
   - **Request changes** (يحتاج تعديل)

### عند دمج PR:

1. تأكد أن:
   - كل الـ checks نجحت (CI) ✅
   - عدد المراجعات المطلوبة متوفر ✅
   - لا تعارضات (conflicts) ✅
2. اختر **Squash and merge** (للحفاظ على تاريخ نظيف)
3. احذف الفرع بعد الدمج (إن لم يعد ضرورياً)

---

## 🛠️ التعامل مع مشاكل شائعة

### مشكلة: "تعارض في الدمج" (Merge Conflict)

```bash
# على الفرع الخاص بك
git fetch origin
git merge origin/main
# أو
git rebase origin/main

# حل التعارضات في محررك
# بعد الحل:
git add .
git commit
git push
```

### مشكلة: "نسيت إنشاء فرع وعملت على main"

```bash
# أنشئ فرعاً من التغييرات الحالية
git checkout -b ch3/section-3.3-ahmed
git add .
git commit -m "feat: add §3.3 (refs #3)"
git push

# أعد main لحالته الأصلية
git checkout main
git reset --hard origin/main
```

### مشكلة: "فشل CI (PDF لم يُبنَ)"

1. اذهب إلى [Actions](https://github.com/GP-Project-ust/Bayan-Documentation/actions)
2. افتح آخر workflow فشل
3. اقرأ السجل (log)
4. ابحث عن `error:`
5. افتح Issue بـ label `bug`

---

## 📊 متابعة التقدم

### تقرير أسبوعي (للمشرف):

```markdown
# تقرير الأسبوع XX-XX-2026

## ✅ الإنجازات
- اكتمل §3.1 (وليد) - [PR #15]
- اكتمل §3.2 (محمد رشيد) - [PR #16]

## 🔄 قيد العمل
- §3.3 (أحمد) - 60% مكتمل
- §3.4 (عبدالكريم) - بدأ اليوم

## ⚠️ التحديات
- تأخر §3.6 بسبب انتظار باقي الأقسام
- مشكلة في ترجمة جدول كبير (تم حلها)

## 📅 خطة الأسبوع القادم
- إنهاء §3.3 و §3.4
- بدء §3.5 و §3.6
- مراجعة شاملة للفصل الثالث
```

---

## 🎓 نصائح قيادية

### ✅ افعل:

1. **كن قدوة** — ابدأ العمل مبكراً وأظهر الالتزام
2. **تواصل بوضوح** — استخدم GitHub Issues للتواصل الرسمي
3. **احتفل بالإنجازات** — رسالة شكر لكل PR مدموج
4. **كن مرناً** — عدّل الخطط عند الحاجة
5. **استمع لفريقك** — اطرح أسئلة، لا تفترض
6. **وثّق القرارات** — في `decisions.md`

### ❌ لا تفعل:

1. **لا تسيطر** — فريقك متعلم، ثق بهم
2. **لا تتجاهل المشاكل** — عالجها فوراً
3. **لا تؤجل المراجعات** — راجع PRs خلال 24 ساعة
4. **لا تخفِ الأخبار السيئة** — شاركها مع الفريق
5. **لا تنسَ المشرف** — أبقه على اطلاع دائم

---

## 🆘 عند الأزمات

### أزمة: "لن ننتهي في الوقت"

1. اجمع الفريق لاجتماع طارئ
2. حدد الأولويات:
   - ما هو ضروري للتسليم؟
   - ما يمكن تأجيله؟
3. أبلغ المشرف فوراً
4. عدّل الـ Milestones

### أزمة: "خلاف بين عضوين"

1. استمع لكلا الطرفين بشكل منفصل
2. اعقد اجتماعاً مشتركاً
3. ركّز على المشكلة، لا الأشخاص
4. إن لم تحل، اطلب تدخّل المشرف

---

## 📞 جهات اتصال

| الجهة | متى تتواصل |
|------|-----------|
| **المشرف (د. نبيل)** | القرارات الكبرى، تأخير كبير، خلافات |
| **الفريق (Discord)** | التنسيق اليومي، أسئلة سريعة |
| **GitHub Discussions** | الأسئلة العامة، النقاشات |

---

## 📚 مراجع للقائد

- [GitHub Projects Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [CONTRIBUTING.md](../CONTRIBUTING.md)
- [PROJECT_RULES.md](../PROJECT_RULES.md)

---

**أنت القائد — لكنك لست وحدك.** فريقك ومشرفك معك. ثق بنفسك، تواصل بوضوح، وستنجحون بإذن الله. 🚀
