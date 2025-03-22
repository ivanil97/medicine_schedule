from datetime import datetime
from typing import Optional, List, Union

from pydantic import BaseModel


class ScheduleSchema(BaseModel):
    """
    Pydantic-модель, описывающая ответ на получение данных о расписании
    """

    id: int
    med_name: str
    frequency: int
    duration: Optional[int]
    user_id: int
    created_at: datetime


class DayScheduleResponse(BaseModel):
    """
    Pydantic-модель, описывающая ответ на получение данных о расписании и графике приема на день
    """

    schedule: ScheduleSchema
    day_intakes: Union[List[str], str]