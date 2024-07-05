""" Tests for db """
import pytest
from api.database import repository

@pytest.mark.asyncio
async def test_get_character_sheet_by_id_async(testable_character_sheets, test_database):
    """Gets DB character sheet from db by ID"""
    sheet = await repository.get_character_sheet_by_id_async(test_database, 1)
    assert len(testable_character_sheets) is 2
    assert sheet is not None
