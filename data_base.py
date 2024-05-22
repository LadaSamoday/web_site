import sqlite3


conn = sqlite3.connect('db.db', check_same_thread=False)
cursor = conn.cursor()
def init_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS note(
                    id INTEGER PRIMARY KEY UNIQUE NOT NULL,
                    name TEXT,
                    text TEXT)
                    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS tag(
                    id INTEGER PRIMARY KEY UNIQUE NOT NULL,
                    name TEXT,
                    note_id INTEGER,
                    FOREIGN KEY(note_id) REFERENCES note(id) ON DELETE CASCADE)
                    ''')
    conn.commit()

def add_note_db(name, text):
    cursor.execute('''INSERT INTO note(name, text) VALUES(?, ?)''', (name, text))
    conn.commit()

def get_notes():
    cursor.execute('''SELECT * FROM note''')
    return cursor.fetchall()

def get_note(id):
    cursor.execute('''SELECT * FROM note WHERE id = ?''', (id,))
    return cursor.fetchone()

def delete_note_db(id):
    cursor.execute('''DELETE FROM note WHERE id = ?''', (id,))
    conn.commit()

def update_note_db(id, name, text):
    cursor.execute('''UPDATE note SET text = ?, name = ? WHERE id = ?''', (text, name, id))
    conn.commit()

# init_db()
# add_note('Уборка', 'Протереть пыль')
# print(get_notes())
# update_note(2, 'Уборка 2', 'пыль')
# print(get_notes())
# delete_note(3)

def add_tag(name, note_id):
    cursor.execute('''INSERT INTO tag(name, note_id) VALUES(?, ?)''', (name, note_id))
    conn.commit()

def delete_tag(id):
    cursor.execute('''DELETE FROM tag WHERE id = ?''', (id,))
    conn.commit()

def get_tags(note_id):
    cursor.execute('''SELECT * FROM tag WHERE note_id = ?''', (note_id,))
    return cursor.fetchall()


# add_tag('Пыль', 2)
# print(get_tags(2))
# delete_tag(3)

# conn = sqlite3.connect('db.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS shop(
#                name TEXT,
#                price INT,
#                manufacturer TEXT,
#                sale INT)''')
# cursor.execute('''INSERT INTO shop(name, price, manufacturer, sale) VALUES(?, ?, ?, ?)''',
#                ('Хлеб', 60, 'Хлебзавод1111', 5))
# conn.commit()
# cursor.execute('UPDATE shop SET price = ? WHERE name = ?',('85', 'Хлеб'))
# conn.commit()
# cursor.execute('DELETE FROM shop WHERE price = 60')
# conn.commit()
# cursor.execute('DROP TABLE shop')
# conn.commit()
# cursor.execute('SELECT * FROM shop')
# print(cursor.fetchall())