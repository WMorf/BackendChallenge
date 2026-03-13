from appCRUD import *

buildDB()

while True:
        print("\nLibrary Menu")
        print("1. Create book")
        print("2. Create author")
        print("3. View books")
        print("4. View authors")
        print("5. Add book")
        print("6. Add author")
        print("7. Delete book")
        print("8. Delete author")
        print("9. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            createBook()
        elif choice == "2":
            createAuthor()
        elif choice == "3":
            showBooks()
        elif choice == "4":
            showAuthors()
        elif choice == "5":
            createBook()
        elif choice == "6":
            createAuthor()
        elif choice == "7":
            removeBook()
        elif choice == "8":
            removeAuthor()
        elif choice == "9":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")
