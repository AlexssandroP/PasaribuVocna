import requests

api_key = '189f4d35-af91-43a0-8d76-c0840f8457bf'
word = 'pasaribu'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definitions)