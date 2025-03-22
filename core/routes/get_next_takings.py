from fastapi import Depends, Query, APIRouter
from sqlalchemy.orm import Session

from core.schemas import NextTakingsResponse
from core.services import ScheduleService
from core.utils import get_db_session, get_next_intakes, time_to_str

router = APIRouter()


@router.get('/next_takings', response_model=NextTakingsResponse)
async def get_next_takings(user_id: int = Query(...),
                           db: Session = Depends(get_db_session)):
    """
    Эндпоинт для получения данных о лекарствах, которые необходимо принять в ближайшее время (задано в настройках)
    """

    schedule_service = ScheduleService(db)
    user_schedules = schedule_service.get_user_schedules(user_id)

    next_takings = [
        {
            'schedule_id': i_schedule.id,
            'med_name': i_schedule.med_name,
            'day_intakes': time_to_str(get_next_intakes(i_schedule))
        }
        for i_schedule in user_schedules
    ]

    next_takings = [i_taking for i_taking in next_takings if i_taking['day_intakes']]

    return {'next_takings': next_takings}
