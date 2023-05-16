from fastapi import FastAPI
from routes import routes as api

app = FastAPI()
app.include_router(api.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)