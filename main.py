from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
"""For book in books:
    Print books
        Table? One sentence at a time?
"""
# Solve

def viewing():
    for books in library_books:
        print(f"ID: {books.id}\nAuthor: {books.author}\nTitle: {books.title}\n")
# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
user_ask = input("Enter author or genre name: ")
for book in library_books:
    if user_ask == "Fantasy":
        print(book.title)
    elif user_ask == "Rick Riordan":
        print(book.title)


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
if book != taken:
    book = unavailable
    book is due in 2 weeks from today
    increments += 1
else:
    print("Already checked out.")

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def return_book():
    if book == returned:
        book == True
        clear the due date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def overdue():
    if due_date == today-1 and book == checked out:
        print("Book overdue")


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    viewing()
    pass
