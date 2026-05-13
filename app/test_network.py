import requests

try:

    response = requests.get("https://google.com")

    print(response.status_code)

except Exception as e:

    print("ERROR:", e)