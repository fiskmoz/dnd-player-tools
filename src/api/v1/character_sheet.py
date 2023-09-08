""" character sheet endpoints """

from fastapi import APIRouter, Depends, HTTPException
from database import crud
from database.db import get_session_async
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.schemas import CharacterSheetResponse


router = APIRouter(
    prefix="/character_sheets",
    tags=["character_sheets"],
)


@router.get(
    "/{character_sheet_id}",
)
async def get_character_sheet(
    sheet_id: int, session: AsyncSession = Depends(get_session_async)
) -> CharacterSheetResponse:
    """gets a character sheet by id"""
    sheet = await crud.get_character_sheet_by_id_async(session, sheet_id)
    if sheet is None:
        raise HTTPException(status_code=404, detail="Sheet not found")
    return CharacterSheetResponse(name=sheet.Name).model_dump_json()


@router.post(
    "/",
)
async def create_character_sheet(
    name: str,
    session: AsyncSession = Depends(get_session_async)
) -> CharacterSheetResponse:
    """gets a character sheet by id"""
    sheet = await crud.create_character_sheet_async(session, name)
    return CharacterSheetResponse(id=str(sheet.CharacterSheetId), name=sheet.Name)

