import sqlite3  # built-in library for working with SQLite database

def get_db():
    conn = sqlite3.connect('skills.db')  # connect to database file
    conn.row_factory = sqlite3.Row  # return rows as dictionaries instead of tuples
    return conn  # return connection object

def init_db():
    conn = get_db()  # get database connection
    cursor = conn.cursor()  # create cursor to execute SQL commands
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')
    conn.commit()  # save changes
    conn.close()  # close connection