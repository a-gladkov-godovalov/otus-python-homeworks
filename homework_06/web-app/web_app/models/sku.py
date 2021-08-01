from datetime import datetime

from sqlalchemy import DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from .database import db


class Sku(db.Model):
    """
    Таблица товара
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False, unique=True)
    category_id = db.Column(db.Integer, ForeignKey('category.id'), nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=datetime.utcnow, server_default=func.now())

    category = relationship('Category', back_populates='skus')

    def __str__(self):
        return f'{self.__class__.__name__}(id = {self.id}, ' \
               f'name = {self.name!r},' \
               f'category = {self.category.name}' \
               f'created_at = {self.created_at!r})'

    def __repr__(self):
        return str(self)
