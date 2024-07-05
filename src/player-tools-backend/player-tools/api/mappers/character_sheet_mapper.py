""" Mappers related to character sheets """

from api.database.models import CharacterSheet
from api.models.character_sheet import CharacterSheetResponse


def character_sheet_response_map(sheet: CharacterSheet) -> CharacterSheetResponse:
    """ Maps a character sheet DB model into a response model"""
    return CharacterSheetResponse(
            id=str(sheet.CharacterSheetId), 
            name=sheet.Name)
