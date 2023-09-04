""" character sheet endpoints """

from fastapi import APIRouter, Depends
from dependencies.dependencies import get_db
from database import crud
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
    id: int, db: AsyncSession = Depends(get_db)
) -> CharacterSheetResponse:
    """gets a character sheet by id"""
    sheet = await crud.create_character_sheet_async(db, id)
    return CharacterSheetResponse(name=sheet.Name)


@router.post(
    "/",
)
async def create_character_sheet(
    db: AsyncSession = Depends(get_db),
) -> CharacterSheetResponse:
    """gets a character sheet by id"""
    sheet = await crud.create_character_sheet_async(db, "")
    return CharacterSheetResponse(name=sheet.Name)
