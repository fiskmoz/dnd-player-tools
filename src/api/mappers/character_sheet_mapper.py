""" Mappers related to character sheets """

from database.models import CharacterSheet
from schemas.schemas import CharacterSheetResponse


def character_sheet_response_map(sheet: CharacterSheet) -> CharacterSheetResponse:
    """ Maps a character sheet DB model into a response model"""
    return CharacterSheetResponse(
            id=str(sheet.CharacterSheetId), 
            name=sheet.Name)
