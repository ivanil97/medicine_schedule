from pydantic import BaseModel


class ScheduleCreateResponse(BaseModel):
    """
    Pydantic-модель, описывающая ответ на создание расписания
    """

    message: str
    schedule_id: int
