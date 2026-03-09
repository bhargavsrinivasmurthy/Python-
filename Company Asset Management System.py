class Asset:

    def __init__(self, emp, asset):
        self.emp = emp
        self.asset = asset

    def save(self):
        with open("assets.txt", "a") as f:
            f.write(self.emp + "," + self.asset + "\n")


emp = input("Employee Name: ")
asset = input("Asset Assigned: ")

a = Asset(emp, asset)
a.save()

print("Asset Assigned Successfully")