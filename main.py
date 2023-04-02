from fastapi import FastAPI
from db import engin
import models
import routers

app = FastAPI()
app.include_router(router=routers.router)
models.Base.metadata.create_all(bind=engin)
