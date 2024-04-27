from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from .router.user import user_router


def create_app():
    app = FastAPI(docs_url="/", redoc_url="/docs")

    # Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(GZipMiddleware, minimum_size=1000)

    # Helper

    # Routers
    app.include_router(user_router)


    return app
