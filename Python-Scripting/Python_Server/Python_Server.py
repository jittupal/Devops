from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
import os
from models import TodoModel
from database import engine, Base, Sessionlocal
from sqlalchemy.orm import Session

load_dotenv()

app = FastAPI()

TodoModel.metadata.create_all(bind=engine)


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    pass


class TodoResponse(TodoBase):
    id: int

    class Config:
        orm_mode = True


def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return todos


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if todo:
        return todo
    return {"error": "Todo Not Found"}


@app.post("/todos")
def create_todo(todo: TodoBase, db: Session = Depends(get_db)):
    new_todo = TodoModel(**todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo:
        return {"error": "Todo Not Found"}

    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully"}
