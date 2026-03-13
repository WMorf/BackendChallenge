import sqlite3

db = 'challenge.db'

#for code readability
def dbConnect():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn

def buildDB():
    conn = dbConnect()
    with open("schema.sql", "r", encoding="utf-8") as file:
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