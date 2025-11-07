# Library Management System - OOP Style

class Book():
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = copies
        self.total_copies = copies
