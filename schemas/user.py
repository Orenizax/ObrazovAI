from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=16)
    email: EmailStr

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=16)
    email: EmailStr

class UserResponse(UserBase):
    id: int = Field(..., gt=0)
    pass