from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import CreateUserInput, UserResponse, UpdateUserInput
from app.auth import get_current_user
from app.core.database import get_db
from app.models import User
from app.db.users import create_user, read_users, read_user, update_user, delete_user

UsersRouter = APIRouter()

# Create User Endpoint
@UsersRouter.post("/users/", response_model=UserResponse)
def create_user_endpoint(user: CreateUserInput, db: Session = Depends(get_db)):
    return create_user(user, db)

# Read All Users Endpoint
@UsersRouter.get("/user/", response_model=List[UserResponse])
def read_users_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return read_users(skip, limit, db)

# Read User by ID Endpoint
@UsersRouter.get("/user/{user_id}", response_model=UserResponse)
def read_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return read_user(user_id, db)

# Update User Endpoint
@UsersRouter.put("/user/{user_id}", response_model=UserResponse)
def update_user_endpoint(
    user_id: int,
    user: UpdateUserInput,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return update_user(user_id, user, current_user, db)

# Delete User Endpoint
@UsersRouter.delete("/user/{user_id}", response_model=UserResponse)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return delete_user(user_id, db)
