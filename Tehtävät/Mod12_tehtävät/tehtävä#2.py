import json
import requests
city_name=input('Anna kaupungin nimi: ')
API_key=f'6277c29385063a1de39458f9176d2541'
pyyntö = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang=fi'

try:
    vastaus = requests.get(pyyntö)
    print('status code', vastaus.status_code)
    if vastaus.status_code==200:
        data = vastaus.json()
        print(json.dumps(data, indent=2))
        print(f' Sää kohteessa {city_name}:\n{data['main']['temp']} astetta celsiusta\n{data['weather'][0]['description']}')

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")