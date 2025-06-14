from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from models import Todo
from database import SessionLocal
from .auth import get_current_user


router = APIRouter(prefix="/v1/todos", tags=["Todos"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


user_dep = Annotated[dict, Depends(get_current_user)]  # type: ignore
db_dep = Annotated[Session, Depends(get_db)]


class TodoParams(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool


@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(user: user_dep, db: db_dep):  # type: ignore
    todos = db.query(Todo).filter(Todo.owner_id == user.get("id")).all()  # type: ignore
    return todos


class CreateTodo(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dep, db: db_dep, todo: CreateTodo):  # type: ignore
    new_todo = Todo(**todo.model_dump(), owner_id=user["id"])
    db.add(new_todo)
    db.commit()
    return (
        db.query(Todo)
        .filter(Todo.id == new_todo.id)
        .filter(Todo.owner_id == user["id"])  # type: ignore
        .first()
    )


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def read_one(id: int, user: user_dep, db: db_dep):  # type: ignore
    todo = (
        db.query(Todo)
        .filter(Todo.id == id)
        .filter(Todo.owner_id == user["id"])  # type: ignore
        .first()
    )
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {id} not found",
        )
    return todo
