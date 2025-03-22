from datetime import datetime
from typing import List, Optional


def time_to_str(datetime_marks: List[datetime]) -> Optional[List[str]]:
    """
    Функция для перевода времени приема лекарств в строковой формат
    """

    if datetime_marks:
        str_list = [i_intake.strftime("%H:%M") for i_intake in datetime_marks]
        return str_list
    return None
