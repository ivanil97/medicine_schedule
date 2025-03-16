import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    secret_key: str = os.environ.get(
        'SECRET_KEY',
        'phjsdviojrio[09r2903mcx123d;x-94mcll;v')
    access_token_expires_in_minutes: int = os.environ.get(
        'ACCESS_TOKEN_EXPIRES_IN_MINUTES', 60)

    db_user: str = os.environ.get('DB_USER', 'admin')
    db_password: str = os.environ.get('DB_PASS', '12345678')
    db_name: str = os.environ.get('DB_NAME', 'med_schedule_api')
    db_host: str = os.environ.get('DB_HOST', 'localhost')
    db_port: str = os.environ.get('DB_PORT', 5432)


settings = Settings()
