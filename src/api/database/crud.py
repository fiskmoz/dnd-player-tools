""" Crud operations for the API """

from sqlalchemy.ext.asyncio import AsyncSession
from .models import CharacterSheet


async def get_character_sheet_by_id_async(db: AsyncSession, sheet_id: int):
    """Gets DB character sheet from db by ID"""
    return (
        await db.query(CharacterSheet)
        .where(CharacterSheet.CharacterSheetId == sheet_id)
        .first()
    )


async def create_character_sheet_async(db: AsyncSession, name: str):
    """Gets DB character sheet from db by ID"""
    sheet = CharacterSheet(Name=name)
    db.add(sheet)
    await db.commit()
    await db.refresh(sheet)
    return sheet
