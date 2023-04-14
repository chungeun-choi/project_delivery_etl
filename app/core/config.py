import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    SERVER_WORKER: int = os.getenv("SERVER_WORKER",1)
    SERVER_HOST: str = os.getenv("SERVER_HOST")
    SERVER_PORT: int = os.getenv("SERVER_PORT",8000)