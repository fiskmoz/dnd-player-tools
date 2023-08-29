""" Crud operations for the API """

from sqlalchemy.orm import Session
from .models import CharacterSheet


def get_character_sheet_by_id(db: Session, sheet_id: int):
    """Gets DB character sheet from db by ID"""
    return (
        db.query(CharacterSheet)
        .where(CharacterSheet.CharacterSheetId == sheet_id)
        .first()
    )


def create_character_sheet(db: Session, name: str):
    """Gets DB character sheet from db by ID"""
    sheet = CharacterSheet(Name=name)
    db.add(sheet)
    db.commit()
    db.refresh(sheet)
    return sheet
