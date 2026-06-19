import requests

url = "http://4.224.186.213/evaluation-service/auth"

data = {
    "email": "chauhanvarshita1603@gmail.com",
    "name": "Varshita Chauhan",
    "rollNo": "ENG23CS0492",
    "accessCode": "BgWZSW",
    "clientID" :"3594dd63-9a2e-4a46-885f-57ab530a7bb7",
    "clientSecret":"HydwBzgpnmmTrZDT"
}

response = requests.post(url, json=data)

print(response.json())