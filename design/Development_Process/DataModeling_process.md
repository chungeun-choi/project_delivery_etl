# 데이터베이스 관련 개발 로직

## 1. Data modeling 진행 후 Aliembic을 통해 마이그레이션 진행

---

<aside>
💡 alembic 최초 실행시에는 ‘alembic init’ 명령어를 통해 필요 파일들을 자동으로 생성해주게됩니다 사용자는 ‘alembic.ini’ 파일에서 connection 정보를 변경하거나 env.py 파일의 특정 함수를 추가해줌으로써 연결에 대한 정보를 변경 할 수 있도록 설정해야합니다

</aside> </br>

### alembic revision

아래의 명령어를 실행하여 마이그레이션을 하기위한 Python 파일을 생성

```bash
alembic revision -m {메모}
```

### revision 파일 정의

`upgrade()`는 마이그래이션 버전을 적용할 때 실행되고 `downgrade()`
는 적용한 마이그래이션을 취소할 때 실행됩니다

![https://user-images.githubusercontent.com/65060314/232264396-661eb262-fd2c-4835-b699-3bcb5118a21d.png](https://user-images.githubusercontent.com/65060314/232264396-661eb262-fd2c-4835-b699-3bcb5118a21d.png)

### Upgrade head

아래의 명령어를 통해 변경한 마이그레이션 내용을 반영합니다

```bash
alembic upgrade head
```
<br>
<aside>
💡 alembic을 통한 마이그레이션 시 의존성 처리
alembic은 선행 되어진 마이그레이션 정보와 현재의 마이그레이션에 대한 내용의 의존성을 처리하기 위해 특정 변수들을 활용해 비교를 하게됩니다 또한 이 변수는 마이그레이션하게되는 타겟 database의 table 형태로 저장되어져 내용이 보존되어지게됩니다  <br>
변수 종류: ‘`revision`’, ‘`down_revision`’, ‘`branch_labels`’,’`depends_on`’

</aside> <br>

## 2. FastAPI 비동기 작업으로 인해 ‘DB connection’ 객체도 비동기 프로세스를 통해 생성

---

<aside>
💡 API를 통하 DB request 요청은 ‘session’ 변수를 통해 생성되어진 connection 객체를 사용하여 트랜잭션을 처리할 수 있도록 합니다
’Data model’로 사용할 객체는 ‘Base’ 변수에 정의되어진 ‘declarative_base’ 함수를 통해 생성합니다

</aside>

### ‘AsyncEngine’ 객체를 통한 engine 객체 생성 및 초기화

```python
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{Settings.DB_USER}:{Settings.DB_PASS}@{Settings.DB_HOST}:{Settings.DB_PORT}/{Settings.DB_NAME}"

engine: AsyncEngine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True, pool_pre_ping=True)
```

### ‘sessionmaker’ 클래스를 통해 engine 객체를 전달 받아 session facotry 객체 초기화

```python
session_maker = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
```

### ‘async_scoped_session’ 객체를 통해 request 별 connection을 생성 할 수 있도록 변수 초기화

```python
session: Union[AsyncSession, async_scoped_session] = async_scoped_session(
    session_factory=session_maker,
    scopefunc=current_task,
)
```

- Base 변수
    
    ```python
    Base = declarative_base()
    ```
    

## 3. Entity 정의 작업 진행

---

Entity 정의는 SQLModel을 상속받아 생성하며 sqlAlchemy와 함께 연동하여 사용할 수 있도록 구성

SQLModel 튜토리얼 가이드 : [https://sqlmodel.tiangolo.com/tutorial/](https://sqlmodel.tiangolo.com/tutorial/)

### baseModel

해당 클래스는 모든 entity 모델에 공통적으로 들어가게되는 설정과 필드를 추상화 해둔 클래스로서 josn에대한 인코딩*디코딩에 대한 설정, 데이터를 생성한 시점과 변경된 시점에 대한 내용이 적용되어지게 됩니다

- 클래스
    
    ```python
    class ModelBase(SQLModel):
        class Config:
            json_loads = orjson.loads
            json_dumps = orjson_dumps
            json_encoders = {datetime: datetime_convert}  
    
           
        id: Optional[int] = Field(
            default=None, sa_column=Column(BigInteger, primary_key=True, autoincrement=True)
        )
    
        created_at: Optional[datetime] = Field(
            default=None,
            sa_column=Column(
                type_=TIMESTAMP(timezone=True),
                default=func.now(),
                server_default=func.now(),
                nullable=False,
            ),
        )
    
        updated_at: Optional[datetime] = Field(
            default=None,
            sa_column=Column(
                type_=TIMESTAMP(timezone=True),
                default=func.now(),
                server_default=func.now(),
                onupdate=func.now(),
                nullable=False,
            ),
        )
    ```
    
- helper 함수
    
    ```python
    def orjson_dumps(v, *, default):
        
        return orjson.dumps(v, default=default).decode()
    
    def datetime_convert(dt: datetime) -> str:
        if not dt.tzinfo:
            dt = dt.replace(tzinfo=ZoneInfo("UTC"))
    
        return datetime.astimezone(dt).strftime("%Y-%m-%d %H:%M:%S %z")
    ```
    
    <aside>
    💡 **orjson 사용이유**
    orjson은 json 데이터를 인코딩하거나 디코딩하기위한 패키지이다, C 확장 모듈로 만들어져있어 python 기본모듈인 json은 사용하는 것 보다 훨씬 빠른 속도를 보여줌에 따라 orjson을 사용하여 인코딩, 디코딩 작업을 진행한다
    
    </aside>
    

### entity 정의 방법

![https://user-images.githubusercontent.com/65060314/233533768-34e769a4-347e-42bd-bcfe-12344c74ef59.png](https://user-images.githubusercontent.com/65060314/233533768-34e769a4-347e-42bd-bcfe-12344c74ef59.png)

### testing

생성한 entity는 database와의 정상적인 연결 및 동작이되는지 확인하기위해 테스트를 진행합니다 테스트는 CRUD 항목에 대해서 진행하며 테스트 파일을 ‘./test/app/core/db’에 python 모듈을 생성하여 함수를 생성하여 구현합니다

- connection 객체를 생성하기 위한 모듈
    
    해당 모듈의 engine 변수를 참조하여 테스트하는 모듈에서 connection 객체를 생성할 수 있도록 정의합니다
    
    ```python
    from sqlmodel import create_engine
    from app.core.config import Settings
    
    SQLALCHEMY_DATABASE_URL = f"postgresql://{Settings.DB_USER}:{Settings.DB_PASS}@{Settings.DB_HOST}:{Settings.DB_PORT}/{Settings.DB_NAME}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    ```
    

[예제]

```python
from app.entities.model_connection_info import ConnectionInfo
from sqlmodel import Session, create_engine,select ,SQLModel
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
        update = select(ConnectionInfo).where(ConnectionInfo.connection_name == "test_connection")
        
        results = session.exec(update)
        result = results.one()

        result.host = "10.101.134.1"

        session.add(result)
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

    _PostConnectionInfo()

    _GetConnectionInfo()

    _UpdateConnectionInfo()
    

    _DeleteConnectionInfo()
```