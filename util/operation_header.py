import requests
import json

url = 'http://127.0.0.1:10086/add/'

data = {"username": "admin", "password": "admin"}

header = {"content-type":"application/json"}

res = requests.post(url,json=data,headers=header).json()
print(type(res),res)