FROM python:3.11-slim

WORKDIR /app

# Установка зависимостей для Selenium + Chrome
RUN apt-get update && apt-get install -y \
    chromium-browser \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Копирование requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода тестов
COPY . .

# Запуск тестов с генерацией отчёта Allure
CMD ["pytest", "--alluredir=allure-results"]
