from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["index"])
async def index():
    return [{"username": "Foo"}, {"username": "Bar"}]


@router.get("/isMeetingRunning", tags=["metrics"])
async def is_meeting_running():
    return {"username": "fakecurrentuser"}


@router.get("/getMeetingInfo", tags=["metrics"])
async def get_meeting_info():
    return {"username": "fakecurrentuser"}


@router.get("/getMeetings", tags=["metrics"])
async def get_meetings():
    return {"username": "fakecurrentuser"}


@router.get("/create", tags=["meetings"])
async def create_get(username: str):
    return {"username": username}


@router.post("/create", tags=["meetings"])
async def create_post(username: str):
    return {"username": username}


@router.get("/end", tags=["meetings"])
async def end(username: str):
    return {"username": username}


@router.get("/join", tags=["meetings"])
async def join(username: str):
    return {"username": username}
