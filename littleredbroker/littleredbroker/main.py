from fastapi import FastAPI

from littleredbroker.routers import bigbluebutton_api, littleredbroker

app = FastAPI()


app.include_router(
    bigbluebutton_api.router,
    prefix="/bigbluebutton/api",
    tags=["BBB API"],
)

app.include_router(
    littleredbroker.router,
    tags=["LRB Utils"],
)
