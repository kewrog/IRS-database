import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk  # For image handling

db_connection = None




# Function to connect to the database
def connect_to_database(username, password):
    global db_connection
    try:
        db_connection = mysql.connector.connect(
            host='localhost',
            database='irs',
            user=username,
            password=password
        )
        if db_connection.is_connected():
            messagebox.showinfo("Success", "Connected to the database successfully!")
            show_main_window()
    except Error as e:
        messagebox.showerror("Error", f"Failed to connect to the database: {e}")

# Function to Create a New Record in the Database
def create_record():
    try:
        table = simpledialog.askstring("Input", "Enter the table name:", parent=main_window)
        if not table:
            return

        cursor = db_connection.cursor()
        cursor.execute(f"DESCRIBE {table}")
        columns = cursor.fetchall()
        values = []

        for column in columns:
            column_name = column[0]
            value = simpledialog.askstring("Input", f"Enter value for {column_name}:", parent=main_window)

            values.append(value)

        placeholders = ", ".join(["%s"] * len(values))
        columns_list = ", ".join([col[0] for col in columns])
        query = f"INSERT INTO {table} ({columns_list}) VALUES ({placeholders})"
        cursor.execute(query, values)
        db_connection.commit()
        messagebox.showinfo("Success", "Record created successfully!")
    except Error as e:
        messagebox.showerror("Error", f"Failed to create record: {e}")

# Function to Read Records from the Database
def read_records():
    try:
        table = simpledialog.askstring("Input", "Enter the table name to read from:", parent=main_window)

        if not table:
            return

        cursor = db_connection.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        records = cursor.fetchall()

        # Display the records in a new window
        records_window = tk.Toplevel()
        records_window.title(f"Records from {table}")
        records_window.geometry("600x400")
        records_window.configure(bg="#ffffff")

        text_widget = tk.Text(records_window, font=("Helvetica", 12))
        text_widget.pack(expand=True, fill="both")

        for record in records:
            text_widget.insert(tk.END, str(record) + "\n")
    except Error as e:
        messagebox.showerror("Error", f"Failed to read records: {e}")

# Function to Update a Record in the Database
def update_record():
    try:
        table = simpledialog.askstring("Input", "Enter the table name to update:", parent=main_window)

        if not table:
            return

        set_clause = simpledialog.askstring("Input", "Enter SET clause (e.g., column1 = 'value'):", parent=main_window)

        condition = simpledialog.askstring("Input", "Enter WHERE condition (e.g., id = 1):", parent=main_window)

        if not set_clause or not condition:
            return

        cursor = db_connection.cursor()
        query = f"UPDATE {table} SET {set_clause} WHERE {condition}"
        cursor.execute(query)
        db_connection.commit()
        messagebox.showinfo("Success", "Record updated successfully!")
    except Error as e:
        messagebox.showerror("Error", f"Failed to update record: {e}")

# Function to Delete a Record from the Database
def delete_record():
    try:
        table = simpledialog.askstring("Input", "Enter the table name to delete from:", parent=main_window)

        if not table:
            return

        condition = simpledialog.askstring("Input", "Enter WHERE condition (e.g., id = 1):", parent=main_window)

        if not condition:
            return

        cursor = db_connection.cursor()
        query = f"DELETE FROM {table} WHERE {condition}"
        cursor.execute(query)
        db_connection.commit()
        messagebox.showinfo("Success", "Record deleted successfully!")
    except Error as e:
        messagebox.showerror("Error", f"Failed to delete record: {e}")


# Function to Show Table Names
def show_table_names():
    try:
        cursor = db_connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        if tables:
            output = "Available Tables:\n\n"
            for table in tables:
                output += f"{table[0]}\n"
        else:
            output = "No tables found in the database."

        # Display table names in a message box
        messagebox.showinfo("Table Names", output)
    except Error as e:
        messagebox.showerror("Error", f"Failed to retrieve table names: {e}")
        
# Placeholder function for running set operations
def run_set_operations():
    try:
        query = """SELECT Agent_Name AS Name
                    FROM agent
                    UNION
                    SELECT Employer_Name AS Name
                    FROM employer;""" 
        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        # Format results for display
        output = "Set Operation Results (UNION):\n\n"
        for row in results:
            output += f"{row[0]}\n"
        
        # Display results in a message box
        messagebox.showinfo("Set Operations Results", output)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    

# Placeholder function for running set membership queries
def run_set_membership_queries():
    try:
        query = """
                SELECT Agent_Name
                FROM agent
                WHERE Department IN (
                    SELECT Department
                    FROM employer
                );
            """  
        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        # Format and display results
        if results:
            output = "Set Membership Query Results:\n\n"
            for row in results:
                output += f"{row[0]}\n"
        else:
            output = "No matching results found for the set membership query."

        # Display results in a messagebox
        messagebox.showinfo("Set Membership Results", output)


    except Error as e:
        messagebox.showerror("Error", f"Failed to execute set membership query: {e}")
    #messagebox.showinfo("Info", "Set membership queries will be implemented here.")

# Placeholder function for running set comparison queries
def run_set_comparison_queries():
    try:
        # Display agents who are not listed as employers
        query = """
        SELECT Agent_Name
        FROM agent
        WHERE Agent_Name NOT IN (
            SELECT Employer_Name
            FROM employer
        );
        """ 
        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            output = "Set Comparison Query Results:\n\n"
            for row in results:
                output += f"{row[0]}\n"
        else:
            output = "No matching results found for the set comparison query."

        # Display results in a messagebox
        messagebox.showinfo("Set Comparison Results", output)

    except Error as e:
        messagebox.showerror("Error", f"Failed to execute set comparison query: {e}")

# Placeholder function for running WITH clause queries
def run_with_clause_queries():
    try:
        # Temporary table of active agents and filter by department
        query = """
        WITH ActiveAgents AS (
            SELECT Agent_ID, Agent_Name, Department
            FROM agent
            WHERE Department IS NOT NULL
        )
        SELECT Agent_Name, Department
        FROM ActiveAgents
        WHERE Department LIKE 'Finance%';
        """  

        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            output = "WITH Clause Query Results:\n\n"
            for row in results:
                output += f"Name: {row[0]}, Department: {row[1]}\n"
        else:
            output = "No matching results found for the WITH clause query."

        # Display results in a messagebox
        messagebox.showinfo("WITH Clause Results", output)

    except Error as e:
        messagebox.showerror("Error", f"Failed to execute WITH clause query: {e}")

# Placeholder function for running advanced aggregate queries
def run_advanced_aggregate_queries():
    try:
        # Count agents per department and display those with more than one agent

        query = """
        SELECT Department, COUNT(*) AS AgentCount
        FROM agent
        GROUP BY Department
        HAVING COUNT(*) > 1;
        """  
        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            output = "Advanced Aggregate Query Results:\n\n"
            for row in results:
                output += f"Department: {row[0]}, Agent Count: {row[1]}\n"
        else:
            output = "No matching results found for the advanced aggregate query."

        # Display results in a messagebox
        messagebox.showinfo("Advanced Aggregate Results", output)

    except Error as e:
        messagebox.showerror("Error", f"Failed to execute advanced aggregate query: {e}")

# Placeholder function for running OLAP queries
def run_olap_queries():
    try:
        # Assign rank to agents within each department based on their rank
        query = """
        SELECT Agent_Name, Department, RANK() OVER (PARTITION BY Department ORDER BY Agent_Rank) AS RankInDepartment
        FROM agent;
        """  
        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            output = "OLAP Query Results:\n\n"
            for row in results:
                output += f"Name: {row[0]}, Department: {row[1]}, Rank: {row[2]}\n"
        else:
            output = "No matching results found for the OLAP query."

        # Display results in a messagebox
        messagebox.showinfo("OLAP Query Results", output)

    except Error as e:
        messagebox.showerror("Error", f"Failed to execute OLAP query: {e}")

# Function to show the main application window
def show_main_window():
    global main_window
    if login_window:
        login_window.destroy()

    # Create the main window
    main_window = tk.Tk()
    main_window.title("IRS Database Management System")
    main_window.geometry("1200x900")
    main_window.configure(bg="#f0f2f5")

    # Create a canvas and a scrollbar
    canvas = tk.Canvas(main_window, bg="#e6f7ff")
    scrollbar = tk.Scrollbar(main_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#e6f7ff")

    # Configure the scrollable frame
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Header Frame with Title and Logo
    header_frame = tk.Frame(scrollable_frame, bg="#003366", height=100)
    header_frame.pack(fill="x")

    title_label = tk.Label(header_frame, text="IRS Database Management System", font=("Helvetica", 28, "bold"),
                           bg="#003366", fg="white", pady=20)
    title_label.pack()

    # Load and display images after creating main_window
    try:
        logo_image = Image.open("irs.jpeg")  # Correct path to your image
        logo_image = logo_image.resize((80, 80), Image.ANTIALIAS)
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(header_frame, image=logo_photo, bg="#003366")
        logo_label.image = logo_photo
        logo_label.pack(side="left", padx=20)
    except Exception as e:
        print(f"Error loading image: {e}")

    # Content Frame for Buttons and Operations
    content_frame = tk.Frame(scrollable_frame, bg="#e6f7ff", pady=20)
    content_frame.pack(fill="both", expand=True, padx=30, pady=30)

    # Add Section Labels for CRUD and Advanced Queries
    crud_label = tk.Label(content_frame, text="CRUD Operations", font=("Helvetica", 20, "bold"), bg="#e6f7ff", pady=10)
    crud_label.pack()

    # Load images for CRUD operations
    try:
        add_image = Image.open("add.png").resize((60, 60), Image.LANCZOS)
        add_photo = ImageTk.PhotoImage(add_image)
        read_image = Image.open("read.png").resize((60, 60), Image.LANCZOS)
        read_photo = ImageTk.PhotoImage(read_image)
        update_image = Image.open("update.png").resize((60, 60), Image.LANCZOS)
        update_photo = ImageTk.PhotoImage(update_image)
        delete_image = Image.open("delete.png").resize((60, 60), Image.LANCZOS)
        delete_photo = ImageTk.PhotoImage(delete_image)
    except Exception as e:
        print(f"Error loading CRUD images: {e}")

    # CRUD Buttons
    tk.Button(content_frame, text="Create Record", font=("Helvetica", 14), bg="#0073e6", fg="white",
              command=create_record).pack(pady=10, fill="x")
    tk.Button(content_frame, text="Read Records", font=("Helvetica", 14), bg="#0073e6", fg="white",
              command=read_records).pack(pady=10, fill="x")
    tk.Button(content_frame, text="Update Record", font=("Helvetica", 14), bg="#0073e6", fg="white",
              command=update_record).pack(pady=10, fill="x")
    tk.Button(content_frame, text="Delete Record", font=("Helvetica", 14), bg="#0073e6", fg="white",
              command=delete_record).pack(pady=10, fill="x")

    # Button to Show Table Names
    tk.Button(content_frame, text="Show Table Names", font=("Helvetica", 14), bg="#0073e6", fg="white",
              command=show_table_names).pack(pady=10, fill="x")

    # Divider Line
    divider = tk.Frame(content_frame, bg="#bfbfbf", height=2)
    divider.pack(fill="x", pady=20)

    # Advanced Queries Section
    advanced_label = tk.Label(content_frame, text="Advanced SQL Queries", font=("Helvetica", 20, "bold"), bg="#e6f7ff", pady=10)
    advanced_label.pack()

    # Load images for advanced query operations
    try:
        set_operations_image = Image.open("12.WEBP").resize((60, 60), Image.LANCZOS)
        set_operations_photo = ImageTk.PhotoImage(set_operations_image)
        membership_queries_image = Image.open("13.WEBP").resize((60, 60), Image.LANCZOS)
        membership_queries_photo = ImageTk.PhotoImage(membership_queries_image)
        comparison_queries_image = Image.open("14.WEBP").resize((60, 60), Image.LANCZOS)
        comparison_queries_photo = ImageTk.PhotoImage(comparison_queries_image)
        with_clause_image = Image.open("15.WEBP").resize((60, 60), Image.LANCZOS)
        with_clause_photo = ImageTk.PhotoImage(with_clause_image)
        advanced_aggregate_image = Image.open("16.WEBP").resize((60, 60), Image.LANCZOS)
        advanced_aggregate_photo = ImageTk.PhotoImage(advanced_aggregate_image)
        olap_image = Image.open("17.WEBP").resize((60, 60), Image.LANCZOS)
        olap_photo = ImageTk.PhotoImage(olap_image)
    except Exception as e:
        print(f"Error loading advanced query images: {e}")

    # Advanced Query Buttons with images
    tk.Button(content_frame, image=set_operations_photo, text=" Run Set Operations", font=("Helvetica", 14),
              compound="left", bg="#005bb5", fg="white", command=run_set_operations).pack(pady=10, fill="x")
    tk.Button(content_frame, image=membership_queries_photo, text=" Run Set Membership Queries", font=("Helvetica", 14),
              compound="left", bg="#005bb5", fg="white", command=run_set_membership_queries).pack(pady=10, fill="x")
    tk.Button(content_frame, image=comparison_queries_photo, text=" Run Set Comparison Queries", font=("Helvetica", 14),
              compound="left", bg="#005bb5", fg="white", command=run_set_comparison_queries).pack(pady=10, fill="x")
    tk.Button(content_frame, image=with_clause_photo, text=" Run WITH Clause Queries", font=("Helvetica", 14),
              compound="left", bg="#005bb5", fg="white", command=run_with_clause_queries).pack(pady=10, fill="x")
    tk.Button(content_frame, image=advanced_aggregate_photo, text=" Run Advanced Aggregate Queries", font=("Helvetica", 14),
              compound="left", bg="#005bb5", fg="white", command=run_advanced_aggregate_queries).pack(pady=10, fill="x")
    tk.Button(content_frame, image=olap_photo, text=" Run OLAP Queries", font=("Helvetica", 14),
              compound="left", bg="#005bb5", fg="white", command=run_olap_queries).pack(pady=10, fill="x")

    # Footer Frame with Exit Button
    footer_frame = tk.Frame(scrollable_frame, bg="#f0f2f5")
    footer_frame.pack(fill="x", pady=10)
    tk.Button(footer_frame, text="Exit", font=("Helvetica", 14), bg="#d9534f", fg="white", command=main_window.quit).pack(side="right", padx=20)

    # Run the main loop
    main_window.mainloop()



# Function to show the login window
def show_login_window():
    global login_window
    login_window = tk.Tk()
    login_window.title("Login to IRS Database")
    login_window.geometry("500x400")
    login_window.configure(bg="#f0f2f5")

    # Header Frame for the login window
    header_frame = tk.Frame(login_window, bg="#003366", height=100)
    header_frame.pack(fill="x")

    title_label = tk.Label(header_frame, text="IRS Database Login", font=("Helvetica", 22, "bold"),
                           bg="#003366", fg="white", pady=20)
    title_label.pack()

    # IRS Themed Image
    try:
        irs_image = Image.open("irs2.webp")  # Update with the correct path
        irs_image = irs_image.resize((350, 150), Image.LANCZOS)
        irs_photo = ImageTk.PhotoImage(irs_image)
        irs_label = tk.Label(login_window, image=irs_photo, bg="#f0f2f5")
        irs_label.image = irs_photo
        irs_label.pack(pady=10)
    except Exception as e:
        print(f"Error loading image: {e}")

    # Username and password labels and entry fields
    username_label = tk.Label(login_window, text="Username:", font=("Helvetica", 14), bg="#f0f2f5")
    username_label.pack(pady=5)
    username_entry = tk.Entry(login_window, font=("Helvetica", 14))
    username_entry.pack(pady=5)

    password_label = tk.Label(login_window, text="Password:", font=("Helvetica", 14), bg="#f0f2f5")
    password_label.pack(pady=5)
    password_entry = tk.Entry(login_window, font=("Helvetica", 14), show="*")
    password_entry.pack(pady=5)

    # Login button
    login_button = tk.Button(login_window, text="Login", font=("Helvetica", 14), bg="#0073e6", fg="white",
                             command=lambda: connect_to_database(username_entry.get(), password_entry.get()))
    login_button.pack(pady=20)

    # Run the login loop
    login_window.mainloop()

# Function to connect to the database
def connect_to_database(username, password):
    global db_connection
    try:
        db_connection = mysql.connector.connect(
            host='localhost',
            database='irs',
            user=username,
            password=password
        )
        if db_connection.is_connected():
            messagebox.showinfo("Success", "Connected to the database successfully!")
            show_main_window()
    except Error as e:
        messagebox.showerror("Error", f"Failed to connect to the database: {e}")

# Run the login window
show_login_window()

# Function to display query results in a new window
def show_query_results(results, title):
    results_window = tk.Toplevel()
    results_window.title(title)
    results_window.geometry("800x600")
    results_window.configure(bg="#ffffff")

    text_widget = tk.Text(results_window, font=("Helvetica", 12))
    text_widget.pack(expand=True, fill="both")

    for result in results:
        text_widget.insert(tk.END, str(result) + "\n")

# Utility function to close the database connection gracefully
def close_database_connection():
    global db_connection
    if db_connection and db_connection.is_connected():
        db_connection.close()
        db_connection = None
        print("Database connection closed.")

# Overriding the main window's close event to ensure the database connection is closed
def on_main_window_close():
    close_database_connection()
    main_window.destroy()

# Update the main window's close protocol to use the graceful close function
def show_main_window():
    global main_window
    if login_window:
        login_window.destroy()

    # Create the main window
    main_window = tk.Tk()
    main_window.title("IRS Database Management System")
    main_window.geometry("1400x900")
    main_window.configure(bg="#f0f2f5")

    # Set the protocol to handle window close
    main_window.protocol("WM_DELETE_WINDOW", on_main_window_close)

    # Header Frame with Title and Logo
    header_frame = tk.Frame(main_window, bg="#003366", height=100)
    header_frame.pack(fill="x")

    title_label = tk.Label(header_frame, text="IRS Database Management System", font=("Helvetica", 28, "bold"),
                           bg="#003366", fg="white", pady=20)
    title_label.pack()

    # Logo Image in the Header
    try:
        logo_image = Image.open("irs.jpeg")  # Update with the correct path
        logo_image = logo_image.resize((80, 80), Image.ANTIALIAS)
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(header_frame, image=logo_photo, bg="#003366")
        logo_label.image = logo_photo
        logo_label.pack(side="left", padx=20)
    except Exception as e:
        print(f"Error loading image: {e}")

    # Content Frame for Buttons and Operations
    content_frame = tk.Frame(main_window, bg="#e6f7ff", pady=20)
    content_frame.pack(fill="both", expand=True, padx=30, pady=30)

    # Section Label for CRUD Operations
    crud_label = tk.Label(content_frame, text="CRUD Operations", font=("Helvetica", 20, "bold"), bg="#e6f7ff", pady=10)
    crud_label.pack()

    # CRUD Buttons
    tk.Button(content_frame, text="Create Record", font=("Helvetica", 14), bg="#0073e6", fg="white",
              command=create_record).pack(pady=10, fill="x")
    tk.Button(content_frame, text="Read Records", font=("Helvetica", 14), bg="#0073e6", fg="white",
              command=read_records).pack(pady=10, fill="x")
    tk.Button(content_frame, text="Update Record", font=("Helvetica", 14), bg="#0073e6", fg="white",
              command=update_record).pack(pady=10, fill="x")
    tk.Button(content_frame, text="Delete Record", font=("Helvetica", 14), bg="#0073e6", fg="white",
              command=delete_record).pack(pady=10, fill="x")

    # Divider Line
    divider = tk.Frame(content_frame, bg="#bfbfbf", height=2)
    divider.pack(fill="x", pady=20)

    # Advanced Queries Section Label
    advanced_label = tk.Label(content_frame, text="Advanced SQL Queries", font=("Helvetica", 20, "bold"), bg="#e6f7ff", pady=10)
    advanced_label.pack()

    # Advanced Query Buttons
    tk.Button(content_frame, text="Run Set Operations", font=("Helvetica", 14), bg="#005bb5", fg="white",
              command=run_set_operations).pack(pady=10, fill="x")
    tk.Button(content_frame, text="Run Set Membership Queries", font=("Helvetica", 14), bg="#005bb5", fg="white",
              command=run_set_membership_queries).pack(pady=10, fill="x")
    tk.Button(content_frame, text="Run Set Comparison Queries", font=("Helvetica", 14), bg="#005bb5", fg="white",
              command=run_set_comparison_queries).pack(pady=10, fill="x")
    tk.Button(content_frame, text="Run WITH Clause Queries", font=("Helvetica", 14), bg="#005bb5", fg="white",
              command=run_with_clause_queries).pack(pady=10, fill="x")
    tk.Button(content_frame, text="Run Advanced Aggregate Queries", font=("Helvetica", 14), bg="#005bb5", fg="white",
              command=run_advanced_aggregate_queries).pack(pady=10, fill="x")
    tk.Button(content_frame, text="Run OLAP Queries", font=("Helvetica", 14), bg="#005bb5", fg="white",
              command=run_olap_queries).pack(pady=10, fill="x")

    # Footer Frame with Exit Button
    footer_frame = tk.Frame(main_window, bg="#f0f2f5")
    footer_frame.pack(fill="x", pady=10)
    tk.Button(footer_frame, text="Exit", font=("Helvetica", 14), bg="#d9534f", fg="white", command=on_main_window_close).pack(side="right", padx=20)

    # Run the main loop
    main_window.mainloop()
