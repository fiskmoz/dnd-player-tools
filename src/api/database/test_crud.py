import pytest

from sqlalchemy.ext.asyncio import AsyncSession

from database.crud import get_character_sheet_by_id_async
from .models import CharacterSheet


@pytest.mark.asyncio
async def test_returns_character_sheet_when_exists(test_db, mocker):
    # Create a mock AsyncSession
    db_mock = mocker.Mock(spec=AsyncSession)

    # Create a mock CharacterSheet
    character_sheet_mock = mocker.Mock(spec=CharacterSheet)

    # Configure the mock db to return the character sheet mock
    db_mock.query.return_value.where.return_value.first.return_value = character_sheet_mock

    # Call the function under test
    result = await get_character_sheet_by_id_async(db_mock, 1)

    # Assert that the result is equal to the character sheet mock
    assert result == character_sheet_mock

    # Assert that the db query method was called with the correct arguments
    db_mock.query.assert_called_once_with(CharacterSheet)
    db_mock.query.return_value.where.assert_called_once_with(CharacterSheet.CharacterSheetId == 1)
    db_mock.query.return_value.where.return_value.first.assert_called_once()