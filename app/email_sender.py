import os
import sys
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()
from app.word_generator import return_word
from Database.store import data_add
from Database.word_exists import word_exists
from Database.vocabulary_creation import vocabulary_table

def send_mail():
    table_value = vocabulary_table()
    smart_word = return_word()
    word = smart_word['word']
            
    while word_exists(word):
        print("Dupilcate Found")
        smart_word = return_word()
        word = smart_word['word']    
    
    value = data_add(data= smart_word)
    sender = os.getenv("sender")
    reciever = os.getenv("reciever")
    password = os.getenv("password")

    html = f"""
    <html>
        <body>
            <h2>Today's Word</h2>
            
            <p><b>Word : </b>{smart_word['word']}</p>
            
            <p><b>Meaning : </b>{smart_word['meaning']}</p>
            
            <p><b>Example : </b>{smart_word['example']}</p>
        
            <p><b>Synonym : </b>{smart_word['synonym']}</p>
        </body>
    </html>
    """

    message = MIMEText(html, "html")
    message["subject"] = "word of the day"
    message["from"] = sender
    message["to"] = reciever

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.starttls()
        server.login(sender,password)
        server.send_message(message)
        server.quit()
       
    print("sent")

