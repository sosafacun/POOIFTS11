from datetime import datetime
from dataclasses import dataclass

#exception thrower to catch any non-filled fields
def _require(value: str, field_name: str):
    if not value or not value.strip():
        raise ValueError(f"{field_name} is required!")
    return value.strip()

#omg, i didn't know dataclasses were a thing. They are so fucking goated to work with.
@dataclass
class Client():
    client_id: str
    name: str
    last_name: str
    dob: str
    phone: str
    is_bday_gift_active: bool
    last_visit: str


    #valitador made ez. When registering a new client these are the only necessary fields.
    def validate(self):
        self.name = _require(self.name, "Name")
        self.last_name = _require(self.name, "Last name")
        self.dob = _require(self.name, "Date of Birth")
        self.phone = _require(self.name, "Phone")
