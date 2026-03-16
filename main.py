from appCRUD import *

choice = input("Build database? (y/n): ").strip().lower()

while True:
    if choice == "y":
        buildDB()
        break
    elif choice == "n":
        break
    else:
        print("Invalid choice. Try again.")

choice = input("Seed database? (y/n): ").strip().lower()

while True:
    if choice == "y":
        seedDB()
        break
    elif choice == "n":
        break
    else:
        print("Invalid choice. Try again.")


while True:
        print("\nDatabase Menu")
        print("1. Manage Books")
        print("2. Manage Authors")
        print("3. API")
        print("4. Show Total Records")
        print("5. Show Most Recent Record")
        print("6. Show All")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            while True:
                print("\nBooks Menu")
                print("1. Add Book")
                print("2. Show Books")
                print("3. Edit/Delete Book")
                print("3. Back to Main Menu")

                book_choice = input("Choose an option: ").strip()

                if book_choice == "1":
                    createBook()
                elif book_choice == "2":
                    showBooks()
                elif book_choice == "3":
                    break

        elif choice == "2":
            while True:
                print("\nAuthors Menu")
                print("1. Add Author")
                print("2. Show Authors")
                print("3. Edit/Delete Author")
                print("4. Show Author's Books")
                print("5. Back to Main Menu")

                author_choice = input("Choose an option: ").strip()

                if author_choice == "1":
                    createAuthor()
                elif author_choice == "2":
                    showAuthors()
                elif author_choice == "3":
                    findAuthor()
                elif author_choice == "4":
                    author_id = input("Enter author ID: ").strip()
                    try:
                        author_id = int(author_id)
                        showAuthorBooks(author_id)
                    except ValueError:
                        print("Invalid author ID.")
                elif author_choice == "5":
                    break

        elif choice == "3":
            print("\nAPI functionality not implemented yet.")

        elif choice == "4":
            print("\nTotal Records:")
            print(f"Books: {len(getBooks())}")
            print(f"Authors: {len(getAuthors())}")

        elif choice == "5":
            print("\nMost Recent Record:")
            recent_book = getMostRecentBook()
            recent_author = getMostRecentAuthor()
            if recent_book:
                print(f"Most Recent Book: {recent_book['title']} by {recent_book['author_name']} (Published: {recent_book['published_date']})")
            else:
                print("No books found.")
            if recent_author:
                print(f"Most Recent Author: {recent_author['author_name']} (Born: {recent_author['birth_date']})")
            else:
                print("No authors found.")


        elif choice == "6":
            print("\nAll Books:")
            showBooks()
            print("\nAll Authors:")
            showAuthors()

        elif choice == "7":
            print("Goodbye.")
            break

        else:
             print("Invalid choice. Try again.")
