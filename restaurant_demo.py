# file: restaurant_demo.py
from flask import Flask, render_template, request, url_for
import datetime

app = Flask(__name__)
app.jinja_env.globals['now'] = datetime.datetime.utcnow

@app.route("/")
def reservation_form():
    return render_template("reservation.html")

@app.route("/confirm", methods=["POST"])
def confirm():
    message = f"Reservation confirmed for {request.form['name']} on {request.form['date']}"
    return render_template(
        "confirm.html",
        name=request.form["name"],
        phone=request.form["phone"],
        date=request.form["date"],
        time=request.form["time"],
        size=request.form["size"],
        message=message,
    )

@app.route("/daily-report")
def daily_report():
    today = datetime.date.today().strftime("%B %d, %Y")
    return render_template("report.html", today=today)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)