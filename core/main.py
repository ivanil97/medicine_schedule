from fastapi import FastAPI

from core.routes.create_schedule import router as router_1
from core.routes.get_user_schedules import router as router_2
from core.routes.get_day_schedule import router as router_3
from core.routes.get_next_takings import router as router_4

app = FastAPI()

app.include_router(router_1)
app.include_router(router_2)
app.include_router(router_3)
app.include_router(router_4)
