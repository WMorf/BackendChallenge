CREATE TABLE IF NOT EXISTS Authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name TEXT NOT NULL,
    birth_date DATE
);

CREATE TABLE IF NOT EXISTS Books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    published_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(id)
);

INSERT INTO Authors (author_name, birth_date) VALUES
('F. Scott Fitzgerald', '1896-09-24'),
('Harper Lee', '1926-04-28'),
('George Orwell', '1903-06-25'),
('Jane Austen', '1775-12-16'),
('Isaac Asimov', '1920-01-02');

INSERT INTO Books (title, author_id, published_date) VALUES
('The Great Gatsby', 1, '1925-04-10'),
('To Kill a Mockingbird', 2, '1960-07-11'),
('1984', 3, '1949-06-08'),
('Pride and Prejudice', 4, '1813-01-28'),
('Animal Farm', 3, '1945-08-17');