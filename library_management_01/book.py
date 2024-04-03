class Book:
    """
    title
    author
    available
    """
    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating
        self.count = 0
        self.available = True


    def info(self):
        return f"{self.title}, {self.author}, {self.rating}, {self.count}"

