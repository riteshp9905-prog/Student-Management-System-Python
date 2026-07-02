import sqlite3

DB_NAME = "students.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            roll TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT,
            marks REAL,
            percentage REAL,
            grade TEXT
        )
    """)

    conn.commit()
    conn.close()


# Create table automatically
create_table()