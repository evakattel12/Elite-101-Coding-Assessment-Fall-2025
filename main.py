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
            #checkout()
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
    search_item = input("Please enter a genre or author name: ")
    if search_item.lower() == "historical" or search_item.lower() == "harper lee":
        print(library_books[1])
    elif search_item.lower() == "dystopian" or search_item.lower() == "george orwell":
        print(library_books[3])
    elif search_item.lower() == "science fiction" or search_item.lower() == "raw bradbury":
        print(library_books[6])
    elif search_item.lower() == "fantasy":
        print(library_books[0])
        print(library_books[5])
    elif search_item.lower() == "classic" or search_item.lower() == "f. scott fitzgerald":
        print(library_books[2])
    elif search_item.lower() == "coming-of-age" or search_item.lower() == "j.d. salinger":
        print(library_books[7])
    elif search_item.lower() == "romance" or search_item.lower() == "jane austen":
        print(library_books[4])
    elif search_item.lower() == "j.r.r. tolkien":
        print(library_books[5])
    elif search_item.lower() == "rick riordan":
        print(library_books[0])
    else:
        search_item = ("Invalid input, please enter a genre or author name: ")

#fantasy, romance, science fiction, dystopian


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

"""
# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

class Books:
    def __init__(self, book_Id, title, author, genre, available, due_date, checkouts):
        self.book_Id = book_Id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts
    def features(self):
        return {"Book ID: ", self.book_Id, "Title: ", self.title, "Author: ", self.author, "Genre: ", self.genre, "Available: ", self.available, "Due Date: ", self.due_date, "Checkouts: ", self.checkouts}
    
# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    menu()
    pass
