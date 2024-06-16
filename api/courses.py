import fastapi

router = fastapi.APIRouter()


@router.get("/courses")
async def read_courses():
    return {"courses": []}


@router.post("/courses")
async def create_course_api():
    return {"courses": []}


@router.get("/courses/{id}")
async def update_courses():
    return {"courses": []}

@router.delete("/courses{id}")
async def delete_courses():
    return {"courses": []}