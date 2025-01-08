from fastapi import FastAPI

from src.routes.user_routes import router as router_users
from src.routes.todo_routes import router as router_todo
from src.routes.category_routes import router as router_category
from src.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_users)
app.include_router(router_todo)
app.include_router(router_category)
