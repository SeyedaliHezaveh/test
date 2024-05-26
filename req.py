import requests

url = 'http://localhost:5000/shortUrls'
data = {"url": "https://quera.org"}
response = requests.post(url, data=data, json=data)

print(response.content)