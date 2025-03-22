from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ScheduleRequest(BaseModel):
    """
    Pydantic-модель, валидирующая запрос на создание нового расписания
    """

    med_name: str
    frequency: int = Field(gt=0)
    duration: Optional[int] = Field(default=None, gt=0)
    user_id: int = Field(gt=0)
    created_at: Optional[datetime] = None
