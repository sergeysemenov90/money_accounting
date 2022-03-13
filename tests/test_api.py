import requests
import pytest
from tests.factories import UserFactory
import json


@pytest.fixture()
def new_user():
    return UserFactory(email='test@test.ru')


@pytest.fixture()
def another_user():
    return UserFactory(email='test@test2.ru')


def test_home_page():
    r = requests.get('http://localhost:8000/home')
    assert r.status_code == 200
    assert b'id' in r.content


def test_operations_page():
    r = requests.get('http://localhost:8000/operations')
    assert r.status_code == 200
    assert r.headers['content-type'] == 'application/json'


def test_add_user(new_user):
    data = new_user.__dict__
    data.pop('_sa_instance_state')
    r = requests.post('http://localhost:8000/users', data=json.dumps(data))
    assert r.status_code == 201



