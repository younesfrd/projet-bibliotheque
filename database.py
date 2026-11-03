import sqlite3

def get_connection():
    return sqlite3.connect("bibliotheque.db")
def initialiser_base():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            auteur TEXT NOT NULL,
            annee INTEGER NOT NULL,
            disponible INTEGER DEFAULT 1
        )
    """)
    conn.commit()
    conn.close()
initialiser_base()