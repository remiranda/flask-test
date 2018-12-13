from flask import Flask
app = Flask(__name__)

@app.route("/acerca")
def helloword():
    return "<h1 style='color:green'>Primer Hello ...! </h1>"


@app.route("/suma/<int:a>/<int:b>")
@app.route("/suma/<float:a>/<float:b>")
def suma(a,b):
    suma_ab = a + b
    return "La suma de {} + {} es : {}".format(a,b,suma_ab)


@app.route("/divide/<int:a>/<int:b>")
@app.route("/divide/<float:a>/<float:b>")
def division(a,b=0):
    if b != 0 :
        div_ab = a / b
        return "La division de {} / {} es : {}".format(a,b,div_ab)
    else:
        return "La division no se puede realizar ; el divisor es 0 "

@app.errorhandler(404)
def error(error):
    return "la Url no existe ...!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


