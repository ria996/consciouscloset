import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Item type':1, 'Color':1, 'Size':2, 'Material':4})

print(r.json())