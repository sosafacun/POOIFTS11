from datetime import datetime
from data.iPerson import Person


class Employee(Person):
    def __init__(self,
    name: str,
    dob: str,
    email: str,
    phone: str,
    employee_id: int,
    is_bday_gift_active: bool):

        super().__init__(name, dob, email, phone, is_bday_gift_active)
        self.employee_id = employee_id

    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "dob": self.dob.strftime("%Y-%m-%d"),
            "email": self.email,
            "phone": self.phone,
            "is_bday_gift_active": self.is_bday_gift_active
        }
