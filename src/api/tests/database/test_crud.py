""" Tests for db """
# from sqlalchemy.ext.asyncio import AsyncSession
# from database.models import CharacterSheet

## I HAVE NO IDEA HOW TO IMPLEMENT THIS, MOCK IT PERHAPS?
# async def test_get_character_sheet_by_id_async(async_session: AsyncSession):
#     """Gets DB character sheet from db by ID"""
#     print(async_session)
#     character_sheet = (await async_session.query(CharacterSheet)
#         .where(CharacterSheet.CharacterSheetId == 1)
#         .first())
#     assert character_sheet is not None