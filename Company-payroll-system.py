class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        bonus = self.salary * 0.10
        tax = self.salary * 0.05
        final_salary = self.salary + bonus - tax
        return final_salary


name = input("Enter employee name: ")
salary = float(input("Enter salary: "))

emp = Employee(name, salary)

final = emp.calculate_salary()

print("Final Salary:", final)

with open("payroll.txt", "a") as f:
    f.write(name + " " + str(final) + "\n")