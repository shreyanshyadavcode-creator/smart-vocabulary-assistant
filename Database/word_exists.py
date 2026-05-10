import sys
import os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.word_generator import return_word
data = return_word()

BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "word.db"

import sqlite3

def word_exists(word): 
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT 1 FROM vocabulary WHERE word = ?" ,
            (word,)
        )
        result = cursor.fetchone()
        connection.close()
        return result
    
print(word_exists(data['word']))
    