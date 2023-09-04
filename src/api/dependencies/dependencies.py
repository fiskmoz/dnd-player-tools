# Dependencies
from database.db import SessionLocal, engine
from database import models


async def get_db():
    async with engine.begin() as connection:
        await connection.run_sync(models.Base.metadata.create_all(bind=db.engine))
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
