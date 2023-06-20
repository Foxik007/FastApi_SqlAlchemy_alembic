from pydantic import BaseModel


class Book_schema(BaseModel):
    id: int
    name_book: str
    autor: str
    price: float
    page: int
    pdf: str