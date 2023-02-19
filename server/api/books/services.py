from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from api import db
from . import models


async def insert_data_to_db(data, db: Session = Depends(db.get_db)):
    # Check if book exists
    is_exists = (
        db.query(models.Book)
        .filter(
            models.Book.author == data.author,
            models.Book.book_name == data.book_name,
            models.Book.link == data.link,
        )
        .first()
    )
    if is_exists:
        return "Book already exists"
    else:
        # Insert into db
        print("inserting to db")
        book = models.Book(
            author=data.author,
            book_name=data.book_name,
            link=data.link,
        )
        print(f"book is {book}")
        db.add(book)
        db.commit()
        inserted_book = (
            db.query(models.Book)
            .filter(
                models.Book.author == book.author,
                models.Book.book_name == book.book_name,
                models.Book.link == book.link,
            )
            .first()
        )
        return inserted_book


async def fetch_data_from_table(db: Session = Depends(db.get_db)):
    books = db.query(models.Book).order_by(func.rand()).first()
    return books


async def fetch_data_by_id_from_table(id, db: Session = Depends(db.get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    return book


async def update_book_by_id(id, data, db: Session = Depends(db.get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    book.author = data.author
    book.book_name = data.book_name
    book.link = data.link
    db.commit()


async def delete_book_by_id(id, db: Session = Depends(db.get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    db.delete(book)
    db.commit()
