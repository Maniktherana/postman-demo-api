from pydantic import BaseModel


class Book(BaseModel):
    author: str
    book_name: str
    link: str = None
