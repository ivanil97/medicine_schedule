from typing import List, Optional

from pydantic import BaseModel



class NextTakingSchema(BaseModel):
    """
    Pydantic-модель, описывающая данные о лекарстве для приема в ближайшее время
    """

    schedule_id: int
    med_name: str
    day_intakes: Optional[List[str]]


class NextTakingsResponse(BaseModel):
    """
    Pydantic-модель, описывающая список лекарств для принятия в ближайшее время
    """

    next_takings: List[NextTakingSchema]
