import requests

url = "http://127.0.0.1:5000/add"

params = {
    'a': 10,
    'b': 20
}

response = requests.get(url, params=params)

data = response.json()

print("Addition Result:", data['result'])