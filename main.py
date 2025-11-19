#rich lib
from utils.rich_ui import RichUI as ui

#DI for the services
from services.client_service import ClientService
client_service = ClientService()

from services.employee_service import EmployeeService
employee_service = EmployeeService()

from services.appointment_service import AppointmentService
appointment_service = AppointmentService()

#DI for the controllers
from controllers.crud_controller import CRUDController
client_controller = CRUDController("Client", client_service, ui)
employee_controller = CRUDController("Employee", employee_service, ui)
appointment_controller = CRUDController("Appointment", appointment_service, ui)

#Assign a controller for each choice
controllers = {
    "1": client_controller,
    "2": employee_controller,
    "3": appointment_controller
}

def load_dummy_data():
    #it was bothering me so i just deleted it. I'll add something later down the line.
    pass

def build_crud_menu(controller):
    return[
    ("1",f"Register new {controller.name}"),
    ("2",f"View all {controller.name}"),
    ("3",f"Update existing {controller.name}"),
    ("4",f"Delete existing {controller.name}"),
    ("5",f"Search for {controller.name}"),
    ("Q","Go back to the main menu")
]

if __name__ == "__main__":

    while True:
        choice = ui.simple_menu(
            "Final OOP Project     |\t\t       IFTS N°11",
            "Student: Facundo Sosa | Professor: Mariano Billi",
            [
                ("1","Client Menu"),
                ("2","Employee Menu"),
                ("3","Appointment Menu"),
                ("Q","Exit Program")
            ]
        )

        if choice == "Q":
            ui.show_loading_message(". . .")
            break
        
        controller = controllers.get(choice)
        if controller:
            controller.run_menu(build_crud_menu(controller))