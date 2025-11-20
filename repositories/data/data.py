#dummy data for testing without the .csv
from ..models.client import Client
from ..models.employee import Employee
from ..models.appointment import Appointment
from ..models.status import Status

from typing import List

client_list: List[Client] = []
employee_list: List[Employee] = []
appointment_list: List[Appointment] = []

def create_client_data():
    '''client_id: str #01-XXXXXXXX
    name: str
    last_name: str
    dob: str #YYYY-MM-DD
    phone: str #xxxxxxxxxx
    is_bday_gift_active: bool 
    last_visit: str #YYYY-MM-DD'''

    c01 = Client("01-10029384", "Lucia", "Gomez", "1995-03-14", "1123456789", False, "2025-10-12")
    c02 = Client("01-20394856", "Martín", "Romero", "1988-07-02", "1132984455", False, "2025-09-28")
    c03 = Client("01-30948322", "Sofia", "Martinez", "2001-11-21", "1145672233", False, "")
    c04 = Client("01-40018293", "Diego", "Fernandez", "1992-01-05", "1149823344", False, "")
    c05 = Client("01-50194827", "Valentina", "Lopez", "1999-06-17", "1156677889", False, "2025-10-31")
    c06 = Client("01-60238941", "Tomas", "Cruz", "1985-09-30", "1162233445", False, "2025-07-14")
    c07 = Client("01-70398421", "Camila", "Silva", "1997-02-28", "1174455667", False, "")
    c08 = Client("01-80451233", "Sebastian", "Rios", "2000-12-09", "1183344552", False, "2025-09-02")
    c09 = Client("01-90567312", "Florencia", "Castro", "1993-04-25", "1198899001", False, "2025-10-18")
    c10 = Client("01-99871244", "Agustin", "Herrera", "1989-05-13", "1104456678", False, "2025-08-22")

    client_list.extend([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10])

def create_employee_data():
    '''class Employee():
    employee_id: str #02-XXXXXXXX
    name: str
    last_name: str
    dob: str #YYYY-MM-DD
    phone: str  #xxxxxxxxxx
    is_bday_gift_active: bool'''

    e01 = Employee("02-19283746", "Carolina", "Suarez", "1987-04-19", "1156672211", False)
    e02 = Employee("02-28374655", "Javier", "Molina", "1991-09-12", "1145523388", False)
    e03 = Employee("02-37465589", "Paula", "Benitez", "1998-03-03", "1133345566", False)
    e04 = Employee("02-46558921", "Lucas", "Paredes", "1985-12-15", "1122981144", False)
    e05 = Employee("02-55679234", "Maria", "Cabrera", "1994-02-27", "1177884466", False)
    e06 = Employee("02-62347815", "Nicolas", "Bravo", "1990-11-04", "1189912233", False)
    e07 = Employee("02-71234985", "Rocio", "Sanchez", "1996-06-09", "1194422311", False)
    e08 = Employee("02-89341277", "Federico", "Diaz", "1983-01-22", "1165547788", False)
    e09 = Employee("02-93412764", "Julieta", "Ortiz", "1997-10-08", "1147899922", False)
    e10 = Employee("02-99834512", "Alejandro", "Campos", "1989-05-16", "1108876655", False)

    employee_list.extend([e01, e02, e03, e04, e05, e06, e07, e08, e09, e10])

def create_appointment_data():
    '''class Appointment():
    appointment_id: str #03-X (first appointment would just be 03-1)
    client: Client
    employee: Employee
    date: str #YYYY-MM-DD
    duration_in_mins: int
    status: Status'''
    a01 = Appointment("03-1",  client_list[0], employee_list[1], "2025-11-01", 60,  Status.CONFIRMED)
    a02 = Appointment("03-2",  client_list[2], employee_list[3], "2025-11-02", 45,  Status.AWAITING_CONFIRMATION)
    a03 = Appointment("03-3",  client_list[5], employee_list[2], "2025-11-03", 30,  Status.CONFIRMED)
    a04 = Appointment("03-4",  client_list[7], employee_list[1], "2025-11-04", 90,  Status.CANCELLED)
    a05 = Appointment("03-5",  client_list[1], employee_list[0], "2025-11-05", 120, Status.NOT_CONFIRMED)

    a06 = Appointment("03-6",  client_list[4], employee_list[6], "2025-11-06", 60,  Status.CONFIRMED)
    a07 = Appointment("03-7",  client_list[6], employee_list[2], "2025-11-07", 45,  Status.AWAITING_CONFIRMATION)
    a08 = Appointment("03-8",  client_list[9], employee_list[5], "2025-11-08", 30,  Status.CONFIRMED)
    a09 = Appointment("03-9",  client_list[3], employee_list[8], "2025-11-09", 75,  Status.CANCELLED)
    a10 = Appointment("03-10", client_list[8], employee_list[4], "2025-11-10", 60,  Status.CONFIRMED)

    a11 = Appointment("03-11", client_list[0], employee_list[1], "2025-11-11", 45,  Status.CONFIRMED)
    a12 = Appointment("03-12", client_list[5], employee_list[2], "2025-11-12", 60,  Status.CONFIRMED)
    a13 = Appointment("03-13", client_list[7], employee_list[1], "2025-11-13", 30,  Status.AWAITING_CONFIRMATION)
    a14 = Appointment("03-14", client_list[6], employee_list[2], "2025-11-14", 120, Status.NOT_CONFIRMED)
    a15 = Appointment("03-15", client_list[9], employee_list[5], "2025-11-15", 90,  Status.CONFIRMED)

    a16 = Appointment("03-16", client_list[2], employee_list[3], "2025-11-16", 60,  Status.CONFIRMED)
    a17 = Appointment("03-17", client_list[4], employee_list[6], "2025-11-17", 45,  Status.CONFIRMED)
    a18 = Appointment("03-18", client_list[1], employee_list[0], "2025-11-18", 30,  Status.CANCELLED)
    a19 = Appointment("03-19", client_list[3], employee_list[8], "2025-11-19", 75,  Status.AWAITING_CONFIRMATION)
    a20 = Appointment("03-20", client_list[8], employee_list[4], "2025-11-20", 60,  Status.CONFIRMED)

    appointment_list.extend([
        a01, a02, a03, a04, a05,
        a06, a07, a08, a09, a10,
        a11, a12, a13, a14, a15,
        a16, a17, a18, a19, a20
    ])

def init_data():
    create_client_data()
    create_employee_data()
    create_appointment_data()
