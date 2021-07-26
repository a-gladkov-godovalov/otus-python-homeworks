# Домашняя работа №5
# Запуск контейнера: docker run -p 8000:5000 first-app

# Устанавливаем Docker-образ операционной системы с предустановленным Python
FROM python:3.9.6-buster

# Объявляем корневую директорию
WORKDIR /first-app

# Обновляем систему управления пакетами
RUN pip install -U pip

# Копируем из локальной машины файлы для pipenv в корневую директорую Docker-образа
COPY Pipfile .
COPY Pipfile.lock .

# Устанавливаем пакет управления виртуальным окружением
RUN pip install pipenv

# Устанавливаем все пакеты от которых зависит приложение
RUN pipenv install --system

# Копируем файлы приложения
COPY web-app.py .
COPY ./app ./app

# Объявляем переменные окружения для запуска flask
ENV FLASK_APP=web-app.py
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0

# Открываем порт в Docker-образе для обращения к приложению
EXPOSE 5000

# Запускаем приложение
CMD ["flask", "run", "--host=0.0.0.0"]
