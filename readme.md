Library Management System (OOP Refactor)

- Project Overview
This project refactors a procedural-style library management system into an object-oriented design using Python. The system allows users to manage books and members, and supports borrowing and returning operations with proper validations.

- Project Structure

library-management-oop/
│
├── README.md
│
├── procedural_version/
│   ├── library_procedural.py         # Original procedural code
│   └── test_procedural.py            # Test suite for procedural version
│
├── oop_solution/
│   ├── library_oop.py                # Refactored OOP implementation
│   └── test_oop.py                   # Test suite for OOP version


- Design Overview

Book Class
- Attributes: id, title, author, total_copies, available_copies
- Purpose: Represents a book and tracks its availability


Member Class
- Attributes: id, name, email, borrowed_books
- Purpose: Represents a library member and manages their borrowed books


- books
Library Class
- Attributes: books, members, borrowed_books
- Methods:
- add_book(book)
- add_member(member)
- borrow_book(member_id, book_id)
- return_book(member_id, book_id)
- display_available_books()
- display_member_books(member_id)


- Testing

Test Coverage
The test_oop.py file includes comprehensive tests for:
- Basic Operations
- Adding books and members
- Borrowing and returning books
- Displaying available books and member borrow lists
- Edge Cases
- Borrowing unavailable books
- Exceeding borrowing limit (3 books max)
- Returning books not borrowed
- Handling non-existent books or members


How to Run
To run the test suite, execute test_oop.py directly:


Git Version Control
The following commits were made during development:
- (Missed) Initial commit for procedural code conversion
- Book class implemented and tested
- Member class implemented and tested
- Library class implemented and tested
- Final integration and testing of all classes
- git commit readme (i forgot to add it to Final commit)
Note: The first commit was unintentionally skipped during setup. The procedural code was already complete and used as reference.
