import sqlite3

db = 'challenge.db'

def get_connection():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    with open("schema.sql", "r", encoding="utf-8") as file:
        conn.executescript(file.read())
    conn.commit()
    conn.close()

def get_books():
    conn = get_connection()
    rows = conn.execute("""
        SELECT Books.id, Books.title, Authors.author_name, Books.published_date
        FROM Books
        JOIN Authors ON Books.author_id = Authors.id
        ORDER BY Books.id
    """).fetchall()
    conn.close()
    return rows

def show_books():
    books = get_books()
    if not books:
        print("\nNo books found.")
        return
    print("\nBooks:")
    for book in books:
        print(f"{book['id']}. {book['title']} - {book['author_name']} ({book['published_date']})")