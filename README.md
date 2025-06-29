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
