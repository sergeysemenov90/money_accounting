from fastapi import FastAPI
from database import service
from database.models import MoneyOperation

app = FastAPI()


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
