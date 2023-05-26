from fastapi import FastAPI
from api.routes import routes as api
from auth.routes import routes as auth

app = FastAPI()
app.include_router(auth.router)
app.include_router(api.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)