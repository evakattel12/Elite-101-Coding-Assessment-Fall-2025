from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a menu with choices.
def menu():
    print("Welcome to the library catalog!")
    print("1. View Available Books\n 2. Search (Author or Genre)\n 3. Checkout a Book\n 4. Return\n 5. Overdue\n 6. Top 3 Most Checked Out Books\n 7. Exit")
    catalog_in_use = True
    while catalog_in_use == True:
        user_input = input("Please enter a number (1-7): ")
        if user_input == "1":
            viewing()
        elif user_input == "2":
            search()
        #elif user_input == "3":
            # Checkout
        #elif user_input == "4":
             # Return
        #elif user_input == "5":
            # Overdue
        #elif user_input == "6":
            # View Top 3 most checked out books
        elif user_input == "7":
            print("Thank you for checking out the library catalog.")
            catalog_in_use = False
        else:
            user_input = ("Invalid input, please enter a number (1-7): ")


def viewing():
    print("")
    print("----Available Books----")
    for books in library_books:
        print("----------------")
        for key, value in books.items():
            print(f"{key}: {value}")
    print("----------------")
# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search():
    search_item = input("Please enter a genre or author's name: ")
    for books in library_books:
        for key, value in books.items():
            if key.lower() == "history" and search_item.lower() == "history":
                print(f"{key[3]}: {value[3]}")

"""
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
"""
if __name__ == "__main__":
    menu()
    pass
