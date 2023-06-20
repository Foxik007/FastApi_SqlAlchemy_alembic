from sqlalchemy import Integer, String, Float,ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = 'book'
    id: Mapped[int] = mapped_column(Integer, unique=True, primary_key=True)
    name_book: Mapped[str] = mapped_column(String,nullable=False)
    autor: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float,nullable=False)
    page: Mapped[int] = mapped_column(Integer,nullable=False)
    pdf: Mapped[str] = mapped_column(String,nullable=True)


