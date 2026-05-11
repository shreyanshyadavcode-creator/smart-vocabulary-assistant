import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

user = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def return_word():
    response = user.chat.completions.create(
        model="gpt-3.5-turbo",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an English vocabulary teacher. "
                    "Generate exactly in JSON format with these content:\n\n"
                    "word: <word>\n"
                    "meaning : <Hindi meaning>\n"
                    "example : <sentence>\n "
                    "synonym : <Synonym of the word>\n"
                )
            },
            {
                "role": "user",
                "content": (
                    "Give me one advanced English word that is useful "
                    "in day-to-day life and leaves an impact on people."
                )
            }
        ]
    )

    data = json.loads(response.choices[0].message.content)
    
    return data

#test code for while loop used in emai_sender.py file

# def return_word():
#     word = {
#         'word':'DECISION',
#         'meaning' : "Determinantion",
#         'example' : "12345",
#         'synonym' : "qwerty"
#     }
#     return word


if __name__ == '__main__':
    result = return_word()
    print(result)