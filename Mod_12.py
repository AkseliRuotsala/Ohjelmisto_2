#Ulkoisen rajapinnan käyttö

import requests
import json
'''
hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana
vastaus = requests.get(pyyntö).json()

#tämä on lähinnä koko vastauksen muotoilua varten
print(json.dumps(vastaus, indent=2))

sanakirja=vastaus[0]
print(f'Name: {sanakirja['show']['name']}\nGenre: {sanakirja['show']['genres'][0]}')

#lista [0][0]
sanakirja['show']['name']
'''

import json
import requests

hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(json.dumps(json_vastaus, indent=2))
        for a in json_vastaus:
            print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")