class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(self.emp_id, self.name, self.department, self.salary)


def add_employee():
    emp_id = input("Enter ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = input("Enter Salary: ")

    with open("employees.txt", "a") as file:
        file.write(emp_id + "," + name + "," + dept + "," + salary + "\n")

    print("Employee Added Successfully")


def view_employees():
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                emp = line.strip().split(",")
                e = Employee(emp[0], emp[1], emp[2], emp[3])
                e.display()
    except FileNotFoundError:
        print("No employee records found")


while True:
    print("\n1 Add Employee")
    print("2 View Employees")
    print("3 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        break