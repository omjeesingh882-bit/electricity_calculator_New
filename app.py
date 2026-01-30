from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bill = None
    if request.method == "POST":
        units = float(request.form["units"])

        if units <= 100:
            bill = units * 1.5
        elif units <= 200:
            bill = (100 * 1.5) + (units - 100) * 2.5
        else:
            bill = (100 * 1.5) + (100 * 2.5) + (units - 200) * 4

    return render_template("index.html", bill=bill)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
