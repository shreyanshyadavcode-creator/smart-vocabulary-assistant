import os
import sys
from dotenv import load_dotenv
import resend


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.word_generator import return_word
from Database.store import data_add
from Database.word_exists import word_exists
from Database.vocabulary_creation import vocabulary_table

load_dotenv()

# Load Resend API key
resend.api_key = os.getenv("RESEND_API_KEY")


def send_mail():

    # Create table if not exists
    vocabulary_table()

    # Generate unique word
    smart_word = return_word()

    word = smart_word["word"]

    while word_exists(word):
        print("Duplicate Found")
        smart_word = return_word()
        word = smart_word["word"]

    # Save into database
    value = data_add(data=smart_word)

    print(value)

    # Multiple receivers from .env
    # receivers = os.getenv("receivers").split(",")
    # print(receivers)

    # HTML Email
    html = f"""

    <html>

        <body>

            <h2>Today's Word</h2>

            <p><b>Word :</b> {smart_word['word']}</p>

            <p><b>Meaning :</b> {smart_word['meaning']}</p>

            <p><b>Example :</b> {smart_word['example']}</p>

            <p><b>Synonym :</b> {smart_word['synonym']}</p>

        </body>

    </html>

    """

    try:

        response = resend.Emails.send({

            "from": "onboarding@resend.dev",

            "to": "shreyanshyadav.code@gmail.com",

            "subject": "Word of the Day",

            "html": html
        })

        print("Email Sent Successfully")

        # print(response)

        return True

    except Exception as e:

        print("Resend Error:", e)

        return False