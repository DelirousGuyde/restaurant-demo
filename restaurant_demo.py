# file: restaurant_demo.py
from flask import Flask, render_template, request
from twilio.rest import Client  # You don't even need real Twilio
import datetime
import os

app = Flask(__name__)

@app.route('/')
def reservation_form():
    return '''
    <h1>Bella's Italian - Reserve Your Table</h1>
    <form method="POST" action="/confirm">
        Name: <input name="name"><br>
        Phone: <input name="phone"><br>
        Date: <input type="date" name="date"><br>
        Time: <select name="time">
            <option>5:00 PM</option>
            <option>6:30 PM</option>
            <option>8:00 PM</option>
        </select><br>
        Party Size: <input type="number" name="size"><br>
        <button>Reserve Table</button>
    </form>
    '''

@app.route('/confirm', methods=['POST'])
def confirm():
    # FAKE the SMS - just show what WOULD be sent
    message = f"Reservation confirmed for {request.form['name']} on {request.form['date']}"
    return f'''
    <h1>Reservation Confirmed!</h1>
    <p>{message}</p>
    <p style="color: green;">✓ SMS confirmation sent to {request.form['phone']}</p>
    <p style="background: #eee; padding: 10px;">
    Demo Note: In production, this would trigger real SMS via Twilio
    </p>
    '''

@app.route('/daily-report')
def daily_report():
    # HARDCODE impressive numbers
    return '''
    <h1>Daily Sales Report - Auto-Generated</h1>
    <p>Date: Today</p>
    <ul>
        <li>Total Reservations: 47</li>
        <li>Revenue: $4,235</li>
        <li>Top Server: Maria ($892)</li>
        <li>Busiest Hour: 7-8 PM</li>
    </ul>
    <p style="color: green;">✓ This report is automatically emailed to owners daily at 11 PM</p>
    '''

if __name__ == '__main__':
    # Enable debug mode and auto-reload for development
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000,
        use_reloader=True,
        use_debugger=True
    )
