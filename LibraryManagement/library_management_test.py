from book import Book
from library_management import LibraryManagement

def test_create_book():
    book = Book("Python Crash Course", "Eric Matthes")
    assert book.title == "Python Crash Course"
    assert book.author == "Eric Matthes"
    assert book.available == True


def test_add_book():
    book = Book("Python Crash Course", "Eric Matthes")
    library = LibraryManagement()
    library.add_book(book)

    assert len(library.books) == 1


def test_search_book():
    book1 = Book("Python Crash Course", "Eric Matthes")
    book2 = Book("Clean Code", "Robert C. Martin")

    library = LibraryManagement()
    library.add_book(book1)
    library.add_book(book2)

    result = library.search_book("Clean Code")
    assert len(result) > 0

def test_borrow_book():
    book1 = Book("Python Crash Course", "Eric Matthes")
    book2 = Book("Clean Code", "Robert C. Martin")

    library = LibraryManagement()
    library.add_book(book1)
    library.add_book(book2)

    result = library.borrow_book("Clean Code")
    assert result == "Book borrowed successfully"
    assert library.books[1].available == False

def test_remove_book():
    book1 = Book("Python Crash Course", "Eric Matthes")
    book2 = Book("Clean Code", "Robert C. Martin")

    library = LibraryManagement()
    library.add_book(book1)
    library.add_book(book2)

    result = library.remove_book("Clean Code")
    assert len(library.books) == 1
