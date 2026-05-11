import sys
import os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "word.db"

import sqlite3
def vocabulary_table():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""

    CREATE TABLE IF NOT EXISTS vocabulary (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        word TEXT,

        meaning TEXT,

        example TEXT,

        synonym TEXT
    )

    """)
    
    connection.commit()

    connection.close()
    return True