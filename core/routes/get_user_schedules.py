from fastapi import Depends, Query, APIRouter
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from core.services import ScheduleService
from core.utils import get_db_session

router = APIRouter()

@router.get('/schedules')
async def get_user_schedules(user_id: int = Query(...),
                             db: Session = Depends(get_db_session)) -> JSONResponse:
    """
    Эндпоинт для получения списка расписаний пользователя
    """

    schedule_service = ScheduleService(db)
    user_schedules = schedule_service.get_user_schedules(user_id)
    schedules_list = [i_schedule.id for i_schedule in user_schedules]

    return JSONResponse({'schedules': schedules_list})
