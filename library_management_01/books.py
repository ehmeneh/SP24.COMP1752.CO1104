from book import Book

# book objects
book1 = Book(title="The Lean Startup", author="Eric Ries", rating=5)
book2 = Book("Thinking, Fast and Slow", "Daniel Kahneman", 4) # position-based mapping
book3 = Book("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 3.5)
book4 = Book("The Alchemist", "Paulo Coelho", 3.7)
book5 = Book("To Kill a Mockingbird", "Harper Lee", 4.3)


database = {}
# key-value
database["B1234"] = book1
database["B6789"] = book2
database["B2468"] = book3
database["B1357"] = book4
database["B9876"] = book5


def display_all_books():
    for key in database:
        book_item = database[key]
        print(f"{key}, title: {book_item.title}, author: {book_item.author}, rating: {book_item.rating}")


def get_info_by_code(book_code):
    book_object = database[book_code]
    return book_object.info()


def get_book_name(book_code):
    pass


def get_book_author(book_code):
    pass


def get_book_rating(book_code):
    pass


def get_book_count(book_code):
    pass


def set_count(book_name):
    pass

def get_count(book_name):
    pass