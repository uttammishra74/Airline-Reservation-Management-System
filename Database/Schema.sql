CREATE DATABASE airline_db;
USE airline_db;

CREATE TABLE admins (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE passengers (
    passenger_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    password VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE airports (
    airport_id INT AUTO_INCREMENT PRIMARY KEY,
    airport_code CHAR(3) UNIQUE,
    airport_name VARCHAR(100),
    city VARCHAR(50),
    country VARCHAR(50)
);

CREATE TABLE flights (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(10) UNIQUE,
    airline_name VARCHAR(50),
    source_airport ,VARCHAR(10)
    destination_airport INT,
    departure_time DATETIME,
    arrival_time DATETIME,
    economy_seats INT,
    business_seats INT,
    economy_price DECIMAL(10,2),
    business_price DECIMAL(10,2),
    status ENUM('Scheduled','Delayed','Cancelled') DEFAULT 'Scheduled',
    FOREIGN KEY (source_airport) REFERENCES airports(airport_id),
    FOREIGN KEY (destination_airport) REFERENCES airports(airport_id)
);

CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    passenger_id INT,
    flight_id INT,
    seat_class ENUM('Economy','Business'),
    seats_booked INT DEFAULT 1,
    total_amount DECIMAL(10,2),
    booking_status ENUM('Confirmed','Cancelled') DEFAULT 'Confirmed',
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id),
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);

CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    payment_method ENUM('Card','UPI','NetBanking'),
    payment_status ENUM('Pending','Success','Failed') DEFAULT 'Success',
    amount DECIMAL(10,2),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);
