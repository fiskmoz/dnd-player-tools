""" character sheet response model """

from pydantic import BaseModel

class CharacterSheetResponse(BaseModel):
    """Response model for a character sheet"""
    id: str
    name: str

class CharacterSheetRequest(BaseModel):
    """Request model for creating a character sheet"""

    name: str
