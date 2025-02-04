# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Копируем весь код в контейнер
COPY . .

# Выполняем команду для старта сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
