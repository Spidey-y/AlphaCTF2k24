import sqlite3


def create_db():
    conn = sqlite3.connect('trivia.db')
    c = conn.cursor()
    c.execute(
        '''CREATE TABLE IF NOT EXISTS servers (server_id INTEGER PRIMARY KEY, score INTEGER)''')
    c.execute(
        '''CREATE TABLE IF NOT EXISTS attempts (server_id INTEGER, question TEXT, correct_answer TEXT)''')
    conn.commit()
    conn.close()


def add_server(server_id):
    conn = sqlite3.connect('trivia.db')
    c = conn.cursor()
    c.execute(
        '''INSERT OR IGNORE INTO servers (server_id, score) VALUES (?, ?)''', (server_id, 0))
    conn.commit()
    conn.close()


def add_all_servers(client):
    for guild in client.guilds:
        add_server(guild.id)


def add_one(server_id):
    conn = sqlite3.connect('trivia.db')
    c = conn.cursor()
    c.execute(
        '''UPDATE servers SET score = score + 1 WHERE server_id = ?''', (server_id,))
    conn.commit()
    conn.close()


def remove_one(server_id):
    conn = sqlite3.connect('trivia.db')
    c = conn.cursor()
    c.execute(
        '''UPDATE servers SET score = score - 1 WHERE server_id = ?''', (server_id,))
    conn.commit()
    conn.close()


def reset_score(server_id):
    conn = sqlite3.connect('trivia.db')
    c = conn.cursor()
    c.execute(
        '''UPDATE servers SET score = 0 WHERE server_id = ?''', (server_id,))
    conn.commit()
    conn.close()


def get_score(server_id):
    conn = sqlite3.connect('trivia.db')
    c = conn.cursor()
    c.execute(
        '''SELECT score FROM servers WHERE server_id = ?''', (server_id,))
    score = c.fetchone()
    conn.close()
    return score[0] if score else 0


def get_last_unsolved_attempt(server_id):
    conn = sqlite3.connect('trivia.db')
    c = conn.cursor()
    c.execute(
        '''SELECT * FROM attempts WHERE server_id = ? LIMIT 1''', (server_id,))
    attempt = c.fetchone()
    conn.close()
    return attempt


def add_attempt(server_id, question, correct_answer):
    conn = sqlite3.connect('trivia.db')
    c = conn.cursor()
    c.execute(
        '''INSERT INTO attempts (server_id, question, correct_answer) VALUES (?, ?, ?)''', (server_id, question, correct_answer))
    conn.commit()
    conn.close()


def solve_attempt(server_id):
    conn = sqlite3.connect('trivia.db')
    c = conn.cursor()
    c.execute('''DELETE FROM attempts WHERE server_id = ?''', (server_id,))
    conn.commit()
    conn.close()
