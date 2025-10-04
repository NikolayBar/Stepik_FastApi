from fastapi import FastAPI

from app.config import load_config
from app.logger import logger


app = FastAPI()
config = load_config()

if config.debug:
    app.debug = True
else:
    app.debug = False


@app.get("/")
def root():
    return {"message": "Hello World!"}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}


@app.get("/db")
def get_db_info():
    logger.info(f"Connecting to database: {config.db.database_url}")
    return {"database_url": config.db.database_url}
