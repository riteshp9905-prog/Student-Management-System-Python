from database import connect
from auth import login

# ------------------ Grade ------------------

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"


# ------------------ Add Student ------------------

def add_student():

    conn = connect()
    cursor = conn.cursor()

    roll = input("Enter Roll No : ")

    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))

    if cursor.fetchone():
        print("\n❌ Roll Number Already Exists!")
        conn.close()
        return

    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    course = input("Enter Course : ")
    marks = float(input("Enter Marks : "))

    percentage = marks
    grade = calculate_grade(marks)

    cursor.execute("""
        INSERT INTO students
        VALUES(?,?,?,?,?,?,?)
    """, (
        roll,
        name,
        age,
        course,
        marks,
        percentage,
        grade
    ))

    conn.commit()
    conn.close()

    print("\n✅ Student Added Successfully!")


# ------------------ View Students ------------------

def view_students():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if not students:
        print("\nNo Student Records Found!")
    else:

        print("\n========== STUDENTS ==========\n")

        for student in students:

            print(f"Roll No    : {student[0]}")
            print(f"Name       : {student[1]}")
            print(f"Age        : {student[2]}")
            print(f"Course     : {student[3]}")
            print(f"Marks      : {student[4]}")
            print(f"Percentage : {student[5]}%")
            print(f"Grade      : {student[6]}")
            print("-----------------------------")

    conn.close()


    # ------------------ Search Student ------------------

def search_student():

    conn = connect()
    cursor = conn.cursor()

    roll = input("Enter Roll No to Search : ")

    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    student = cursor.fetchone()

    if student:

        print("\n========== STUDENT FOUND ==========\n")
        print(f"Roll No    : {student[0]}")
        print(f"Name       : {student[1]}")
        print(f"Age        : {student[2]}")
        print(f"Course     : {student[3]}")
        print(f"Marks      : {student[4]}")
        print(f"Percentage : {student[5]}%")
        print(f"Grade      : {student[6]}")

    else:
        print("\n❌ Student Not Found!")

    conn.close()


# ------------------ Update Student ------------------

def update_student():

    conn = connect()
    cursor = conn.cursor()

    roll = input("Enter Roll No to Update : ")

    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    student = cursor.fetchone()

    if not student:
        print("\n❌ Student Not Found!")
        conn.close()
        return

    print("\nStudent Found! Enter New Details\n")

    name = input("Enter New Name : ")
    age = int(input("Enter New Age : "))
    course = input("Enter New Course : ")
    marks = float(input("Enter New Marks : "))

    percentage = marks
    grade = calculate_grade(marks)

    cursor.execute("""
        UPDATE students
        SET name=?,
            age=?,
            course=?,
            marks=?,
            percentage=?,
            grade=?
        WHERE roll=?
    """, (
        name,
        age,
        course,
        marks,
        percentage,
        grade,
        roll
    ))

    conn.commit()
    conn.close()

    print("\n✅ Student Updated Successfully!")


# ------------------ Delete Student ------------------

def delete_student():

    conn = connect()
    cursor = conn.cursor()

    roll = input("Enter Roll No to Delete : ")

    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    student = cursor.fetchone()

    if not student:
        print("\n❌ Student Not Found!")
        conn.close()
        return

    cursor.execute("DELETE FROM students WHERE roll=?", (roll,))

    conn.commit()
    conn.close()

    print("\n✅ Student Deleted Successfully!")


    # ------------------ Topper Student ------------------

def topper_student():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM students
        ORDER BY marks DESC
        LIMIT 1
    """)

    student = cursor.fetchone()

    if student:
        print("\n========== TOPPER STUDENT ==========")
        print(f"Roll No    : {student[0]}")
        print(f"Name       : {student[1]}")
        print(f"Age        : {student[2]}")
        print(f"Course     : {student[3]}")
        print(f"Marks      : {student[4]}")
        print(f"Percentage : {student[5]}%")
        print(f"Grade      : {student[6]}")
    else:
        print("\nNo Student Records Found!")

    conn.close()


# ------------------ Total Students ------------------

def total_students():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]

    print(f"\n📊 Total Students : {count}")

    conn.close()


# ------------------ Main Program ------------------

if login():

    while True:

        print("\n========================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Topper Student")
        print("7. Total Students")
        print("8. Logout / Exit")

        choice = input("\nEnter Your Choice : ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            topper_student()

        elif choice == "7":
            total_students()

        elif choice == "8":
            print("\n👋 Logged Out Successfully!")
            break

        else:
            print("\n❌ Invalid Choice!")

else:
    print("Access Denied!")

    