"""
Модуль тестов приложения
"""
import pytest
from app import __version__
from app import create_app


@pytest.fixture
def client():
    client = create_app().test_client()
    return client


def test_version():
    assert __version__ == '1.1.1'


def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200


def test_about_page(client):
    response = client.get('/about/')
    assert response.status_code == 200
