""" Tests for db """
import pytest
from mappers import character_sheet_mapper


@pytest.mark.asyncio
async def test_map_character_sheet_db_models(testable_character_sheets):
    """ Maps database models to response models"""
    print(testable_character_sheets)
    mapped1 = character_sheet_mapper.character_sheet_response_map(testable_character_sheets[0])
    mapped2 = character_sheet_mapper.character_sheet_response_map(testable_character_sheets[1])
    assert(mapped1 is not None)
    assert(mapped2 is not None)
    assert(mapped1.name == "Marcus")
    assert(mapped2.name == "Johan")
