import sqlite3

DB_PATH = "library_relationships/relationships.db"


def create_table():
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS borrowed_books (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            book_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (book_id) REFERENCES books(id)
        )
        """)


def show_data_users():
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
        SELECT id, name FROM users
""",
        )
        result = cursor.fetchall()
        return result


def show_data_books():
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT id, title, author FROM books
""")
        result = cursor.fetchall()
        return result


def show_borrowed_details():
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT users.name, books.title, books.author 
        FROM borrowed_books
        JOIN users ON borrowed_books.user_id = users.id
        JOIN books ON borrowed_books.book_id = books.id
""")
        result = cursor.fetchall()
        return result

def add_user(name):
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
        INSERT INTO users(name)
            VALUES(?)
""",
            (name,),
        )


def add_book(title, author):
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
        INSERT INTO books(title, author)
            VALUES(?,?)
""",
            (
                title,
                author,
            ),
        )

def check_user(name):
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
        SELECT id FROM users
        WHERE name = ?
""",
            (name,),
        )
        result = cursor.fetchone()
        return result
    
def check_book(id):
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
        SELECT id FROM books
        WHERE id = ?
""",
            (id,),
        )

        result = cursor.fetchone()
        return result
    
def check_borrowed(book_id, user_id):
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
        SELECT id FROM borrowed_books
        WHERE book_id = ? AND user_id = ?
""",
            (book_id,user_id),
        )
        result = cursor.fetchone()
        return result
    
def search_title_book(book_title):
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
        SELECT id, title, author FROM books
        WHERE title LIKE(?)

""",
            (f"%{book_title}%",),
        )
        result = cursor.fetchall()
        return result
def search_borrowed_books(user_id):
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
        SELECT user_id, book_id, books.title, books.author
        FROM borrowed_books
        JOIN books ON borrowed_books.book_id = books.id
        WHERE user_id = ?
""",
        (
            user_id,
        ),
        )
        result = cursor.fetchall()
        return result
    


def add_borrow_book(book_id, user_id):
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
        INSERT INTO borrowed_books(user_id, book_id)
        VALUES (?,?)
""",
            (
                user_id,
                book_id,
            ),
        )
        return "success"

def return_book(user_id, book_id):
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
        DELETE FROM borrowed_books
        WHERE user_id = ? AND book_id = ?

""",
        (
            user_id,
            book_id,
        ),
        )
        return "success"
    
