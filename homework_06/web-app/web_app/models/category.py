from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.orm import relationship

from .database import db


class Category(db.Model):
    """
    Таблица категорий товара
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False, unique=True)
    created_at = db.Column(DateTime, nullable=False, default=datetime.utcnow, server_default=func.now())

    skus = relationship('Sku', back_populates='category')

    def __str__(self):
        return f'{self.__class__.__name__}(id = {self.id}, ' \
               f'name = {self.name!r},' \
               f'created_at = {self.created_at!r})'

    def __repr__(self):
        return str(self)
