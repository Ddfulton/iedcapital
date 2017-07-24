from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html") 

@app.route("/i")
def i():
    return render_template("i.html")

@app.route("/e")
def e():
    return render_template("e.html")

@app.route("/d")
def d():
    return render_template("d.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
