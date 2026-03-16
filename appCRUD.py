import sqlite3

db = 'challenge.db'

#DATABASE
def dbConnect():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row # Enable dictionary-like access of rows
    return conn

def buildDB():
    conn = dbConnect()
    with open("schema.sql", "r", encoding="utf-8") as file:
        conn.executescript(file.read())
    conn.commit()
    conn.close()

def seedDB():
    conn = dbConnect()
    with open("seed.sql", "r", encoding="utf-8") as file:
        conn.executescript(file.read())
    conn.commit()
    conn.close()

#BOOKS
def addBook(title, author_id, published_date):
    conn = dbConnect()
    conn.execute(
        "INSERT INTO Books (title, author_id, published_date) VALUES (?, ?, ?)",
        (title, author_id, published_date)
    )
    conn.commit()
    conn.close()

def createBook():
    print("\nAdd a New Book")
    title = input("Enter book title: ").strip() 
    if not title:
        print("Title cannot be empty.")
        return
    showAuthors()
    try:
        author_id = int(input("\nEnter author ID: ").strip())
    except ValueError:
        print("Invalid author ID.")
        return

    published_date = input("Enter published date (YYYY-MM-DD): ").strip()
    if not published_date:
        print("Published date cannot be empty.")
        return

    addBook(title, author_id, published_date)
    print("Book added.")

def getBooks():
    conn = dbConnect()
    rows = conn.execute("""
        SELECT Books.id, Books.title, Authors.author_name, Books.published_date
        FROM Books
        JOIN Authors ON Books.author_id = Authors.id
        ORDER BY Books.id
    """).fetchall()
    conn.close()
    return rows

def showBooks():
    books = getBooks()
    if not books:
        print("\nNo books found.")
        return
    print("\nBooks:")
    for book in books:
        print(f"{book['id']}. {book['title']} - {book['author_name']} ({book['published_date']})")

def deleteBook(book_id):
    conn = dbConnect()
    cursor = conn.execute("DELETE FROM Books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0

def removeBook():
    print("\nDelete a Book")
    try:
        book_id = int(input("Enter book ID to delete: ").strip())
    except ValueError:
        print("Invalid book ID.")
        return
    deleted = deleteBook(book_id)
    if deleted:
        print("Book deleted.")
    else:
        print("Book not found.")

def updateBook(book_id, title, author_id, published_date):
    conn = dbConnect()
    cursor = conn.execute("""
        UPDATE Books
        SET title = ?, author_id = ?, published_date = ?
        WHERE id = ?
    """, (title, author_id, published_date, book_id))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0

def getBookById(book_id):
    conn = dbConnect()
    row = conn.execute("""
        SELECT Books.id, Books.title, Books.author_id, Authors.author_name, Books.published_date
        FROM Books
        LEFT JOIN Authors ON Books.author_id = Authors.id
        WHERE Books.id = ?
    """, (book_id,)).fetchone()
    conn.close()
    return row

def findBook():
    try:
        book_id = int(input("\nEnter book ID: ").strip())
    except ValueError:
        print("Invalid book ID.")
        return

    book = getBookById(book_id)
    if not book:
        print("Book not found.")
        return

    author_name = book["author_name"] if book["author_name"] else "Unknown Author"
    print(f"\nBook Found:")
    print(f"ID: {book['id']}")
    print(f"Title: {book['title']}")
    print(f"Author: {author_name}")
    print(f"Published: {book['published_date']}")

    action = input("\nType U to update, D to delete, or press Enter to go back: ").strip().lower()

    if action == "u":
        new_title = input("New title: ").strip()
        showAuthors()

        try:
            new_author_id = int(input("New author ID: ").strip())
        except ValueError:
            print("Invalid author ID.")
            return

        new_published_date = input("New published date (YYYY-MM-DD): ").strip()

        updated = updateBook(book_id, new_title, new_author_id, new_published_date)
        if updated:
            print("Book updated.")
        else:
            print("Book update failed.")

    elif action == "d":
        deleted = deleteBook(book_id)
        if deleted:
            print("Book deleted.")
        else:
            print("Book delete failed.")

def getMostRecentBook():
    conn = dbConnect()

    row = conn.execute("""
        SELECT Books.id, Books.title, Authors.author_name, Books.published_date
        FROM Books
        LEFT JOIN Authors ON Books.author_id = Authors.id
        ORDER BY Books.id DESC
        LIMIT 1
    """).fetchone()

    conn.close()
    return row

#Authors
def addAuthor(author_name, birth_date):
    conn = dbConnect()
    conn.execute(
        "INSERT INTO Authors (author_name, birth_date) VALUES (?, ?)",
        (author_name, birth_date)
    )
    conn.commit()
    conn.close()

def createAuthor():
    print("\nAdd a New Author")
    author_name = input("Enter author name: ").strip()
    if not author_name:
        print("Author name cannot be empty.")
        return
    birth_date = input("Enter birth date (YYYY-MM-DD): ").strip()
    if not birth_date:
        print("Birth date cannot be empty.")
        return
    addAuthor(author_name, birth_date)
    print("Author added.")

def getAuthors():
    conn = dbConnect()
    rows = conn.execute("""
        SELECT id, author_name, birth_date
        FROM Authors
        ORDER BY id
    """).fetchall()
    conn.close()
    return rows

def showAuthors():
    authors = getAuthors()
    if not authors:
        print("\nNo authors found.")
        return
    print("\nAuthors:")
    for author in authors:
        print(f"{author['id']}. {author['author_name']} (Born: {author['birth_date']})")

def deleteAuthor(author_id):
    conn = dbConnect()
    cursor = conn.execute("DELETE FROM Authors WHERE id = ?", (author_id,))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0

def removeAuthor():
    print("\nDelete an Author")
    try:
        author_id = int(input("Enter author ID to delete: ").strip())
    except ValueError:
        print("Invalid author ID.")
        return

    deleted = deleteAuthor(author_id)
    if deleted:
        print("Author deleted.")
    else:
        print("Author not found.")

def updateAuthor(author_id, author_name, birth_date):
    conn = dbConnect()
    cursor = conn.execute("""
        UPDATE Authors
        SET author_name = ?, birth_date = ?
        WHERE id = ?
    """, (author_name, birth_date, author_id))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0

def getAuthorById(author_id):
    conn = dbConnect()
    row = conn.execute("SELECT id, author_name, birth_date FROM Authors WHERE id = ?", (author_id,)).fetchone()
    conn.close()
    return row

def findAuthor():
    try:
        author_id = int(input("\nEnter author ID: ").strip())
    except ValueError:
        print("Invalid author ID.")
        return

    author = getAuthorById(author_id)
    if not author:
        print("Author not found.")
        return

    print(f"\nAuthor Found:")
    print(f"ID: {author['id']}")
    print(f"Name: {author['author_name']}")
    print(f"Birth Date: {author['birth_date']}")

    action = input("\nType U to update, D to delete, or press Enter to go back: ").strip().lower()

    if action == "u":
        new_name = input("New author name: ").strip()
        new_birth_date = input("New birth date (YYYY-MM-DD): ").strip()

        updated = updateAuthor(author_id, new_name, new_birth_date)
        if updated:
            print("Author updated.")
        else:
            print("Author update failed.")

    elif action == "d":
        deleted = deleteAuthor(author_id)
        if deleted:
            print("Author deleted.")
        else:
            print("Author delete failed.")
            
def getMostRecentAuthor():
    conn = dbConnect()

    row = conn.execute("""
        SELECT id, author_name, birth_date
        FROM Authors
        ORDER BY id DESC
        LIMIT 1
    """).fetchone()

    conn.close()
    return row