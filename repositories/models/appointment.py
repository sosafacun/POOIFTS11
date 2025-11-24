from .status import Status
from .client import Client
from .employee import Employee
from services.validator import require, require_date
from dataclasses import dataclass

#omg, i didn't know dataclasses were a thing. They are so fucking goated to work with.
@dataclass
class Appointment():
    appointment_id: str
    client: Client
    employee: Employee
    date: str
    duration_in_mins: int
    status: Status

    #valitador made ez. When registering a new client these are the only necessary fields.
    def validate(self):
        self.client = require(self.client, "Client")
        self.employee = require(self.employee, "Employee")
        self.date = require_date(self.date, "Date")
        self.duration = require(self.duration_in_mins, "Duration (in minutes)")
        self.status = require(self.status, "Status")
    
    def card_header(self):
        return (f"Appointment {self.appointment_id}", self.date)

    def card_body(self):
        return [
            ("Client", f"{self.client.name} {self.client.last_name}"),
            ("Employee", f"{self.employee.name} {self.employee.last_name}"),
            ("Duration", f"{self.duration_in_mins} minutes"),
            ("Status", self.status.name if hasattr(self.status, "name") else self.status)
        ]

    def card_color(self):
        return "bright_magenta"
