class Book:
    """
    title
    author
    available
    """
    def __init__(self, title, author, rating):
        self.name = title
        self.author = author
        self.rating = rating
        self.count = 0
        self.available = True


    def info(self):
        return (f"{self.title}, {self.author}, "
                f"{self.rating}, {self.count}")


    def get_title(self):
        return self.name