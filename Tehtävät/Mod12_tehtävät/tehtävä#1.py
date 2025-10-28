import json
import requests


pyyntö = 'https://api.chucknorris.io/jokes/random'

try:
    vastaus = requests.get(pyyntö)
    print('status code', vastaus.status_code)
    if vastaus.status_code==200:
        data = vastaus.json()
        print(json.dumps(data, indent=2))
        print(data['value'])

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")