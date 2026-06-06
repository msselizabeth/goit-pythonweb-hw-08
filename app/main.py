from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db_connection import session_manager
from app.api.contacts import router as contacts_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await session_manager.close()


app = FastAPI(lifespan=lifespan)

app.include_router(contacts_router, prefix="/api")


@app.get("/api/health")
async def healthcheck():
    return {"status": "ok"}