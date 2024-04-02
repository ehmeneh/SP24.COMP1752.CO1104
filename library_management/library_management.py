class LibraryManagement:
    """
    __init__
    add_book
    search_book
    borrow_book
    remove_book
    """
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        found_book = []
        for book in self.books:
            if book.title == title:
                found_book.append(book)
        return found_book


    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available == True:
                book.available = False
                return "Book borrowed successfully"
        return "Book not available"


    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return "Book removed successfully"
        return "Book not found in the library"
