from fastapi import FastAPI

from banking_assistant.api.routes.health import router as health_router

app = FastAPI(
    title="AI Banking Assistant",
    version="0.1.0",
)

app.include_router(health_router)
