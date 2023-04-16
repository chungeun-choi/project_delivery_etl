# DB connection 관리 로직

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
    

## 3. Entity 정의 및 모델링 작업 진행

---