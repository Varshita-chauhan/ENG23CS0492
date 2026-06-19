import requests

# STEP 1: Get Access Token
auth_url = "http://4.224.186.213/evaluation-service/auth"

auth_data = {
    "email": "chauhanvarshita1603@gmail.com",
    "name": "Varshita Chauhan",
    "rollNo": "ENG23CS0492",
    "accessCode": "BgWZSW",
    "clientID": "3594dd63-9a2e-4a46-885f-57ab530a7bb7",
    "clientSecret": "HydwBzgpnmmTrZDT"
}

auth_response = requests.post(auth_url, json=auth_data)

print("Auth Response:")
print(auth_response.json())

token = auth_response.json()["access_token"]


# STEP 2: Logging Function
def Log(stack, level, package, message):
    log_url = "http://4.224.186.213/evaluation-service/logs"

    payload = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        log_url,
        json=payload,
        headers=headers
    )

    print("\nLog Response:")
    print("Status:", response.status_code)
    print(response.text)


# STEP 3: Test Log
Log(
    "backend",
    "info",
    "utils",
    "Application started successfully"
)