import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("student_db.sqlite")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dept TEXT,
    marks INTEGER
)
''')

# Functions
def add_student():
    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    marks = int(input("Enter Marks: "))
    cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?)", (roll_no, name, dept, marks))
    conn.commit()
    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    print("\n--- Student Records ---")
    if rows:
        for row in rows:
            print(row)
    else:
        print("No records found.")

def update_marks():
    roll_no = int(input("Enter Roll No to Update: "))
    marks = int(input("Enter New Marks: "))
    cursor.execute("UPDATE student SET marks=? WHERE roll_no=?", (marks, roll_no))
    conn.commit()
    print("Marks updated!")

def delete_student():
    roll_no = int(input("Enter Roll No to Delete: "))
    cursor.execute("DELETE FROM student WHERE roll_no=?", (roll_no,))
    conn.commit()
    print("Student deleted!")

def search_student():
    term = input("Enter Roll No or Name to search: ")
    if term.isdigit():
        cursor.execute("SELECT * FROM student WHERE roll_no=?", (int(term),))
    else:
        cursor.execute("SELECT * FROM student WHERE name LIKE ?", (f"%{term}%",))
    rows = cursor.fetchall()
    print("\n--- Search Results ---")
    if rows:
        for row in rows:
            print(row)
    else:
        print("No matching records found.")

# Menu Loop
def main_menu():
    while True:
        print("\n===== Student Database Menu =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_marks()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("Exiting program... ")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    print("Program started ")
    main_menu()
    conn.close()

