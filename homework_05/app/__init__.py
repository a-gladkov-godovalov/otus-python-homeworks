"""
Пакет запуска flask-приложения
"""

from flask import Flask, render_template


def create_app():
    """
    Функция создания приложения
    """
    app = Flask(__name__)

    @app.route('/', endpoint='index')
    def index():
        return render_template('index.html')

    @app.route('/about/', endpoint='about')
    def about():
        return render_template('about.html')

    return app


__version__ = '1.1.1'
