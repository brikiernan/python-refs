from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "category": "fiction",
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "category": "fiction",
    },
    {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "category": "science",
    },
    {
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "category": "science",
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "category": "fiction",
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "category": "science",
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "category": "fantasy",
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "category": "fantasy",
    },
    {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "category": "fantasy",
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "category": "science fiction",
    },
    {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "category": "science fiction",
    },
    {
        "title": "The Martian",
        "author": "Andy Weir",
        "category": "science fiction",
    },
    {
        "title": "Ender's Game",
        "author": "Orson Scott Card",
        "category": "science fiction",
    },
    {
        "title": "The Handmaid's Tale",
        "author": "Margaret Atwood",
        "category": "dystopian",
    },
    {
        "title": "The Road",
        "author": "Cormac McCarthy",
        "category": "dystopian",
    },
]


@app.get("/books")
async def get_books() -> list[dict[str, str]]:
    return BOOKS


@app.get("/books/{title}")
async def get_book_by_title(title: str) -> dict[str, str]:
    for book in BOOKS:
        if book["title"].casefold() == title.casefold():
            return book
    return {}


@app.get("/books/category/{category}")
async def get_books_by_category(category: str) -> list[dict[str, str]]:
    filtered_books = [
        book
        for book in BOOKS
        if book["category"].casefold() == category.casefold()
    ]
    return filtered_books


@app.get("/books/")
async def get_books_by_query(category: str) -> list[dict[str, str]]:
    filtered_books = [
        book
        for book in BOOKS
        if book["category"].casefold() == category.casefold()
    ]
    return filtered_books


@app.get("/books/author/")
async def get_books_by_author(author: str) -> list[dict[str, str]]:
    filtered_books = [
        book for book in BOOKS if book["author"].casefold() == author.casefold()
    ]
    return filtered_books


@app.get("/books/{author}/")
async def get_books_by_author_and_category(
    author: str, category: str
) -> list[dict[str, str]]:
    filtered_books = [
        book
        for book in BOOKS
        if book["author"].casefold() == author.casefold()
        and book["category"].casefold() == category.casefold()
    ]
    return filtered_books


@app.post("/books")
async def add_book(book: dict[str, str]) -> dict[str, str]:
    BOOKS.append(book)
    return book


@app.put("/books")
async def update_book(updated_book: dict[str, str]) -> dict[str, str]:
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == updated_book["title"].casefold():
            BOOKS[i] = updated_book
    return updated_book


@app.delete("/books/{title}")
async def delete_book(title: str) -> dict[str, str]:
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == title.casefold():
            deleted_book = BOOKS.pop(i)
            return {
                "message": f"Book '{deleted_book['title']}' deleted successfully."
            }
    return {"message": f"Book with title '{title}' not found."}
