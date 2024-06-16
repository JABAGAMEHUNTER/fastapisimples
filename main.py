from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="Fast API LMS",
    description="LMS para gerenciamento de estudantes e cursos",
    version="0.0.1",
    contact={
        "name": "Deadpoolio is Amazing",
        "email": "jmatheo71@gmail.com"
    },
    license_info={
        "name": "MIT"
    },
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users/{id}")
async def create_user(user: User):
    users.append(user)
    return {"Success"}


@app.get("/users/{id}")
async def get_user(
        id: int = Path(..., description="The ID of the user you want to retrieve", gt=2),
        q: str = Query(None, max_length=5)
    ):
        return {"user": users[id], "query": q }