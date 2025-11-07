# Library Management System - OOP Style

class Book():
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = copies
        self.total_copies = copies

class Member():
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed = []

class Transaction():
    def __init__(self, member: Member, book: Book):
        self.member_id = member.member_id
        self.book_id = book.book_id
        self.member_name = member.name
        self.book_title = book.title

class Library():
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book_id, title, author, copies):
        book = Book(book_id, title, author, copies)
        self.books.append(book)
        return f"Book '{title}' added successfully!"
    
    def add_member(self, member_id, name, email):
        member = Member(member_id, name, email)
        self.members.append(member)
        return f"Member '{name}' registered successfully!"
    
    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None
    
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def display_available_books(self):
        books = self.books
        result = []
        result.append("\n=== Available Books ===")
        for book in books:
            if book.available_copies > 0:
                result.append(f"{book.title} by {book.author} - {book.available_copies} copies available")
        return '\n'.join(result)