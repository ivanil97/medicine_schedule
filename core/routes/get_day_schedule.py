from fastapi import Depends, Query, APIRouter
from sqlalchemy.orm import Session

from core.schemas import DayScheduleResponse
from core.services import ScheduleService
from core.utils import get_db_session, get_next_intakes, time_to_str

router = APIRouter()


@router.get('/schedule', response_model=DayScheduleResponse)
async def get_day_schedule(user_id: int = Query(...),
                           schedule_id: int = Query(...),
                           db: Session = Depends(get_db_session)):
    """
    Эндпоинт для получения данных о расписании с графиком приема на день
    """

    schedule_service = ScheduleService(db)
    day_schedule = schedule_service.get_day_schedule(user_id, schedule_id)
    day_intakes = get_next_intakes(day_schedule, next_taking_period=None)

    if not day_intakes:
        day_intakes = "Прием лекарства завершен"
    else:
        day_intakes = time_to_str(day_intakes)

    return {'schedule': day_schedule, 'day_intakes': day_intakes}
