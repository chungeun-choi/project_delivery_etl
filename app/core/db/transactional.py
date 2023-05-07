from functools import wraps
from app.core.db.database import session


class Transactional:
    def __init__(self, refresh):
        self.refresh = refresh

    def __call__(self, function):
        @wraps(function)
        async def decorator(*args, **kwargs):
            try:
                result = await function(*args, **kwargs)
                await session.commit()
                if self.refresh:
                    await session.refresh(result)
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                await session.remove()
            return result

        return decorator
