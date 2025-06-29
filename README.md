# 🗓️ Event Scheduler System

A simple backend application built using **Flask** that allows users to manage events with the ability to create, view, update, delete, search events, and receive email notifications before event starts.

---

## 🧩 Features

✅ Create Events with title, description, start time, end time  
✅ List all scheduled events (sorted by start time)  
✅ Update existing event details  
✅ Delete events  
✅ Search events by title or description  
✅ Email reminders before events begin  
✅ Data persistence using JSON file  
✅ Unit tests with `pytest`  
✅ Postman collection included for API testing  

---

## 📦 Requirements

### Python Packages:
Make sure these packages are installed:

```bash
pip install flask apscheduler pytest
```

---

## 🚀 How to Run the Application

1. Clone or navigate to your project directory:

```bash
cd D:\Event Scheduler System
```

2. Install dependencies:

```bash
pip install flask apscheduler pytest
```

3. Start the Flask server:

```bash
python event_app.py
```
The server will be running at: http://localhost:5000

---

## 🧪 Running Tests
To ensure everything works correctly, run the unit tests:

```bash
PYTHONPATH=. pytest tests/testApp.py -v
```

**Note:** Make sure you're in the root directory of your project if above command not working use below command

```bash
$env:PYTHONPATH = "." ; pytest tests/testApp.py -v
```

---

## 📨 Email Notifications Setup

If you're using Gmail for sending email reminders:

1. Enable **2-Step Verification** on your Google account.
2. Generate an **App Password** from **Google App Passwords**.
3. Update the email configuration in **event_app.py**:

```python
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
```

---

## 📎 Postman Testing

Import the provided **postman_collection.json** into Postman to test the API endpoints:
* Create Event
* List Events
* Search Events
* Update Event
* Delete Event

---

## ✅ Summary
This system provides a complete RESTful API for managing events with advanced features like searching and email notifications. It's ideal for personal use or as a foundation for building more complex scheduling applications.
