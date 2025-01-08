from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.models import Todo
from src.schemas.todo_schemas import TodoCreate, Todo as TodoSchema

router = APIRouter(prefix='/todo', tags=['todo'])

@router.post("/", response_model=TodoSchema)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.title == todo.title).first()
    if db_todo:
        raise HTTPException(status_code=400, detail="Todo is already created")

    db_todo = Todo(
        title = todo.title,
        description = todo.description,
        completed = todo.completed,
    )

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.get("/", response_model=TodoSchema)
def get_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.title == todo.title).first()
    if db_todo:
        raise HTTPException(status_code=400, detail="Todo is already created")
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
    )

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo