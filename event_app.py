# event_app.py

from flask import Flask, request, jsonify
import json
import os
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from threading import Thread
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
DATA_FILE = 'events.json'

# Email configuration - Update these values
EMAIL_ADDRESS = "enter_your_email"
EMAIL_PASSWORD = "enter_app_password"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587

# Scheduler instance
scheduler = BackgroundScheduler()
scheduler.start()


def load_events():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_events(events):
    with open(DATA_FILE, 'w') as f:
        json.dump(events, f, indent=4)


def get_next_id(events):
    return max((e['id'] for e in events), default=0) + 1


def send_email(subject, body, recipient):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email: {e}")


def schedule_event_reminders(event):
    reminder_time = datetime.fromisoformat(event['start_time']) - timedelta(minutes=15)
    if 'reminders' in event:
        for email in event['reminders']:
            scheduler.add_job(
                send_email,
                'date',
                run_date=reminder_time,
                args=[f"Reminder: {event['title']}", event['description'], email]
            )
        print(f"Scheduled reminder for '{event['title']}' at {reminder_time}")


@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    reminders = data.get('reminders', [])  # Optional list of emails

    if not all([title, description, start_time, end_time]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        start = datetime.fromisoformat(start_time)
        end = datetime.fromisoformat(end_time)

        # Check if start time is in the past
        if start < datetime.now(start.tzinfo):
            return jsonify({"error": "Start time cannot be in the past"}), 400

        # Check if start time must be before end time
        if start >= end:
            return jsonify({"error": "Start time must be before end time"}), 400


    except ValueError:
        return jsonify({"error": "Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM)"}), 400

    events = load_events()
    new_event = {
        "id": get_next_id(events),
        "title": title,
        "description": description,
        "start_time": start_time,
        "end_time": end_time,
        "reminders": reminders
    }
    events.append(new_event)
    save_events(events)

    schedule_event_reminders(new_event)

    return jsonify(new_event), 201


@app.route('/events', methods=['GET'])
def list_events():
    events = load_events()
    return jsonify(sorted(events, key=lambda x: x['start_time']))


@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    events = load_events()
    found = False
    updated_events = []

    for event in events:
        if event['id'] == event_id:
            event['title'] = data.get('title', event['title'])
            event['description'] = data.get('description', event['description'])
            event['start_time'] = data.get('start_time', event['start_time'])
            event['end_time'] = data.get('end_time', event['end_time'])
            event['reminders'] = data.get('reminders', event.get('reminders', []))
            updated_events.append(event)
            found = True
        else:
            updated_events.append(event)

    if not found:
        return jsonify({"error": "Event not found"}), 404

    save_events(updated_events)
    return jsonify({"message": "Event updated"})


@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    events = load_events()
    updated_events = [e for e in events if e['id'] != event_id]
    if len(updated_events) == len(events):
        return jsonify({"error": "Event not found"}), 404
    save_events(updated_events)
    return jsonify({"message": "Event deleted"})


@app.route('/search', methods=['GET'])
def search_events():
    query = request.args.get('q', '').strip().lower()
    if not query:
        return jsonify([])

    events = load_events()
    filtered = [
        event for event in events
        if query in event['title'].lower() or query in event['description'].lower()
    ]
    return jsonify(sorted(filtered, key=lambda x: x['start_time']))


if __name__ == '__main__':
    app.run(debug=True)
