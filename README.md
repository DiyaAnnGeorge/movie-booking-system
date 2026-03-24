# 🎬 BookMyTicket — Movie Booking System

A Python-based command-line movie booking application with MySQL database
integration, built as a student project.

## 📌 Features

### 👤 User
- Sign up / Log in
- Search movies by language or genre
- Book, cancel and update tickets
- Visual seat selection using matplotlib
- Leave feedback on exit

### 🔐 Admin
- Secure admin login
- Add, delete and update movies
- Manage show timings and screens
- View all bookings and feedbacks

## 🛠️ Tech Stack
- **Language:** Python
- **Database:** MySQL
- **Libraries:** mysql-connector, tabulate, matplotlib, PIL, csv

## ⚙️ Setup Instructions

1. Clone the repository
   git clone https://github.com/DiyaAnnGeorge/movie-booking-system.git

2. Install required libraries
   pip install mysql-connector-python tabulate matplotlib pillow

3. Set up MySQL database and import the provided SQL file

4. Update your database credentials in Project.py or set environment variables:
   DB_HOST=localhost
   DB_USER=root
   DB_PASS=your_password
   DB_NAME=project

5. Run the project
   python Project.py

## 📂 Project Structure
- Project.py — Main application file
- user.csv — User credentials
- feedback.csv — User feedbacks
- movies.jpg — Movie poster display
- welcm.txt / about us.txt — Text content files

## 👩‍💻 Developer
Diya Ann George
B.Tech CSE | VIT Vellore (2024–2028)
github.com/DiyaAnnGeorge
