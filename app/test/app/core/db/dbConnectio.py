import sys

sys.path.append("/Users/cucuridas/Desktop/project_delivery_etl")

from sqlmodel import create_engine
from app.core.config import Settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{Settings.DB_USER}:{Settings.DB_PASS}@{Settings.DB_HOST}:{Settings.DB_PORT}/{Settings.DB_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
