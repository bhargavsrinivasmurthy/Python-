class Ticket:

    def __init__(self, emp, issue):
        self.emp = emp
        self.issue = issue

    def save_ticket(self):
        with open("tickets.txt", "a") as file:
            file.write(self.emp + " : " + self.issue + "\n")


emp = input("Employee Name: ")
issue = input("Enter Issue: ")

t = Ticket(emp, issue)
t.save_ticket()

print("Ticket Created")