import os
from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
import sentry_sdk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

sentry_sdk.init(
    dsn=os.environ['SENTRY_SDK_DSN'],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)


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


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0