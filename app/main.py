from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "OK"}

@app.get("/health/")
async def ping():
    return {"status": "OK"}