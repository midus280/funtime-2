from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    today = datetime.today()
    return render_template("index.html", month=today.month, day=today.day)

@app.route("/booking", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        name = request.form.get("name")
        ticket_type = request.form.get("ticket_type")
        num_tickets = request.form.get("num_tickets")
        date = request.form.get("date")
        return render_template("confirmation.html", name=name, ticket_type=ticket_type,
                               num_tickets=num_tickets, date=date)
    return render_template("booking.html")

if __name__ == "__main__":
    app.run(debug=True)
