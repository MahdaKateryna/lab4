from flask import Flask, render_template, request
from db import insert_data, get_all_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        insert_data(name, email)
    data = get_all_data()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
