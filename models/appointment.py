# appointment.py
from datetime import datetime
from models.status import Status

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