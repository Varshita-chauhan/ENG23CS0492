import requests

url = "http://4.224.186.213/evaluation-service/register"

data = {
    "email": "chauhanvarshita1603@gmail.com",
    "name": "Varshita Chauhan",
    "mobileNo": "9341971911",
    "githubUsername": "Varshita-chauhan",
    "rollNo": "ENG23CS0492",
    "accessCode": "BgWZSW"
}

response = requests.post(url, json=data)

print(response.json())