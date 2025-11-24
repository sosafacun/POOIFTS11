#Used to determine what the services will pull, depending on what it needs to be created.
from services.validator import require, require_date

CLIENT_SCHEMA = {
    "client_id": ("Client ID", require),
    "name": ("Name", require),
    "last_name": ("Last Name", require),
    "dob": ("Date of Birth (YYYY-MM-DD)", require_date),
    "phone": ("Phone", require)
}

EMPLOYEE_SCHEMA = {
    "employee_id": ("Employee ID", require),
    "name": ("Name", require),
    "last_name": ("Last Name", require),
    "dob": ("Date of Birth (YYYY-MM-DD)", require_date),
    "phone": ("Phone", require)
}

APPOINTMENT_SCHEMA = {
    "appointment_id": ("Appointment ID", require),
    "client": ("Client", require),
    "employee": ("Employee", require),
    "date": ("Date (YYYY-MM-DD)", require_date),
    "duration_in_mins": ("Duration (minutes)", require),
    "status": ("Status", require)
}
