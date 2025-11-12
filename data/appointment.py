from datetime import datetime
from data.client import Client
from data.employee import Employee
from data.status import Status

class Appointment:
    def __init__(self,
                 appointment_id: int,
                 scheduled_date: str,
                 client: Client,
                 employee: Employee,
                 duration: int,
                 status: Status,
                 is_confirmed: bool):

        self.appointment_id = appointment_id

        self.scheduled_date = datetime.strptime(scheduled_date, "%Y-%m-%d")
        self.client = client
        self.employee = employee
        self.duration = duration
        self.status = status
        self.is_confirmed = is_confirmed

    def to_dict(self):
        return {
            "appointment_id": self.appointment_id,
            "scheduled_date": self.scheduled_date.strftime("%Y-%m-%d"),
            "client_id": self.client.client_id,
            "client_name": self.client.name,
            "employee_id": self.employee.employee_id,
            "employee_name": self.employee.name,
            "duration": self.duration,
            "status": self.status.value,
            "is_confirmed": self.is_confirmed
        }

