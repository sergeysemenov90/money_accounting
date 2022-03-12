import requests
import pytest
from tests.factories import UserFactory


@pytest.fixture()
def new_user():
    return UserFactory(id=1, email='test@test.ru')


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
    print(data)
    r = requests.post('http://localhost:8000/users', data=data)
    assert r.status_code == 201


def test_new_user_in_db(new_user):
    r = requests.get('http://localhost:8000/users')
    print(r.json())
    assert r.status_code == 200
    assert new_user.id == int(r.json()['users'][0]['id'])
