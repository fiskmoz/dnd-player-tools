from sqlalchemy.ext.asyncio import create_async_engine, async_session

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://user:password@postgresserver/db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = async_session(engine)
