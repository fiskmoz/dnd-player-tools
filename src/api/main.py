""" Start of application """

from fastapi import FastAPI
import uvicorn

from v1 import character_sheet

app = FastAPI()

app.include_router(character_sheet.router)


@app.get("/healthcheck")
async def health():
    """Check if application can respond."""
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
