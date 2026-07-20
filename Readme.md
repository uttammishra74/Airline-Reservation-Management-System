# ✈️ Airline Reservation Management System

A terminal-based Airline Reservation Management System built with **Python** and **MySQL**. This project simulates a real-world airline booking system where passengers can search for flights, reserve seats, cancel bookings, and manage their profiles, while administrators can manage flights, airports, schedules, and generate reports.

---

## 📌 Project Overview

The Airline Reservation Management System is designed to demonstrate how a real backend application works using Python and MySQL. It focuses on database design, SQL operations, business logic, and clean project architecture.

This project follows a modular approach, making it easy to maintain, extend, and integrate with frameworks like FastAPI or Django in the future.

---

## 🎯 Objectives

* Learn how Python communicates with MySQL
* Build a real-world database project
* Practice SQL queries and relationships
* Implement CRUD operations
* Understand backend application flow
* Improve problem-solving and project organization

---

# 🚀 Features

## 👤 Passenger Module

* Register a new account
* Secure login
* Update profile
* Search available flights
* View flight details
* Book tickets
* Choose seat class
* View booking history
* Cancel bookings

---

## 🛠️ Admin Module

* Admin login
* Add airports
* Add airlines
* Add flights
* Update flight schedules
* Update ticket prices
* Delete flights
* View all bookings
* View passenger information
* Generate reports
* View revenue statistics

---

# 🧱 Tech Stack

| Technology             | Purpose               |
| ---------------------- | --------------------- |
| Python                 | Backend Logic         |
| MySQL                  | Database              |
| mysql-connector-python | Database Connectivity |
| SQL                    | Data Manipulation     |
| Git                    | Version Control       |
| GitHub                 | Project Hosting       |

---

# 📂 Project Structure

```text
Airline-Reservation-System/
│
├── database/
│   ├── schema.sql
│   ├── sample_data.sql
│   └── queries.sql
│
├── config/
│   └── db_config.py
│
├── models/
│   ├── passenger.py
│   ├── flight.py
│   ├── booking.py
│   ├── airport.py
│   ├── payment.py
│   └── admin.py
│
├── services/
│   ├── auth_service.py
│   ├── booking_service.py
│   ├── flight_service.py
│   ├── payment_service.py
│   └── report_service.py
│
├── utils/
│   ├── validation.py
│   ├── helpers.py
│   └── menu.py
│
├── screenshots/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🗄️ Database Design

## Tables

### Passengers

Stores passenger information.

### Admins

Stores administrator credentials.

### Airports

Stores airport information.

### Flights

Stores flight schedules.

### Bookings

Stores ticket reservations.

### Payments

Stores payment records.

---

# 🔗 Database Relationships

```text
Passenger
    │
    │ 1
    │
    ▼
Bookings
    ▲
    │
    │ Many
Flight
    │
    │
    ▼
Airport (Source)

Flight
    │
    ▼
Airport (Destination)

Booking
    │
    ▼
Payment
```

---

# 🛫 Passenger Workflow

```text
Register
      │
      ▼
Login
      │
      ▼
Search Flights
      │
      ▼
Select Flight
      │
      ▼
Choose Seat Class
      │
      ▼
Confirm Booking
      │
      ▼
Payment
      │
      ▼
Ticket Generated
```

---

# 👨‍💼 Admin Workflow

```text
Admin Login
      │
      ▼
Manage Airports
      │
      ▼
Manage Flights
      │
      ▼
Manage Ticket Prices
      │
      ▼
View Bookings
      │
      ▼
Generate Reports
```

---

# 📚 SQL Concepts Used

* CREATE DATABASE
* CREATE TABLE
* PRIMARY KEY
* FOREIGN KEY
* AUTO_INCREMENT
* INSERT
* UPDATE
* DELETE
* SELECT
* WHERE
* ORDER BY
* GROUP BY
* HAVING
* LIMIT
* INNER JOIN
* LEFT JOIN
* Aggregate Functions
* Transactions
* Constraints

---

# 🐍 Python Concepts Used

* Object-Oriented Programming (OOP)
* Classes & Objects
* Functions
* Exception Handling
* File Structure
* Modules
* Database Connectivity
* Loops
* Conditional Statements
* Input Validation

---

# 📊 Reports

The system can generate reports such as:

* Total Flights
* Total Bookings
* Revenue Report
* Most Popular Route
* Passenger History
* Flight Occupancy
* Available Seats
* Cancelled Bookings

---

# ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/uttammishra74/airline-reservation-system.git
```

### Navigate to Project

```bash
cd airline-reservation-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

Create a MySQL database.

```sql
CREATE DATABASE airline_db;
```

Import the SQL schema and sample data.

Update your database credentials in:

```text
config/db_config.py
```

Run the project.

```bash
python main.py
```

---

# 📷 Screenshots

Add screenshots here after completing the project.

* Main Menu
* Passenger Login
* Flight Search
* Booking Confirmation
* Booking History
* Admin Dashboard
* Revenue Report

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

* Relational Database Design
* SQL Query Writing
* Python-MySQL Integration
* Backend Development
* Business Logic Implementation
* Project Architecture
* Error Handling
* Version Control with Git

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is open-source and available under the MIT License.

---

# 👨‍💻 Author

**Ayush Mishra**

Aspiring AI Engineer | Python Developer | SQL Enthusiast

Currently building real-world backend projects to strengthen software engineering and AI development skills.

---

⭐ If you found this project helpful, consider giving it a star!
