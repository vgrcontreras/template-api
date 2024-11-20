from fastapi import FastAPI

from backend.routers import router1

app = FastAPI()

app.include_router(router1.router)


@app.get('/')
def read_root():
    return {'message': 'Olá mundo!'}
