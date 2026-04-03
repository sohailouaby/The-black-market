from flask import Flask, render_template

app = Flask(__name__)

@app.route("/templates/index.html")
def home():
    return render_template("index.html")

@app.route("/templates/about.html")
def about():
    return render_template("about.html")

@app.route("/templates/guns.html")
def guns():
    return render_template("guns.html")


if __name__ == "__main__":
    app.run(debug=True)