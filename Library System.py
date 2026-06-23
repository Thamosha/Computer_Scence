#Option A - Library Book Management System

library = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = {"title": title, "author": author, "available": True}
    library.append(book)

    print("Book added")


def view_books():
    if len(library) == 0:
        print("No books available")
    else:
        i = 0
        for book in library:
            i = i + 1

            if book["available"] == True:
                status = "Available"
            else:
                status = "Borrowed"

            print(i, "-", book["title"], "-", status)
        print()


def search_book():
    title = input("Enter book title: ")

    for book in library:
        if book["title"]==title:
            if book["available"]==True:
                print("Book is available")
            elif book["available"]==False:
                print("Book is borrowed")
            return
    print("Book not found")

def borrow_book():
    title = input("Enter book title: ")

    for book in library:
        if book["title"] == title:
            if book["available"] == True:
                print("Borrowed")
                book["available"]= False
            else:
                print("Already borrowed")
            return

    print("Book not found")


def return_book():
    title = input("Enter book title: ")

    for book in library:
        if book["title"] == title:
            if book["available"] == False:
                print("Returned")
                book["available"]= True
            else:
                print("Not borrowed")
            return

    print("Book not found")


def count_books():
    count = 0

    for book in library:
        if book["available"] == True:
            count = count + 1

    print("Available books:", count)


while True:
    print("----- Menu -----")
    print("1 Add book")
    print("2 View books")
    print("3 Search book")
    print("4 Borrow book")
    print("5 Return book")
    print("6 Count books")
    print("7 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        borrow_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        count_books()
    elif choice == "7":
        print("End")
        break
    else:
        print("Wrong choice")
