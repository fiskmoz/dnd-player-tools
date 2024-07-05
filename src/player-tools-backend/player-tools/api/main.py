""" Start of application """

from fastapi import FastAPI
import uvicorn


from api.routes.v1 import character_sheet
from api.database.db import async_engine
from api.database.models import Base


app = FastAPI()

app.include_router(character_sheet.router)
##

@app.on_event("startup")
async def startup():
    # create db tables
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/healthcheck")
async def health():
    """Check if application can respond."""
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
