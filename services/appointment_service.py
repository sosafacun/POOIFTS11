from services.iService import IService
from utils.rich_ui import RichUI as ui

class AppointmentService(IService):

    def create(self):
        print("Creating appointment")

    def read(self):
        print("Reading appointments")

    def update(self):
        print("Updating appointment")

    def delete(self):
        print("Deleting appointment")

    def search(self):
        print("Searching appointment")
        