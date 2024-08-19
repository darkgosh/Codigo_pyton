import requests

url = "https://openapiv1.coinstats.app/portfolio/coins"

headers = {
    "accept": "application/json",
    "X-API-KEY": "Na2rcfyKmIhX3zRnd/L+3k5R/8kNTD97PFnj2W1vbNA="
}

response = requests.get(url, headers=headers)

print(response.text)