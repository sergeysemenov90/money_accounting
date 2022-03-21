from fastapi import FastAPI, Depends
from fastapi import Request, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from business.authentication import verify_user_password, create_access_token
from business.registration import check_and_update_register_data, password_hasher
from database.models import MoneyOperation, User, Category
from repositories.repository import UserRepository, MoneyOperationRepository, CategoryRepository
import logging

app = FastAPI()

logger = logging.getLogger(__name__)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

user_repository = UserRepository()
operation_repository = MoneyOperationRepository()
category_repository = CategoryRepository()

EXPIRE_DELTA=60

@app.get('/')
async def root():
    return {'Hello!': 'Everything works!'}


@app.get('/register')
async def get_registration(request: Request):
    pass


@app.post('/register')
async def post_registration(request: Request):
    reg_data = await request.json()
    confirm_data = check_and_update_register_data(reg_data)
    user = User(**confirm_data)
    if user:
        user_repository.add(user)
        return Response(content=user, status_code=201)
    return Response(status_code=400)


@app.get('/login')
async def get_login(request: Request):
    pass


@app.post('/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_repository.get(form_data.username)
    if not user:
        return Response(content={'message': 'Incorrect username or password'}, status_code=400)
    if verify_user_password(form_data.password, user.hashed_password):
        create_access_token(email=user.email, expire_delta=EXPIRE_DELTA)
        return {'access_token': user.email, 'token_type': 'bearer'}
    return Response(content={'message': 'Incorrect username or password'}, status_code=400)


@app.post('/{user_id}/operations')
async def add_operation(request: Request, token: str = Depends(oauth2_scheme)):
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
async def users_list(token: str = Depends(oauth2_scheme)):
    users = user_repository.list()
    return users


@app.get('/users/{user_id}')
async def get_user(user_id: str, token: str = Depends(oauth2_scheme)):
    user = user_repository.get(user_id)
    return user


@app.post('/categories')
async def add_category(request: Request, token: str = Depends(oauth2_scheme)):
    data = await request.json()
    category = Category(**data)
    category_repository.add(category)
    return Response(content=category, status_code=201)


@app.get('/{user_id}/operations')
async def get_user_operations(user_id: int, token: str = Depends(oauth2_scheme)):
    user = user_repository.get(user_id)
    return {'operations': user.operations}

# TODO: Протестировать api (правильность работы всех роутов)
# TODO: Login/Logout
# TODO: Добавить к роутам защиту от получения чужих данных
# TODO: Личный кабинет для пользователя при входе
# TODO: Изменение суммы операции
# TODO:
# TODO:
