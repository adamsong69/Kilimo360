import sqlite3, json, os
DB_PATH = os.path.join(os.getcwd(), 'data', 'submissions.db')
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS submissions (id INTEGER PRIMARY KEY, form_name TEXT, json TEXT, created_at TEXT)''')
    conn.commit()
    conn.close()

def save_submission(form_name, data_json):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO submissions (form_name, json, created_at) VALUES (?,?,datetime("now"))',(form_name, json.dumps(data_json)))
    conn.commit()
    conn.close()
