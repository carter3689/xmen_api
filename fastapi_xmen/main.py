from fastapi import FastAPI

from fastapi_xmen.routers.post import router as post_router

xmen_app = FastAPI()

xmen_app.include_router(post_router)

from fastapi import FastAPI

from fastapi_xmen.routers.post import router as post_router

xmen_app = FastAPI()

xmen_app.include_router(post_router)