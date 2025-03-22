from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from core.schemas import ScheduleRequest, ScheduleCreateResponse
from core.services import ScheduleService
from core.utils import get_db_session

router = APIRouter()

@router.post('/schedule', status_code=201, response_model=ScheduleCreateResponse)
async def create_schedule(new_schedule_data: ScheduleRequest,
                          db: Session = Depends(get_db_session)):
    """
    Эндпоинт для создания расписания
    """

    schedule_service = ScheduleService(db)
    new_schedule = schedule_service.create_schedule(new_schedule_data.model_dump())

    return {"message": "Расписание добавлено", "schedule_id": new_schedule.id}
