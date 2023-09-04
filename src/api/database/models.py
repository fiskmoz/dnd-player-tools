""" Character sheet DB model """

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CharacterSheet(Base):
    """Character sheet model"""

    __tablename__ = "CharacterSheet"
    CharacterSheetId: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str]
   
