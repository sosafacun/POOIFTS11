from services.iService import IService
from utils.rich_ui import RichUI as ui

from repositories.data.data import client_list

class ClientService(IService):

    def create(self):
        ui.pause_message("creating obj")
            
    def read(self):
        ui.show_cards(client_list)

    def update(self):
        ui.pause_message("updating obj")

    def delete(self):
        ui.pause_message("deleting obj")

    def search(self):
        ui.pause_message("searching obj")
        