
class Book:
    def __init__(self, id, title, author, available_copies, total_copies):
        self.id = id
        self.title = title
        self.author = author
        self.available_copies = available_copies
        self.total_copies = total_copies

    def __str__(self):
        return f"{self.title} by {self.author}"
