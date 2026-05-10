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

def send_mail():
    smart_word = return_word()
    word = smart_word['word']
            
    while(word_exists(word) != 0 ):
        data = return_word()
        word = data['word']
    else : 
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

        with smtplib.SMTP("smtp.gmail.com",587) as server:
            server.starttls()
            server.login(sender,password)
            server.send_message(message)
            server.quit()
            
        print("sent")
        return True
        
        
    


send_mail()