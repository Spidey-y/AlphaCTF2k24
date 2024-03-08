import sqlite3
from uuid import uuid4


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_db_connection()
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            token TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id TEXT PRIMARY KEY ,
            content TEXT NOT NULL,
            title TEXT NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    c.execute(''' 
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            user_id INTEGER,
            post_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (post_id) REFERENCES posts (id) 
        )
    ''')

    conn.commit()
    c.execute("INSERT or IGNORE INTO users (username, password, token) VALUES (?, ?, ?)",
              ('admin', 'su3r5ecr3tp4ssw0rd852461337', '4dmin_t0k3n1337'))
    conn.commit()
    c.execute("INSERT or IGNORE INTO posts (id, content, user_id, title) VALUES (?, ?, ?, ?)",
              ("kz4ce5", "AlphaCTF{c0nga7s_y0u_g07_4n_x55_50ld13r_1337}", 1, "flag is here shhhhh"))
    conn.commit()
    conn.close()


def user_exists(username):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    return user is not None


def create_user(username, password):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
              (username, password))
    conn.commit()
    conn.close()


def check_token(user_id, token):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id=? AND token=?", (user_id, token))
    user = c.fetchone()
    conn.close()
    return user is not None


def authenticate_user(username, password):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (username, password))
    user = c.fetchone()
    if user:
        token = str(uuid4()).replace('-', '')
        c.execute("UPDATE users SET token=? WHERE id=?",
                  (token, user['id']))
        conn.commit()
        c.execute("SELECT * FROM users WHERE username=? AND password=?",
                  (username, password))
        user = c.fetchone()
    conn.close()
    return user
