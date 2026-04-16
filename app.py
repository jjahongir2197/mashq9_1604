from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/calc", methods=["POST"])
def calc():

    son1 = float(request.form.get("son1"))
    son2 = float(request.form.get("son2"))
    amal = request.form.get("amal")

    if amal == "+":
        natija = son1 + son2

    elif amal == "-":
        natija = son1 - son2

    elif amal == "*":
        natija = son1 * son2

    elif amal == "/":
        if son2 != 0:
            natija = son1 / son2
        else:
            return "0 ga bo‘lish mumkin emas"

    return f"Natija: {natija}"

app.run(debug=True)
