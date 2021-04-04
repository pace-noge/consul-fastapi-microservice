import json
import uvicorn
from fastapi import FastAPI
import httpx
from time import sleep
import logging


from config import Config
from utils import register_to_consul
# from register_service import register as register_to_consul

configuration = Config()


# app = FastAPI()


fake_dbs = [
    {'name': 'Bilal', 'class': 'V', 'school_id': 1},
    {'name': 'Ganta', 'class': 'IX', 'school_id': 1},
    {'name': 'Azril', 'class': 'IV', 'school_id': 2}
]


def create_app():
    app = FastAPI(title="student-service")
    return app


app = create_app()


@app.on_event("startup")
def startup_event():
    # register_to_consul()
    register_to_consul()


@app.get("/")
async def list_students():
    return fake_dbs


@app.get("/health")
async def health_status():
    return {"status": "healthy"}



@app.get("/register-service")
async def register():
    # return register_to_consul()
    register_to_consul()


@app.get("/name/{name}")
async def get_student(name: str):
    return filter(lambda x: x.get('name') == name, fake_dbs)

@app.get("/school/{school_id}")
async def filter_student_by_school(school_id: int):
    return filter(lambda x: x.get("school_id") == school_id, fake_dbs)


