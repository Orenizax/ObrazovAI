from fastapi import APIRouter
from schemas.user import (
    UserCreate,
    UserResponse,    
)

router = APIRouter(
    prefix="/v1/users",
    tags=['Users'],
)

@router.post('/registration', response_model=UserResponse)
async def registration(user: UserCreate):
    """Регистрация пользователя"""

    return()