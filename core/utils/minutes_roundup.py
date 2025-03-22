from datetime import datetime, timedelta


def minutes_roundup(datetime_mark: datetime) -> datetime:
    """Функция для округления времени приема лекарства"""

    minutes = datetime_mark.time().minute
    if 0 < minutes <= 15:
        minutes = 15 - minutes
    elif 15 < minutes <= 30:
        minutes = 30 - minutes
    elif 30 < minutes <= 45:
        minutes = 45 - minutes
    elif 45 < minutes <= 60:
        minutes = 60 - minutes

    datetime_mark = datetime_mark + timedelta(minutes=minutes)
    return datetime_mark