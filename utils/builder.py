from repositories.data.data import client_list, employee_list, appointment_list, init_data

from repositories.models.client import Client
from repositories.models.employee import Employee
from repositories.models.appointment import Appointment
from repositories.models.schemas import CLIENT_SCHEMA, EMPLOYEE_SCHEMA, APPOINTMENT_SCHEMA

from services.crud_service import CRUDService

from controllers.crud_controller import CRUDController

from utils.rich_ui import RichUI as ui


#init the data, services and controllers
def build():
    init_data()

    client_service = CRUDService(Client, CLIENT_SCHEMA, client_list)
    employee_service = CRUDService(Employee, EMPLOYEE_SCHEMA, employee_list)
    appointment_service = CRUDService(Appointment, APPOINTMENT_SCHEMA, appointment_list)

    client_controller = CRUDController("Client", client_service, ui)
    employee_controller = CRUDController("Employee", employee_service, ui)
    appointment_controller = CRUDController("Appointment", appointment_service, ui)

    return{
        "1": client_controller,
        "2": employee_controller,
        "3": appointment_controller
    }