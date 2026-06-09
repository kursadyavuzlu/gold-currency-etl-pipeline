import requests

url="https://api.frankfurter.dev/v2/rates"

response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print("FAIL REQUEST, Status Code: {response.status_code}")

