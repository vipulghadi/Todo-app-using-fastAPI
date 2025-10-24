from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/health")

async def health():
    return {"status": "ok"}


