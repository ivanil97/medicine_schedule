import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    db_user: str = os.getenv('DB_USER', 'admin')
    db_password: str = os.getenv('DB_PASS', '12345678')
    db_name: str = os.getenv('DB_NAME', 'med_schedule_api')
    db_host: str = os.getenv('DB_HOST', 'db')
    db_port: int = os.getenv('DB_PORT', 5432)

    day_start: int = int(os.getenv('DAY_START', 8))  # начало дня в часах
    day_end: int = int(os.getenv('DAY_END', 22))  # конец дня в часах
    next_taking_period: int = int(os.getenv('NEXT_TAKING_PERIOD', 3))  # ближайший период в часах


settings = Settings()
