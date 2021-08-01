"""
Домашнее задание №6 "Взаимодействие между контейнерами"

Задача:
- создайте docker-compose файл, настройте там связь базы данных и веб-приложения
- добавьте в свой проект модели. Это могут быть те же модели, что были использованы для сохранения данных с открытого API, это может быть и что-то новое
- добавьте возможность добавлять записи
- создайте страницу, на которой записи выводятся
- база данных должна быть в отдельном контейнере
- бонусом будет, если приложение будет запускаться не в debug режиме, а уже production-ready

Критерии оценки:
- docker-compose файл присутствует и работает
- приложение взаимодействует с БД
- в приложении есть возможность добавить записи, они сохраняются в БД
- в приложении есть страница, которая выдаёт доступные записи (вытаскивает из БД)
"""
from flask import Flask, render_template
from flask_migrate import Migrate

from web_app.models import db
from web_app.views import skus_app

app = Flask(__name__)

app.config.from_object("config.ProductionConfig")

app.register_blueprint(skus_app)

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/', endpoint='index')
def index():
    """
    Главная страница
    """
    return render_template('index.html')


@app.route('/about/', endpoint='about')
def about():
    """
    О сайте
    """
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=False)
