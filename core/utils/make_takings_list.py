from datetime import datetime, time, timedelta
from typing import List

from core.settings import settings


def make_takings_list(period_start, period_end, frequency,
                      day_start: int = settings.day_start,
                      day_end: int = settings.day_end) -> List[datetime]:
    """
    Функция для формирования списка времени приема лекарства
    """

    next_takings = []
    next_intake = datetime.combine(datetime.utcnow().date(), time(hour=day_start))

    while next_intake <= period_end:
        if next_intake >= period_start:
            next_takings.append(next_intake)

        fr = ((day_end - day_start + 1) / frequency) * 60
        next_intake += timedelta(minutes=fr)

        if next_intake.hour > day_end or next_intake.hour < day_start:
            next_intake = datetime.combine(datetime.utcnow().date() + timedelta(days=1), time(hour=day_start))

    return next_takings
