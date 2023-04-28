import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    SERVER_WORKER: int = os.getenv("SERVER_WORKER", 1)
    SERVER_HOST: str = os.getenv("SERVER_HOST")
    SERVER_PORT: int = os.getenv("SERVER_PORT", 8000)

    # Database connection information
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = os.getenv("DB_PORT")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASS: str = os.getenv("DB_PASS")
    DB_NAME: str = os.getenv("DB_NAME")
