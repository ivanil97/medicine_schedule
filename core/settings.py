import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    secret_key: str = os.getenv(
        'SECRET_KEY',
        'phjsdviojrio[09r2903mcx123d;x-94mcll;v')
    access_token_expires_in_minutes: int = os.getenv(
        'ACCESS_TOKEN_EXPIRES_IN_MINUTES', 60)

    db_user: str = os.getenv('DB_USER', 'admin')
    db_password: str = os.getenv('DB_PASS', '12345678')
    db_name: str = os.getenv('DB_NAME', 'med_schedule_api')
    db_host: str = os.getenv('DB_HOST', 'localhost')
    db_port: str = os.getenv('DB_PORT', 5432)

    day_start: int = os.getenv('DAY_START', 8) # начало дня в часах
    day_end: int = os.getenv('DAY_END', 22) # конец дня в часах
    next_taking_period: int = os.getenv('NEXT_TAKING_PERIOD', 3)  # ближайший период в часах


settings = Settings()
