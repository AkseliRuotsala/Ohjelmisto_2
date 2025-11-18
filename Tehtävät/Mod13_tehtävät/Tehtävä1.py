from flask import Flask, jsonify, request

app = Flask(__name__)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

@app.route("/alkuluku/<int:number>", methods=["GET"])
def check_prime(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3001, debug=True)
