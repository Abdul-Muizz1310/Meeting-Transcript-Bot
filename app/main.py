from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv
load_dotenv(dotenv_path=find_dotenv())
from app.routes import router
from app.prompts.langfuse_prompts import register_prompts

app = FastAPI()
register_prompts()
app.include_router(router)