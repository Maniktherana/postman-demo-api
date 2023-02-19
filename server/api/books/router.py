from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api import db
from . import services
from . import schema

router = APIRouter(tags=["book"], prefix="/book")


@router.get("/")
async def get_random_book(db: Session = Depends(db.get_db)):
    data = await services.fetch_data_from_table(db)
    return data if data else {"message": "No data found"}


@router.get("/{id}")
async def get_book_by_id(id: int, db: Session = Depends(db.get_db)):
    data = await services.fetch_data_by_id_from_table(id, db)
    return data if data else {"message": "No data found"}


@router.post("/")
async def create_book(book: schema.Book, db: Session = Depends(db.get_db)):
    print(f"data is {book} and db is {db}")
    inserted_book = await services.insert_data_to_db(book, db)
    return inserted_book


@router.put("/{id}")
async def update_book_by_id(
    id: int, book: schema.Book, db: Session = Depends(db.get_db)
):
    print(f"data is {book} and db is {db}")
    await services.update_book_by_id(id, book, db)
    return book


@router.delete("/{id}")
async def delete_book_by_id(id: int, db: Session = Depends(db.get_db)):
    await services.delete_book_by_id(id, db)
    return {"message": "Book deleted successfully"}
