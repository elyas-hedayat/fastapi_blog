from fastapi import FastAPI

import models
import routers
from db import engin

app = FastAPI()
app.include_router(router=routers.router)
models.Base.metadata.create_all(bind=engin)
