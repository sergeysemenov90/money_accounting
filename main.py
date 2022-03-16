from fastapi import FastAPI
from fastapi import status, Request, Response

from business.registration import register_user
from database import service
from database.models import MoneyOperation, User, Category
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


@app.get('/register')
async def get_registration(request: Request):
    pass


@app.post('/register')
async def post_registration(request: Request):
    reg_data = await request.json()
    user = register_user(reg_data)
    if user:
        user_repository.add(user)
        return Response(content=user, status_code=201)


@app.get('/login')
async def get_login(request: Request):
    pass


@app.post('/login')
async def post_login(request: Request):
    pass


@app.post('/{user_id}/operations')
async def add_operation(request: Request):
    data = await request.json()
    operation = MoneyOperation(**data)
    operation_repository.add(operation)
    return Response(content=operation, status_code=201)


@app.post('/users')
async def add_user(request: Request):
    data = await request.json()
    user = User(**data)
    user_repository.add(user)
    return Response(content=user, status_code=201)


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
    category = Category(**data)
    category_repository.add(category)
    return Response(content=category, status_code=201)


@app.get('/{user_id}/operations')
async def get_user_operations(user_id: int):
    user = user_repository.get(user_id)
    return {'operations': user.operations}


# TODO: Протестировать api (правильность работы всех роутов)
# TODO: Login/Logout
# TODO: Добавить к роутам защиту от получения чужих данных
# TODO: Личный кабинет для пользователя при входе
# TODO: Изменение суммы операции
# TODO:
# TODO:
