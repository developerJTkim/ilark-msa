import os
from typing import Union
from fastapi import FastAPI, Depends
import sentry_sdk
from routers import items, users, hello
from routers.dependencies import get_query_token


sentry_sdk.init(
    dsn=os.environ['SENTRY_SDK_DSN'],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)


# Set Routers
# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()

app.include_router(hello.router)
app.include_router(users.router)
app.include_router(items.router)
