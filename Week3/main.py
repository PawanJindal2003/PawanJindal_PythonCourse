from fastapi import FastAPI
from .routers import auth, user
from .database import engine
from .models import model

app = FastAPI()

model.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(user.router)
