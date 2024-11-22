import add_books
import view_all_books

all_books = []

while True:
    print("Welcome To Library Management System")
    print("0. Exit")
    print("1. Add Book")
    print("2. View all books")
    
    menu = input("\nSelect any number: ")
    
    if menu == "0":
        print("Thanks for use library management system")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    else: 
        print("Choose a valid number")

        