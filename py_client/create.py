import requests

endpoint = "http://127.0.0.1:8000/api/products/"

headers = {"Authorization": 'Bearer 14980a8ff704fef073b8d2905e5e13046a6d93f1'}

data = {
    "title": "New New",
    "price": 958,
}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())
print(get_response.status_code)
