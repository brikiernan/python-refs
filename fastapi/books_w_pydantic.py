from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


class Book:

    def __init__(
        self,
        id: int,
        title: str,
        author: str,
        description: str,
        rating: int,
        published_date: int,
    ):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(
        description="An ID is not need on create and is ignored if provided",
        default=None,
    )
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, le=5)
    published_date: int = Field(ge=2000, le=2030)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "rob",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2029,
            }
        }
    }


# Sample data
BOOKS = [
    Book(1, "Computer Science Pro", "rob", "A nice book", 5, 2030),
    Book(2, "Be Fast with FastAPI", "rob", "A great book!", 5, 2030),
    Book(3, "Master Endpoints", "rob", "A awesome book!", 5, 2029),
    Book(4, "HP1", "Author 1", "Book Description", 2, 2028),
    Book(5, "HP2", "Author 2", "Book Description", 3, 2027),
    Book(6, "HP3", "Author 3", "Book Description", 1, 2026),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def get_books():
    return BOOKS


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    return new_book


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_request: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_request.id:
            BOOKS[i] = Book(**book_request.model_dump())
            return None
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {book_request.id} not found",
    )


@app.delete("/books/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == id:
            BOOKS.pop(i)
            return None
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {id} not found",
    )


@app.get("/books/{id}", status_code=status.HTTP_200_OK)
async def get_book(id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {id} not found",
    )


@app.get("/books/", status_code=status.HTTP_200_OK)
async def get_books_by_rating(rating: int = Query(ge=1, le=5)):
    books = [book for book in BOOKS if book.rating == rating]
    return books


@app.get("/books/published/{year}", status_code=status.HTTP_200_OK)
async def get_books_by_publish_date(year: int = Path(ge=2000, le=2030)):
    books = [book for book in BOOKS if book.published_date == year]
    return books
