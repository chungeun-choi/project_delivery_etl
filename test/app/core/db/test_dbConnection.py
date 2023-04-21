import sys

sys.path.append("/Users/cucuridas/Desktop/project_delivery_etl")


from app.entities.model_connection_info import ConnectionInfo
from sqlmodel import Session, create_engine,select ,SQLModel
from app.core.config import Settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{Settings.DB_USER}:{Settings.DB_PASS}@{Settings.DB_HOST}:{Settings.DB_PORT}/{Settings.DB_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SQLModel.metadata.create_all(engine)

def _GetConnectionInfo():
    with Session(engine) as session:
        result = select(ConnectionInfo)
        return session.exec(result).first()

def _PostConnectionInfo():
    connection1 = ConnectionInfo(
        connection_name="test_conenction",
        host="test@101.1.1.1",
        port=8080,
        user="testuser",
        password="test11!",
    )

    with Session(engine) as session:
        session.add(connection1)
        session.commit()

def _DeleteConnectionInfo():
    delete = select(ConnectionInfo).where(ConnectionInfo.connection_name=="test_conenction")
    
    with Session(engine) as session:
        results= session.exec(delete)

        result = results.one()
        print(result)

        session.delete(result)
        session.commit()


if __name__ == "__main__":

   # _PostConnectionInfo()

    # print(_GetConnectionInfo())

    _DeleteConnectionInfo()

