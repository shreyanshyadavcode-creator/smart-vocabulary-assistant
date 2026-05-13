import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "word.db"


def word_exists(word):

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(

        "SELECT 1 FROM vocabulary WHERE word = ?",

        (word,)
    )

    result = cursor.fetchone()

    connection.close()

    return result