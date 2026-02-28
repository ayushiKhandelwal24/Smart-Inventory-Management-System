===========================================================
      SMART INVENTORY MANAGEMENT SYSTEM - SETUP GUIDE
===========================================================

PROJECT DESCRIPTION:
A Flask-based web application to manage inventory across 
multiple shops with real-time tracking and stock alerts.

1. PREREQUISITES (Kya-kya chahiye):
----------------------------------
* Python 3.x installed on the system.
* MySQL Server & MySQL Workbench installed.
* Libraries: Flask, mysql-connector-python.

2. INSTALLATION STEPS:
----------------------
Step A: Install required Python libraries by running this command 
        in terminal:
        pip install flask mysql-connector-python

Step B: Open MySQL Workbench and run the following SQL files 
        (present in the project folder) to setup the database:
        1. users_schema.sql (Creates Admin Login)
        2. shops_setup.sql  (Creates Shop List)
        3. inventory_queries.sql (Creates Products Table)

Step C: Open 'app.py' and ensure the MySQL 'password' matches 
        your local MySQL root password.

3. HOW TO RUN THE PROJECT:
--------------------------
1. Double-click on the 'Run_Project.bat' file.
2. A black command window will open. Wait for it to say:
   "Running on http://127.0.0.1:5000"
3. Open your Web Browser (Chrome/Edge).
4. Type http://127.0.0.1:5000 in the address bar and press Enter.

4. DEFAULT LOGIN CREDENTIALS:
-----------------------------
* Username: admin
* Password: password123

===========================================================
Developed by: Ayushi
===========================================================