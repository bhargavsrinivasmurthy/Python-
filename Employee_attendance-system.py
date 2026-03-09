from datetime import date

def mark_attendance():
    name = input("Enter employee name: ")
    today = str(date.today())

    with open("attendance.txt", "a") as file:
        file.write(name + " - " + today + "\n")

    print("Attendance Marked")


def view_attendance():
    with open("attendance.txt", "r") as file:
        print(file.read())


while True:
    print("1 Mark Attendance")
    print("2 View Attendance")
    print("3 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        mark_attendance()

    elif choice == "2":
        view_attendance()

    else:
        break