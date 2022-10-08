import os
from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id__": item_id, "q": q}


@app.get("/get/env")
def read_env():
    return {"app_env": os.environ['APP_ENV']}

