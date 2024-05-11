import sqlite3

conn = sqlite3.connect('logs.db', detect_types= sqlite3.PARSE_DECLTYPES)

cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS logs(id INTEGER, entry TEXT);')

cursor.execute('SELECT * FROM pragma_table_info(logs);')

print(cursor.fetchall())
