from fastapi import FastAPI
from fastapi import status, Request, Response
from database import service
from database.models import MoneyOperation
from repositories.repository import UserRepository, MoneyOperationRepository, CategoryRepository
import logging

app = FastAPI()

logger = logging.getLogger(__name__)
user_repository = UserRepository()
operation_repository = MoneyOperationRepository()
category_repository = CategoryRepository()


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
async def add_operation(request: Request):
    data = await request.json()
    operation_repository.add(data)
    return Response(status_code=201)


@app.post('/users')
async def add_user(request: Request):
    data = await request.json()
    user_repository.add(data)
    return Response(status_code=201)


@app.get('/users')
async def users_list():
    users = user_repository.list()
    return users


@app.get('/users/{user_id}')
async def get_user(user_id: str):
    user = user_repository.get(user_id)
    return user


@app.post('/categories')
async def add_category(request: Request):
    data = await request.json()
    category_repository.add(data)
    return Response(status_code=201)



# TODO: Изменение баланса пользователя при добавлении операции
# TODO: Вывод списка операций для пользователя
# TODO: Login/Logout
# TODO: Личный кабинет для пользователя при входе
# TODO: Изменение суммы операции
# TODO:
# TODO:
