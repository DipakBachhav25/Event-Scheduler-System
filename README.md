# 🗓️ Event Scheduler System

A simple RESTful event scheduler built using **Python 3.x**, **Flask**, and **JSON-based persistence**.  
Users can create, view, update, delete events, and search by title or description. The system also supports **email notifications** as reminders for upcoming events.

---

## 🧩 Overview

This is a backend-only Flask application that allows users to manage events through a set of RESTful APIs. Events are stored in a JSON file for persistence, and background tasks are used to send email reminders before scheduled events.

---

## 📦 Features

- ✅ Create, Read, Update, and Delete (CRUD) operations for events.
- 🔍 Search events by title or description.
- 📨 Email reminders 15 minutes before event starts.
- 💾 Persistent storage using JSON files.
- 🧪 Unit tests with `pytest`.
- 🌐 REST API interface for integration with frontends or mobile apps.

---

## 🛠️ Requirements

Make sure you have these installed:

- Python 3.x
- Flask
- APScheduler (for scheduling background jobs)
- pytest (for running tests)

Install dependencies:

```bash
pip install flask apscheduler pytest

---

##📋 How to Run the Application
