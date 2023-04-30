import sys

sys.path.append("/Users/cucuridas/Desktop/project_delivery_etl")


from api.models.connectionInfo import ConnectionInfo
from sqlmodel import Session, create_engine, select, SQLModel
from dbConnectio import engine

SQLModel.metadata.create_all(engine)


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


def _GetConnectionInfo():
    with Session(engine) as session:
        results = select(ConnectionInfo)
        result = session.exec(results).first()
        print(result)

        return result


def _UpdateConnectionInfo():
    with Session(engine) as session:
        update = select(ConnectionInfo).where(
            ConnectionInfo.connection_name == "test_connection"
        )

        results = session.exec(update)
        result = results.one()

        result.host = "10.101.134.1"

        session.add(result)
        session.commit()


def _DeleteConnectionInfo():
    delete = select(ConnectionInfo).where(
        ConnectionInfo.connection_name == "test_conenction"
    )

    with Session(engine) as session:
        results = session.exec(delete)

        result = results.one()
        print(result)

        session.delete(result)
        session.commit()


if __name__ == "__main__":
    _PostConnectionInfo()

    _GetConnectionInfo()

    _UpdateConnectionInfo()

    _DeleteConnectionInfo()
