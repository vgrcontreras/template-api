from fastapi import APIRouter

from backend.schemas import Message

router = APIRouter(prefix='/endpoint', tags=['endpoint_name'])


@router.get('/', response_model=Message)
def your_crud_function():
    return {'message': 'router1'}
