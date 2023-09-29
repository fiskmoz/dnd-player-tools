""" character sheet endpoints """

from fastapi import APIRouter, Depends, HTTPException
from database import crud
from database.db import get_session_async
from sqlalchemy.ext.asyncio import AsyncSession
from mappers import character_sheet_mapper

from schemas.schemas import CharacterSheetRequest, CharacterSheetResponse


router = APIRouter(
    prefix="/character_sheets",
    tags=["character_sheets"],
)


@router.get(
    "/{character_sheet_id}",
)
async def get_character_sheet(
    character_sheet_id: int, session: AsyncSession = Depends(get_session_async)
) -> CharacterSheetResponse:
    """gets a character sheet by id"""
    sheet = await crud.get_character_sheet_by_id_async(session, character_sheet_id)
    if sheet is None:
        raise HTTPException(status_code=404, detail="Sheet not found")
    return character_sheet_mapper.character_sheet_response_map(sheet)


@router.post(
    "/",
)
async def create_character_sheet(
    request: CharacterSheetRequest,
    session: AsyncSession = Depends(get_session_async)
) -> CharacterSheetResponse:
    """gets a character sheet by id"""
    sheet = await crud.create_character_sheet_async(session, request.name)
    return character_sheet_mapper.character_sheet_response_map(sheet)
