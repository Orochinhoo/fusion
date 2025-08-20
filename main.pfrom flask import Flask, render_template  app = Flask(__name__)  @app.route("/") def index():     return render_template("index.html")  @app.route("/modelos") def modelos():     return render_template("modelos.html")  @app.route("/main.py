from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/modelos")
def modelos():
    return render_template("modelos.html")

@app.route("/contato")
def contatos():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
