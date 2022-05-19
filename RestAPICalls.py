import requests

print("Enter your name: ")
name = input()
base_url = 'https://api.nationalize.io/?name='+name
res = requests.get(base_url)
data = res.json()
print(data)
#print(type(data))
print(data['country'])