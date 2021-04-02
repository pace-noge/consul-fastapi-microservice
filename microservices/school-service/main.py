from fastapi import FastAPI
import httpx


from utils import register_to_consul


fake_dbs = [
    {"name": "SD 1", "id": 1},
    {"name": "SD 2", "id": 2}
]


app = FastAPI()


@app.on_event("startup")
def startup():
    register_to_consul()


@app.get("/")
async def get_school_list():
    return fake_dbs




@app.get("/detail/{school_id}")
async def get_school_detail(school_id: int):
    school = filter(lambda x: x.get("id") == school_id, fake_dbs)
    students = {}
    students = await client.get(f"http://student_service/school/{scool_id}/")
    students = students.json()

    ret = {
        "school": school,
        "students": students
    }
    return students


@app.get("/health")
def health_status():
    return {"status": "healthy"}


@app.get("/register-to-consul")
async def register_to_consul_manually():
    return register_to_consul()

