import os
from dotenv import load_dotenv
import resend

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

try:

    response = resend.Emails.send({

        "from": "onboarding@resend.dev",

        "to": ["shreyanshyadav.code@gmail.com"],

        "subject": "Railway Resend Test",

        "html": "<h1>Hello from Railway</h1>"

    })

    print(response)

except Exception as e:

    print("ERROR:", e)