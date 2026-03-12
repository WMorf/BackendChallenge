from appCRUD import *

init_db()

while True:
        print("\nLibrary Menu")
        print("1. View books")
        print("2. Add book")
        print("3. Delete book")
        print("4. View summary")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_books()

        else:
            print("Invalid choice. Try again.")