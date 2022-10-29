from fastapi import FastAPI
from routes.user import user
from pydantic import BaseSettings

app = FastAPI(
    title="My first API",
    description="esta es mi primera api con fastapi",
    version="0.0.1",
    openapi_tags=[{
        "name":"users",
        "description":"users routes"
    }]
)
app.include_router(user)