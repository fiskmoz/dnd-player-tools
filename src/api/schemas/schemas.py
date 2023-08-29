""" character sheet response model """

from pydantic import BaseModel, Field


class CharacterSheetResponse(BaseModel):
    """Response model for a character sheet"""

    id: str
    name: str

    class Config:
        orm_mode = True


class CharacterSheetRequest(BaseModel):
    """Request model for creating a character sheet"""

    parameters: CharacterSheetResponse = Field(...)
