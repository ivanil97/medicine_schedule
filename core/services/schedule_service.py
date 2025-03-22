from fastapi import HTTPException
from core.models import Schedule
from sqlalchemy import select


class ScheduleService:
    """
    Класс для работы с таблицей Schedule в базе данных
    """

    def __init__(self, db):
        self.db = db

    def create_schedule(self, new_schedule_data: dict):
        """
        Функция для создания расписания в базе данных
        """

        new_schedule = Schedule(
            med_name = new_schedule_data.get('med_name'),
            frequency = new_schedule_data.get('frequency'),
            duration = new_schedule_data.get('duration'),
            user_id = new_schedule_data.get('user_id'),
            created_at = new_schedule_data.get('created_at')
        )

        self.db.add(new_schedule)
        self.db.commit()
        self.db.refresh(new_schedule)

        return new_schedule

    def get_user_schedules(self, user_id: int):
        """
        Функция для получения списка расписаний для указанного пользователя
        """

        statement = select(Schedule).where(Schedule.user_id == user_id)
        user_schedules = self.db.execute(statement).scalars().all()

        if user_schedules:
            return user_schedules
        else:
            raise HTTPException(status_code=404, detail="Расписания не найдены")


    def get_day_schedule(self, user_id: int, schedule_id: int):
        """
        Функция для получения данных о выбранном расписании
        """

        statement = select(Schedule).where(Schedule.user_id == user_id).where(Schedule.id == schedule_id)
        user_schedule = self.db.execute(statement).scalars().first()

        if user_schedule:
            return user_schedule
        else:
            raise HTTPException(status_code=404, detail="Расписания не найдены")
