from fastapi import FastAPI

from app.config import load_config
from app.logger import logger
from app.models.models import User


app = FastAPI()
config = load_config()

if config.debug:
    app.debug = True
else:
    app.debug = False

users = [User(id=1, name="John Doe"), User(id=2, name="Tom Bad")]


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/custom")
async def read_custom_message():
    return {"message": "This is a custom message!"}


@app.get("/db")
async def get_db_info():
    logger.info(f"Connecting to database: {config.db.database_url}")
    return {"database_url": config.db.database_url}


@app.get("/user")
async def user():
    return users
