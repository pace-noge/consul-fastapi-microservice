import json
import uvicorn
from fastapi import FastAPI
import httpx
from time import sleep
import logging

logger = logging.getLogger(__name__)

from config import Config

configuration = Config()


# app = FastAPI()


def create_app():
    app = FastAPI(title="student-service")
    app.logger = logger
    return app


def register_to_consul():
    url = "http://consul:8500/v1/agent/service/register"
    data = {
        "Name": "StudentService",
        "Tags": ['student'],
        'Address': configuration.address,
        'Port': configuration.port,
        "Check": {
            'http': f'http://{configuration.address}:{configuration.port}/health',
            'interval': '10s'
        }
    }
    print('Service registration parameters: ', data)
    res = {"message": "registering"}
    res = httpx.put(url, data=json.dumps(data))
    return res.text



app = create_app()

@app.on_event("startup")
def startup_event():
    register_to_consul()

@app.get("/")
async def list_students():
    return [
        {"name": "Bilal Ibnu", "class_name": "Class V"},
        {"name": "Ganta", "class_name": "Class IX"}
    ]


@app.get("/health")
async def health_status():
    return {"status": "healthy"}


@app.get("/ping-consul")
async def ping_consul():
    with httpx.AsyncClient() as client:
        r = client.get("http://consul:8500/agent/services")
    return r.json()


@app.get("/register-service")
async def register():
    return register_to_consul()

@app.get("/{name}")
async def get_student(name: str):
    return {"name": name}


