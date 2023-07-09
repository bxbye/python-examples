"""
    Sample of How to define custom exception class.
    To implement appropriate error handling for scenarios such as borrowing an unavailable book or returning a book that was not borrowed,
    you can define custom exception classes and raise them when these situations occur. 
    Here's an example:
"""
class BookUnavailableError(Exception):
    pass

class BookNotBorrowedError(Exception):
    pass

class Library:
    def __init__(self):
        self.available_books = ["Book 1", "Book 2", "Book 3"]
        self.borrowed_books = []

    def borrow_book(self, book):
        if book in self.available_books:
            self.available_books.remove(book)
            self.borrowed_books.append(book)
            print(f"{book} has been borrowed.")
        else:
            raise BookUnavailableError(f"{book} is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            self.available_books.append(book)
            print(f"{book} has been returned.")
        else:
            raise BookNotBorrowedError(f"{book} was not borrowed.")

# Example usage
library = Library()

try:
    library.borrow_book("Book 1")  # Borrow an available book
    library.borrow_book("Book 4")  # Attempt to borrow an unavailable book
    library.return_book("Book 2")  # Return a borrowed book
    library.return_book("Book 5")  # Attempt to return a book that was not borrowed
except BookUnavailableError as e:
    print(f"Error: {str(e)}")
except BookNotBorrowedError as e:
    print(f"Error: {str(e)}")
