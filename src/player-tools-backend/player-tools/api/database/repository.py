""" Crud operations for the API """

from sqlalchemy.ext.asyncio import AsyncSession
from api.database.models import CharacterSheet


async def get_character_sheet_by_id_async(session: AsyncSession, sheet_id: int) -> CharacterSheet:
    """Gets DB character sheet from db by ID"""
    sheet= await session.get(CharacterSheet, sheet_id)
    return sheet

async def create_character_sheet_async(session: AsyncSession, name: str) -> CharacterSheet:
    """Gets DB character sheet from db by ID"""
    sheet = CharacterSheet(Name=name)
    session.add(sheet)
    await session.commit()
    await session.refresh(sheet)
    return sheet
