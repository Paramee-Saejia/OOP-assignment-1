# oop_solution\library_oop.py

class Book:
    def __init__(self, id, title, author, available_copies, total_copies):
        self.id = id
        self.title = title
        self.author = author
        self.available_copies = available_copies
        self.total_copies = total_copies

    def __str__(self):
        return f"{self.title} by {self.author}"


class Member:
    def __init__(self, member_id, name, email):
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} ({self.email})"
