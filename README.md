# Program for managing a library. Has the procedural version and a refactored objected-oriented version. Includes tests.

## File format:
- README.md # This file
- procedural_version/
  - library_procedural.py # Procedural version
  - test_procedural.py # Procedural test
- oop_solution/
  - library_oop.py # OOP version
  - test_oop.py # OOP test


## Explanation for oop_solution/library_oop.py:

### Book has the attributes for:
- book id
- title
- author
- available copies
- total copies

It has protected methods to borrow and return, modifying the available copies.

### Member has the attributes for:
- member id
- name
- email
- list of borrowed books (list of transactions)

It has protected methods to borrow and return, modifying the list of transactions.

### Transaction has the attributes for:
- book id

Currently unnecessary but is able to be expanded if needed (such as adding a date of borrowing).

### Library has the attributes for:
- list of books
- list of members

It has methods to:
- add books and members
- find books and members from their ID
- a system for borrowing and returning books
- display available books
- display a member's borrowed books, given a member ID

## Testing - Test suite test_oop.py includes:
- Basic Operations
  - Adding books and members
  - Borrowing and returning books
  - Displaying information

- Edge Cases
  - Borrowing unavailable books
  - Exceeding borrowing limit
  - Returning books not borrowed
  - Non-existent books/members

## How to run test code
Copy oop_solution or procedural_version, and run the associated test_\[version].py.