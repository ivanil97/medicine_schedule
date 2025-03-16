from fastapi import FastAPI

from routes.get_schedule import router


app = FastAPI()
app.include_router(router)
