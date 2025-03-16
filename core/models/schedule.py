from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from core.database import Base


class Schedule(Base):
    """
    Модель для хранения данных о расписании
    """

    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True, autoincrement=True)
    med_name = Column(String(100), nullable=False)
    frequency = Column(Integer, nullable=False) # Количество раз в день
    duration = Column(Integer, nullable=True) # None для постоянного приема
    user_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)

    def __str__(self):
        return f'Schedule #{self.id}, medicine: {self.med_name}, user: {self.user_id}'
