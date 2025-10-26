from fastapi import FastAPI
from config.database import create_db_tables
from .core.exception_handlers import register_exception_handlers
from .auth import  AuthRouter


app = FastAPI()
register_exception_handlers(app)

app.include_router(
    AuthRouter,
    prefix="/auth",
)


@app.on_event("startup")
async def startup():
    print("startup")
    create_db_tables()

@app.get("/health")
async def health():
    return {"status": "ok"}


