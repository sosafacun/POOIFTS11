from dataclasses import dataclass, field
from datetime import datetime
from services.validators.validator import require, require_date

#omg, i didn't know dataclasses were a thing. They are so fucking goated to work with.
@dataclass
class Employee():
    employee_id: str
    name: str
    last_name: str
    dob: str
    phone: str
    is_bday_gift_active: bool

    age: int = field(init=False)

    def __post_init__(self):
        self.age = self._get_age()
    
    #valitador made ez. When registering a new Employee these are the only necessary fields.
    def validate(self):
        self.name = require(self.name, "Name")
        self.last_name = require(self.last_name, "Last name")
        self.dob = require_date(self.dob, "Date of Birth")
        self.phone = require(self.phone, "Phone")

    def _get_age(self):
        birthdate = datetime.strptime(self.dob, "%Y-%m-%d")
        today = datetime.today()
        return today.year - birthdate.year -((today.month, today.day) < (birthdate.month, birthdate.day)) #stackoverflow
    
    def card_header(self):
        return (f"{self.name} {self.last_name}", self.employee_id) 

    def card_body(self):
        return [
            ("Phone", self.phone),
            ("Age", f"{self.age} [dim]({self.dob})[/dim]"),
            ("Birthday Gift", "Active" if self.is_bday_gift_active else "Inactive")
        ]

    def card_color(self):
        return "bright_green"