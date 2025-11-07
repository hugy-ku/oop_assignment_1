# Library Management System - OOP Style

class Book():
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = copies
        self.total_copies = copies

class Library():
    def __init__(self):
        self.books = []
    
    def add_book(self, book_id, title, author, copies):
        book = Book(book_id, title, author, copies)
        self.books.append(book)
        return f"Book '{title}' added successfully!"
    
    def display_available_books(self):
        books = self.books
        result = []
        result.append("\n=== Available Books ===")
        for book in books:
            if book.available_copies > 0:
                result.append(f"{book.title} by {book.author} - {book.available_copies} copies available")
        return '\n'.join(result)