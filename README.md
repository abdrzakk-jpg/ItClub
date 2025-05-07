<<<<<<< HEAD
# itclub
=======
# نبراس - منصة تعليمية ذكية 🎓

نبراس هي منصة تعليمية متكاملة تجمع بين التعلم التقليدي والذكاء الاصطناعي. تهدف المنصة إلى توفير بيئة تعليمية تفاعلية للطلاب والمعلمين.

## المميزات الرئيسية 🌟

- نظام محادثة ذكي مدعوم بـ Google Gemini AI 🤖
- نظام دردشة مباشر للتواصل بين الطلاب والمعلمين 💬
- لوحة تحكم للمشرفين لإدارة المنصة 👨‍💼
- واجهة مستخدم عصرية وسهلة الاستخدام 🎨
- نظام تسجيل دخول وإدارة حسابات آمن 🔐

## المتطلبات التقنية 🛠️

- Python 3.11 أو أحدث
- Flask Framework
- SQLite Database   
- Modern Web Browser

## التثبيت والإعداد ⚙️

1. قم بتثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

2. قم بإعداد ملف البيئة `.env`:
```env
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///database.db
GEMINI_API_KEY=your_gemini_api_key
```

3. قم بتشغيل المشروع:
```bash
./run.sh
```

## هيكل المشروع 📁

```
ProductionVersion/
├── pkg/
│   ├── routes/          # مسارات التطبيق
│   ├── static/         # الملفات الثابتة (CSS, JS, Images)
│   ├── templates/      # قوالب HTML
│   └── utils/          # أدوات مساعدة
├── main.py            # نقطة بداية التطبيق
├── requirements.txt   # المتطلبات
└── run.sh            # سكريبت التشغيل
```

## المساهمة 🤝

نرحب بمساهماتكم! إذا وجدت خللاً أو لديك اقتراح لتحسين المنصة، يرجى:
1. عمل Fork للمشروع
2. إنشاء فرع جديد (`git checkout -b feature/amazing_feature`)
3. تقديم التعديلات (`git commit -m 'Add amazing feature'`)
4. رفع التغييرات (`git push origin feature/amazing_feature`)
5. فتح Pull Request

## الرخصة 📝

هذا المشروع مرخص تحت رخصة MIT. راجع ملف `LICENSE` للمزيد من المعلومات.

## الاتصال والدعم 📧

- البريد الإلكتروني: abdrzakk.dz@gmail.com

## شكر خاص 🙏

شكر خاص لجميع المساهمين والداعمين لهذا المشروع.

---
صنع بـ ❤️ في الجزائر 🇩🇿# itclub
>>>>>>> 32e17c1 (first commit)
