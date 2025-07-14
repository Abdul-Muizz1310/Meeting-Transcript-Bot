from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv
load_dotenv(dotenv_path=find_dotenv())
from app.routes import router

app = FastAPI()
app.include_router(router)