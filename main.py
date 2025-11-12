from data.client import Client
from data.employee import Employee

def main():
    clients = [
        Client("Alice Johnson", "1990-05-12", "alice.johnson@email.com", "555-0142", 101, False, "2025-11-01"),
        Client("Brian Smith", "1985-09-23", "brian.smith@email.com", "555-0199", 102, False, "2025-10-18"),
        Client("Cynthia Lee", "1998-02-17", "cynthia.lee@email.com", "555-0283", 103, False, "2025-09-30"),
        Client("David Brown", "1977-11-02", "david.brown@email.com", "555-0355", 104, True, "2025-08-25"),
        Client("Elena Davis", "2001-08-30", "elena.davis@email.com", "555-0411", 105, False, "2025-11-05")
    ]

    employees = [
        Employee("Frank Wilson", "1982-03-14", "frank.wilson@company.com", "555-0510", 201, False),
        Employee("Grace Miller", "1995-12-08", "grace.miller@company.com", "555-0602", 202, False),
        Employee("Henry Clark", "1979-07-25", "henry.clark@company.com", "555-0714", 203, False),
        Employee("Isabella Moore", "1992-10-19", "isabella.moore@company.com", "555-0833", 204, False),
        Employee("Jack Taylor", "1988-01-05", "jack.taylor@company.com", "555-0976", 205, False)
    ]

    for c in clients:
        print(c)
    for e in employees:
        print(e)

if __name__ == "__main__":
    main()
