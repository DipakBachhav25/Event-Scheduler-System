# 🗓️ Event Scheduler System

A simple RESTful event scheduler built using *Python, **Flask, and **JSON-based persistence*.

This system allows users to create, view, update, delete, and search events. Additionally, it supports email notifications before events start.

---

## 🧩 Features

- ✅ Create, Read, Update, Delete Events
- 🔍 Search Events by Title or Description
- 📨 Email Reminders (15 minutes before event)
- 💾 Data Persistence via JSON File
- 🧪 Unit Tests with pytest
- 📦 REST API Accessible via Postman or curl

---

## 🛠️ Requirements

- Python 3.x
- Flask
- APScheduler (for background tasks)

Install dependencies:

bash
pip install flask apscheduler


> Note: This project does not require any database — all data is stored in a local events.json file.

---

## 🚀 How to Run the Application

1. Clone the repository (replace with your actual GitHub link):

bash
git clone https://github.com/yourusername/event-scheduler.git
cd event-scheduler


2. Install dependencies:

bash
pip install flask apscheduler


3. Run the application:

bash
python event_app.py


The server will start at http://localhost:5000.

---

## 📝 Example Usage

### 🟢 Create an Event with Reminder

bash
curl -X POST http://localhost:5000/events -H "Content-Type: application/json" -d '{
  "title": "Team Meeting",
  "description": "Discuss project updates",
  "start_time": "2025-04-10T10:00:00",
  "end_time": "2025-04-10T11:00:00",
  "reminders": ["user@example.com"]
}'


*Output (example):*

json
{
  "id": 1,
  "title": "Team Meeting",
  "description": "Discuss project updates",
  "start_time": "2025-04-10T10:00:00",
  "end_time": "2025-04-10T11:00:00",
  "reminders": ["user@example.com"]
}


---

### 🔍 Search Events

bash
curl "http://localhost:5000/search?q=team"


*Output (example):*

json
[
  {
    "id": 1,
    "title": "Team Meeting",
    "description": "Discuss project updates",
    "start_time": "2025-04-10T10:00:00",
    "end_time": "2025-04-10T11:00:00",
    "reminders": ["user@example.com"]
  }
]


---

### 📋 List All Events

bash
curl http://localhost:5000/events


---

### 🆕 Update an Event

bash
curl -X PUT http://localhost:5000/events/1 -H "Content-Type: application/json" -d '{
  "title": "Updated Team Sync",
  "description": "Urgent discussion",
  "start_time": "2025-04-10T10:30:00",
  "end_time": "2025-04-10T11:30:00"
}'


---

### 🗑️ Delete an Event

bash
curl -X DELETE http://localhost:5000/events/1


---

## 📁 Files Structure


event-scheduler/
│
├── event_app.py            # Main Flask app
├── events.json             # Event storage
├── README.md               # This file
├── postman_collection.json # Import into Postman for testing
└── tests/
    └── testApp.py          # Pytest unit tests


---

## 🧪 Running Tests

Make sure you're in the root folder:

bash
cd D:\Event Scheduler System


Run tests:

bash
PYTHONPATH=. pytest tests/testApp.py -v


You should see all tests pass successfully.

---

## 📧 Email Notification Setup

To enable email reminders:

1. Set your email credentials in event_app.py:

python
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"

