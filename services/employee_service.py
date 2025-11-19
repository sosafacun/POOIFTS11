from services.iService import IService
from utils.rich_ui import RichUI as ui

class EmployeeService(IService):

    def create(self):
        try:
            ui.pause()
        except Exception as e:
            ui.throw_exception("failed: ",)
            
    def read(self):
        ui.pause()

    def update(self):
        ui.pause()

    def delete(self):
        ui.pause()

    def search(self):
        ui.pause()
        