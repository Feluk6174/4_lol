import requests

r = requests.get('http://localhost:8000/upos-1:p:1,2')

r = requests.get('http://localhost:8000/shoot-1:d:17,16')

r = requests.get('http://localhost:8000/start-1:p:1,1')

print(r.text)