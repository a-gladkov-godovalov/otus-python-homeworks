from flask import Blueprint, request, render_template, url_for, redirect
from sqlalchemy.exc import IntegrityError
from web_app.models import Sku, Category
from web_app.models import db
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError

skus_app = Blueprint("skus_app", __name__, url_prefix="/skus")


@skus_app.route('/catalog/', endpoint='catalog')
def list_skus():
    """
    Получение списка товара
    """
    skus = Sku.query.all()
    count = len(skus)
    return render_template("skus/index.html", skus=skus, count=count)


@skus_app.route("/add_sku/", methods=["GET", "POST"], endpoint="add_sku")
def add_sku():
    """
    Добавление товара
    """
    if request.method == "GET":
        categorys = Category.query.all()

        if not categorys:
            url = url_for("skus_app.add_category")
            return redirect(url)

        return render_template("skus/add_sku.html", categorys=categorys)

    sku_name = request.form.get("sku-name")
    if not sku_name:
        raise BadRequest("Заполните обязательное поле Наименование!")

    category_id = request.form.get("category-id")
    if not category_id:
        raise BadRequest("Сначала выберите категорию товара!")

    sku = Sku(name=sku_name, category_id=category_id)
    db.session.add(sku)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise InternalServerError(f"Не удалось сохранить товар с именем {sku_name!r}!")

    url = url_for("skus_app.catalog")
    return redirect(url)


@skus_app.route("/add_category/", methods=["GET", "POST"], endpoint="add_category")
def add_category():
    """
    Добавление категории товара
    """
    if request.method == "GET":
        return render_template("skus/add_category.html")

    category_name = request.form.get("category-name")
    if not category_name:
        raise BadRequest("Заполните обязательное поле Наименование!")

    category = Category(name=category_name)
    db.session.add(category)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise InternalServerError(f"Не удалось сохранить категорию с именем {category_name!r}!")

    url = url_for("skus_app.add_sku")
    return redirect(url)
