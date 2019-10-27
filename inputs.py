def setup():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    employid = int(input("Enter your employee ID: "))
    hourly = float(input("Enter your hourly wage: "))
    overtime = float(input("Enter your overtime wage: "))
    return fname, lname, employid, hourly, overtime
