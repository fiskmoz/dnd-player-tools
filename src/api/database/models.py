""" Character sheet DB model """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CharacterSheet(Base):
    """Character sheet model"""

    __tablename__ = "CharacterSheet"

    CharacterSheetId = Column(Integer(), primary_key=True)
    Name = Column(String(100), nullable=False)
