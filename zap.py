import requests

url = 'https://api.chat-api.com/instance123/message?token=83763g87x'
data = ({"phone": "+5516981528800"}, {"body": "Hello, World!"})
res = requests.post(url, json=data)
print (res.text)
