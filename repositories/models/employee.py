from dataclasses import dataclass
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
    last_visit: str

    #valitador made ez. When registering a new Employee these are the only necessary fields.
    def validate(self):
        self.name = require(self.name, "Name")
        self.last_name = require(self.last_name, "Last name")
        self.dob = require_date(self.dob, "Date of Birth")
        self.phone = require(self.phone, "Phone")
