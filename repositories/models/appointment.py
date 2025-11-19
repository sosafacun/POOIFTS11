from models.status import Status
from models.client import Client
from models.employee import Employee

#exception thrower to catch any non-filled fields
def _require(value: str, field_name: str):
    if not value or not value.strip():
        raise ValueError(f"{field_name} is required!")
    return value.strip()

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
        self.client = _require(self.client, "Client")
        self.employee = _require(self.client, "Employee")
        self.date = _require(self.date, "Date")
        self.duration = _require(self.duration_in_mins, "Duration (in minutes)")
        self.status = _require(self.status, "Status")
        