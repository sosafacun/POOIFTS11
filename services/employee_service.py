from services.iService import IService
from utils.rich_ui import RichUI as ui

from repositories.data.data import employee_list

class EmployeeService(IService):

    def create(self):
        ui.pause_message("creating obj")
            
    def read(self):
        ui.show_cards(employee_list)

    def update(self):
        ui.pause_message("updating obj")

    def delete(self):
        ui.pause_message("deleting obj")

    def search(self):
        ui.pause_message("searching obj")
        