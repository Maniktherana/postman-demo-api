from sqlalchemy import Column, Integer, String
from api.db import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True, nullable=False
    )
    author = Column(String(255), nullable=False)
    book_name = Column(String(255), nullable=False)
    link = Column(String(255), nullable=True)

    def __init__(self, author, book_name, link):
        self.author = author
        self.book_name = book_name
        self.link = link

    def __repr__(self):
        return f"Book('{self.author}', '{self.book_name}', '{self.link}')"
