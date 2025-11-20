from models.status import Status
from models.client import Client
from models.employee import Employee
from services.validators.validator import require, require_date

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
        