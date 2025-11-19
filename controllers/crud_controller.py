from utils.rich_ui import RichUI as ui

class CRUDController():
    def __init__(self, name, service, ui):
        self.name = name
        self.service = service
        self.ui = ui

    def run_menu(self, menu_items):
        while True:
            choice = self.ui.simple_menu(self.name + " CRUD + Search", menu_items)
            if choice == "Q":
                return
            self.handle(choice)

    def handle(self, choice):
        actions = {
            "1": self.service.create,
            "2": self.service.read,
            "3": self.service.update,
            "4": self.service.delete,
            "5": self.service.search
        }
        action = actions.get(choice)
        
        if action:
            action()