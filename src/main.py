from fastapi import FastAPI

from src.routes.user_routes import router as router_users
from src.routes.todo_routes import router as router_todos
from src.routes.course_routes import router as router_courses
from src.database import Base, engine

# uvicorn.run(app, host="127.0.0.1", port=8000, workers=1)
# Get-Process python* | Select-Object Id,ProcessName
# Get-Process python* | Stop-Process -Force


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_users)
app.include_router(router_todos)
app.include_router(router_courses)