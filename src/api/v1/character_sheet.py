""" character sheet endpoints """

from fastapi import APIRouter, Depends
from dependencies.dependencies import get_db
from database import crud
from sqlalchemy.orm import Session

from schemas.schemas import CharacterSheetResponse


router = APIRouter(
    prefix="/character_sheets",
    tags=["character_sheets"],
)


@router.get(
    "/{character_sheet_id}",
)
async def get_character_sheet(
    id: int, db: Session = Depends(get_db)
) -> CharacterSheetResponse:
    """gets a character sheet by id"""
    sheet = crud.get_character_sheet_by_id(db, id)
    return CharacterSheetResponse(name=sheet.Name)


@router.post(
    "/",
)
async def create_character_sheet(
    db: Session = Depends(get_db),
) -> CharacterSheetResponse:
    """gets a character sheet by id"""
    sheet = crud.create_character_sheet(db, "")
    return CharacterSheetResponse(name=sheet.Name)
