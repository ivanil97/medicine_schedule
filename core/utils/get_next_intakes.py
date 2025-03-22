from datetime import timedelta, datetime, time
from typing import List, Optional

from core.models import Schedule
from core.settings import settings

from .make_takings_list import make_takings_list


def get_next_intakes(schedule: Schedule,
                     day_start: int = settings.day_start,
                     day_end: int = settings.day_end,
                     next_taking_period: Optional[int] = settings.next_taking_period) -> Optional[List[datetime]]:
    """
    Функция для получения графика приема лекарства на день или ближайшее время
    """

    if schedule.duration:
        schedule_end = schedule.created_at + timedelta(days=schedule.duration)
        if schedule_end < datetime.utcnow():
            return None

    if next_taking_period:
        period_start = datetime.utcnow()
        period_end = period_start + timedelta(hours=next_taking_period)
    else:
        period_start = datetime.combine(datetime.utcnow().date(), time(hour=day_start))
        period_end = datetime.combine(datetime.utcnow().date(), time(hour=day_end))

    next_takings = make_takings_list(period_start=period_start, period_end=period_end, frequency=schedule.frequency)

    return next_takings
