from fastapi import FastAPI
from fastapi import status, Request, Response
from database import service
from database.models import MoneyOperation
from repositories.repository import UserRepository
from repositories.fake_repositories import FakeUserRepository
import logging

app = FastAPI()

logger = logging.getLogger(__name__)
repository = FakeUserRepository([])


@app.get('/')
async def root():
    return {'Hello!': 'Everything works!'}


@app.get('/home')
async def home():
    user = service.get_user()
    return user


@app.get('/operations')
async def operations():
    user = service.get_user()
    return {'operations': user['operations']}


@app.post('/operations')
async def add_operation(value):
    user = service.get_user()
    user['operations'] += value
    return user


@app.post('/users')
async def add_user(request: Request):
    data = await request.form()
    repository.add(data)
    return Response(status_code=201)


@app.get('/users')
async def users_list():
    return repository.list()

