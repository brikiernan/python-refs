from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos

app = FastAPI(
    title="Todo API with FastAPI 🚀",
    description="A todo app built while learning FastAPI.",
    version="1.0.0",
)

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
# app.include_router(admin.router)
# app.include_router(users.router)
