from fastapi import FastAPI
from app.slack_router import slack_router
from app.database import init_db

app = FastAPI()

app.include_router(slack_router, prefix="/slack")

@app.on_event("startup")
def startup():
    init_db()
