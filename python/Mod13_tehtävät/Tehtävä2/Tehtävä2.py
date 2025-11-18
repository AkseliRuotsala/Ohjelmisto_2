from flask import Flask
import csv

app = Flask(__name__)
airports = {}

with open("airports.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        icao = row["ident"].upper()
        airports[icao] = {
            "Name": row["name"],
            "Municipality": row["municipality"]
        }

@app.route("/")
def home():
    return "Airport API is running"


@app.route("/kentta/<icao>")
def hae_kentta(icao):
    icao = icao.upper()

    if icao in airports:
        data = airports[icao]
        vastaus = {
            "ICAO": icao,
            "Name": data["Name"],
            "Municipality": data["Municipality"]
        }
    else:
        vastaus = {
            "ICAO": icao,
            "Error": "Airport not found"
        }

    return vastaus


app.run(use_reloader=True, host="127.0.0.1", port=3002)
