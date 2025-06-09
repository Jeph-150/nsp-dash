# nsp-dash

**Project Overview**
This project aims to build a simple, lightweight system to track and monitor family devices in real time. Inspired by Nokia NSP concepts, it focuses on device online status, location, and last seen timestamps — all managed through an easy-to-use web dashboard.

**MVP Features**
Python client script runs on each family device, sending periodic heartbeats with:
  Device ID
  Online status
  IP address
  Timestamp
Backend server (Flask or FastAPI) exposes REST API to receive device data and serve dashboard info.
Simple frontend dashboard displaying:
  List of devices
  Last seen timestamps
  Online/offline status (based on recent heartbeats)
  Optional map view with IP geolocation

**Tech Stack**
Backend: Python (Flask or FastAPI)
Database: SQLite or JSON file (for prototyping)
Client: Python script
Frontend: HTML/CSS/JS (vanilla or minimal React)

**How to Run**
Start backend server locally
Run client scripts on devices or simulated terminals
Open frontend dashboard to view device statuses

**Future Enhancements**
API authentication (JWT or API keys)
Cloud deployment (Heroku, Render, etc.)
Mobile app integration
Real GPS support and offline/online notifications

**Purpose**
Provide an easy-to-use, real-time family device monitoring tool that works end-to-end with minimal setup, perfect for personal use and resume projects.

