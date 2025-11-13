# appointment.py
from datetime import datetime
from data.status import Status

class Appointment:
    def __init__(
        self,
        appointment_id: int,
        client_id: int,
        employee_id: int,
        scheduled_date: str,
        duration: int,
        status: str,
        is_confirmed: bool
    ):
        self.appointment_id = appointment_id
        self.client_id = client_id
        self.employee_id = employee_id
        self.scheduled_date = datetime.strptime(scheduled_date, "%Y-%m-%d").date()
        self.duration = duration
        self.status = Status(status)
        self.is_confirmed = is_confirmed
    
    #needed in order to check for unfilled fields.
    @staticmethod
    def required_fields():
        return [
            "appointment_id",
            "client_id",
            "employee_id",
            "scheduled_date",
            "duration",
            "status",
            "is_confirmed"
        ]
    
    #obj -> dict converter
    def to_dict(self):
        return {
            "appointment_id": self.appointment_id,
            "client_id": self.client_id,
            "employee_id": self.employee_id,
            "scheduled_date": self.scheduled_date.strftime("%Y-%m-%d"),
            "duration": self.duration,
            "status": self.status.value,
            "is_confirmed": self.is_confirmed
        }
    
    #search support
    def matches(self, needle: str):
        needle = needle.lower()
        return (
            needle == str(self.appointment_id)
            or needle == str(self.client_id)
            or needle == str(self.employee_id)
            or needle in self.status.value.lower()
        )
    
    #stringified output for display
    def __str__(self):
        return (
            f"[bold cyan]Appointment ID:[/bold cyan] {self.appointment_id}\n"
            f"Client ID: {self.client_id}\n"
            f"Employee ID: {self.employee_id}\n"
            f"Date: {self.scheduled_date}\n"
            f"Duration: {self.duration} min\n"
            f"Status: {self.status.value}\n"
            f"Confirmed: {self.is_confirmed}"
        )
