# استخدم صورة Python رسمية
FROM python:3.11-slim

# إعداد مجلد العمل
WORKDIR /app

# نسخ الملفات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# فتح المنفذ الافتراضي
EXPOSE 8000

# تشغيل البوت
CMD ["python", "main.py"]
