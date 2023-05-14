from fastapi import FastAPI
from routes import routes as api

app = FastAPI()
app.include_router(api.router)

