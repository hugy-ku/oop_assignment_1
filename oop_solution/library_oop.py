# Library Management System - OOP Style

class Book():
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = copies
        self.total_copies = copies
    
    def _borrow(self):
        if self.available_copies <= 0:
            return False
        self.available_copies -= 1
        return True
    
    def _return(self):
        self.available_copies += 1
        return True

class Member():
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed = []
    
    def _borrow(self, book):
        if len(self.borrowed) >= 3:
            return False
        self.borrowed.append(Transaction(book))
        return True
    
    def _return(self, book):
        for i, transaction in enumerate(self.borrowed):
            if transaction.book_id == book.book_id:
                self.pop(i)
                return True
        return False

class Transaction():
    def __init__(self, book):
        self.book_id = book.book_id

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
    
    def find_book(self, book_id) -> Book:
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None
    
    def find_member(self, member_id) -> Member:
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member:
            return "Error: Member not found!"
        if not book:
            return "Error: Book not found!"
        
        status = book._borrow()
        if not status:
            return "Error: No copies available!"
        status = member._borrow(book)
        if not status:
            return "Error: Member has reached borrowing limit!"
        return True


    def display_available_books(self):
        books = self.books
        result = []
        result.append("\n=== Available Books ===")
        for book in books:
            if book.available_copies > 0:
                result.append(f"{book.book_id} {book.title} by {book.author} - {book.available_copies} copies available")
        return '\n'.join(result)

    def display_member_books(self, member_id):
        result = []
        member = self.find_member(member_id)
        if not member:
            return "Error: Member not found!"
        
        result.append(f"\n=== Books borrowed by {member.name} ===")
        if len(member.borrowed) == 0:
            return "No books currently borrowed"
        for transaction in member.borrowed:
            book = self.find_book(transaction.book_id)
            result.append(f"- {book.title} by {book.author}")
        return '\n'.join(result)