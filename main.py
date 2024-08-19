from fastapi import FastAPI, Query, Depends
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


class Book(BaseModel):
    title: str
    author: str
    is_classic: bool
    pages: int


class BookArgs:
    def __init__(
            self,
            title: str,
            author: Optional[str] = None,
            is_classic: Optional[bool] = None,
            pages: Optional[int] = Query(default=None, ge=1)
    ):
        self.title = title
        self.author = author
        self.is_classic = is_classic
        self.pages = pages


@app.get('/books')
def get_book(search_args: BookArgs = Depends()) -> Book | dict:
    books = [
            Book(
                title="Lion King",
                author="Abraham Lincoln",
                is_classic=True,
                pages=411),
            Book(
                title="Star Wars Return Jedi",
                author="John Lucas",
                is_classic=False,
                pages=1111)
    ]
    for book in books:
        if book.title == search_args.title:
            return book
    return {"error": "book not found"}


@app.post("/books")
def add_book(book: Book) -> list[Book]:
    books_list: list = [book]
    print(books_list)
    return books_list
