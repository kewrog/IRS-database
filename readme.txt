


IRS Database Management System


Project Overview:

The IRS Database Management System is a user-friendly desktop application developed in Python using tkinter for the GUI and MySQL for database operations. The application allows for comprehensive database management, including CRUD operations and advanced SQL queries, enhancing the overall database interaction experience.


Setup and Running the Application
File Preparation:

Create a new folder named dbo or unzip the provided file exactly as it is.
Ensure that all images are correctly placed in the appropriate folders as submitted. Double-check that the image paths in your code align with the folder structure.
Running the Python File:

Open a terminal and navigate to the dbo folder.
Run the Python script in your local environment using:
bash
Copy code
python your_script_name.py
Once executed, the GUI of the IRS Database Management System will appear on your screen. n your system.


Features
1. User Authentication
Secure login system that connects to the MySQL database using provided credentials.
2. CRUD Operations
Create Record: Add new records to the specified table in the database.
Read Records: View all records from a specified table in a scrollable text widget.
Update Record: Modify existing records based on user-defined conditions.
Delete Record: Remove records from the database based on user input.
3. Advanced SQL Queries
Set Operations: Demonstrates the use of UNION to combine results from different tables.
Set Membership Queries: Checks for membership conditions within the database.
Set Comparison Queries: Performs comparisons to filter records not present in another table.
WITH Clause Queries: Utilizes the WITH clause to simplify complex subqueries.
Advanced Aggregate Queries: Uses aggregate functions to generate summary data, such as counting records per department.
OLAP Queries: Implements RANK() to rank records within partitions, demonstrating OLAP capabilities.
Setup Instructions
1. Prerequisites
Ensure you have Python 3.x installed.
Install the required libraries:
bash
pip install mysql-connector-python
pip install Pillow
2. Database Setup
Install and set up MySQL on your local machine.
Create a database named irs and set up tables as needed for your application.
Update the database connection details in the connect_to_database function (host, database, user, and password).
3. Running the Application
Open a terminal and navigate to the project directory.
Run the script using:
bash
Copy code
python your_script_name.py
Enter your database credentials in the login window to connect.
Usage Guide
Login Window:

Enter your username and password to connect to the IRS database.
If successful, the main application window will open.
Main Window:

CRUD Operations:
Use the provided buttons to create, read, update, or delete records.
Advanced Queries:
Run predefined SQL queries by clicking the corresponding buttons to see results.




instructions for Using the Create and Delete Features
Create Menu: When you select the Create option, you will first be prompted to choose the table name where you want to add a new record.

To view the available table names, use the "Show Table Names" button. This will help you understand which tables are present in the database.
Reading Tables: Before creating or deleting records, it is recommended to read the table data using the Read button. This way, you can familiarize yourself with the existing data structure and ensure any alterations you make are appropriate.

Deleting Records: When deleting data from the database, make sure to use the correct format for the condition. For example, if you want to delete a record from the taxpayer table, specify the condition as follows:

Example: "taxpayer_id = 23"



Error Handling:

The application provides clear error messages for any issues that arise, such as failed database connections or invalid input.
File Structure
main.py: The main Python script containing the GUI and database logic.
README.md: This file, which provides setup instructions and usage details.
Images Folder: Contains images used in the application (e.g., logos, icons).
Dependencies
mysql-connector-python: Used for connecting and interacting with the MySQL database.
Pillow: For handling and displaying images in the GUI.
tkinter: The Python GUI toolkit used to create the application interface.
Error Handling and Security
Robust error handling to manage failed connections and invalid operations.
Secure login system to ensure database access is restricted to authorized users.
Contribution
If this is a group project, specify each member's contribution percentage in a separate file named Contribution.txt.
Future Enhancements
Add more complex queries and analytics features.
Implement a more secure authentication system.
Integrate data visualization for better insights.



