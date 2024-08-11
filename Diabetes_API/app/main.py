from typing import Any
from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
#What is CORSMiddleware: refers to the situations when a frontend running in a browser has
# JavaScript code that communicates with a backend, and the backend is in a different "origin"
# than the frontend.
# Additional Details: #https://fastapi.tiangolo.com/tutorial/cors/
from fastapi.responses import HTMLResponse
from loguru import logger
#Loguru is a Python logging library that provides a simple and elegant way to configure
#and use logging. It offers powerful features while maintaining an easy-to-use interface.
from app.api import api_router
from app.config import settings, setup_app_logging

# setup logging as early as possible: At the start of the program execution
setup_app_logging(config=settings)

#Initiating the FASTAPI
app = FastAPI(title= settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
              )

#Initiating the root router
root_router = APIRouter()

@root_router.get("/")
def index(request: Request) -> Any:
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to the API</h1>"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )

    return HTMLResponse(content=body)

app.include_router(root_router)
app.include_router(api_router, prefix = settings.API_V1_STR)

#Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use this for debugging purposes only
    logger.warning("Running in development mode. Do not run like this in production.")
    import uvicorn

    uvicorn.run(app, host="localhost", port=8001, log_level="debug")

