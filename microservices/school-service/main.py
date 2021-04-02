from fastapi import FastAPI
import httpx


app = FastAPI()

@app.get("/{name}")
async def get_school_detail(name: str):
    students = {}
    async with httpx.AsyncClient() as client:
        students = await client.get(f"http://student-service/students/{name}/")
        students = students.json()
    return students

