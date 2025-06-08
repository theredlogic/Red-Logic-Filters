![Red Logic Logo](https://github.com/theredlogic/Red-Logic-Filters/raw/main/pic.jpg)

# Persian Bad Words For Insult Detection | شناسایی کلمات زشت فارسی

یک کتابخانه‌ی سبک و قابل گسترش برای شناسایی فحش‌ها و کلمات توهین‌آمیز فارسی، مناسب برای استفاده در ربات‌های تلگرام، چت‌بات‌ها، سیستم‌های نظارتی، فیلتر محتوا و ابزارهای NLP.

A lightweight and extendable library for detecting Persian profanity and abusive language. Perfect for Telegram bots, moderation tools, NLP pipelines, and more.

---

ویژگی‌ها | Features

- پشتیبانی از سه سطح توهین: کم، متوسط، شدید
- قابل استفاده در پروژه‌های Python، ربات‌های تلگرام و وب‌اپلیکیشن‌ها
- بدون وابستگی خارجی
- قابل گسترش با لیست‌های دلخواه

---

## ساختار متغیر های رد لاجیک برای فیلتر کلمات | Word Levels

```python
LOW_WORDS_FILTER      # توهین‌های ملایم یا روزمره
HIGH_WORDS_FILTER     # توهین‌های متوسط
EXTREME_WORDS_FILTER  # فحش‌های سنگین
ADVANCED_WORDS_FILTER # ترکیب تمام لیست‌ها
```


برای استفاده از لیست متغیر ها به صورت کامل به این شکل فراخوانی کنید
-
from redlogic import ADVANCED_WORDS_FILTER
-


# برای شناسایی فحش و کلمات نادرست فارسی
