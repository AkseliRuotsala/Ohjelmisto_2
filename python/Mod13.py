from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def moikka():
    return 'terve maailma'

#http://127.0.0.1:3000/summa?luku1=13&luku2=28
#tämä on route eli reitti
@app.route('/summa')
def summa():
    print(request.args)
    args = request.args
    luku1 = float(args.get("luku1"))
    luku2 = float(args.get("luku2"))
    summa = luku1 + luku2

#itse tehty json vastaus
    vastaus = {
        "luku1" : luku1,
        "luku2" : luku2,
        "summa" : summa


    }
    return vastaus


#http://127.0.0.1:3000/kaiku/huhuuuuu

@app.route('/kaiku/<teksti>/<kertaa>')
def kaiku(teksti,kertaa):
    print(teksti,kertaa)
    tulos=""
    for i in range (int(kertaa)):
        tulos += tulos + " "



    vastaus = {
        "kaiku": teksti + " " + teksti
    }
    return vastaus

app.run(use_reloader=True, host='127.0.0.1', port=3000)