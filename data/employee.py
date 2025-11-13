# employee.py
from datetime import datetime
from data.iPerson import Person

class Employee(Person):
    def __init__(
        self,
        name: str,
        dob: str,
        email: str,
        phone: str,
        employee_id: int,
        is_bday_gift_active: bool
    ):
        super().__init__(name, dob, email, phone, is_bday_gift_active)
        self.employee_id = employee_id

    #needed in order to check for unfilled fields.
    @staticmethod
    def required_fields():
        return ["name",
        "dob",
        "email",
        "phone",
        "employee_id",
        "is_bday_gift_active"]
    
    #obj -> dict converter
    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "dob": self.dob.strftime("%Y-%m-%d"),
            "email": self.email,
            "phone": self.phone,
            "is_bday_gift_active": self.is_bday_gift_active
        }
    
    #search support
    def matches(self, needle: str):
        needle = needle.lower()
        return (
            needle in self.name.lower()
            or needle in self.email.lower()
            or needle in self.phone.lower()
            or needle == str(self.employee_id)
        )
    
    #stringified output for display
    def __str__(self):
        return (
            f"[bold cyan]Employee ID:[/bold cyan] {self.employee_id}\n"
            f"Name: {self.name}\n"
            f"DOB: {self.dob}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}"
        )
