from fastapi import FastAPI
from db import engin
import models

app = FastAPI()

models.Base.metadata.create_all(bind=engin)
