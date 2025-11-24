from services.iService import IService
from utils.rich_ui import RichUI as ui

class CRUDService(IService):
    def __init__(self, model, schema, storage):
        self.model = model
        self.schema = schema
        self.storage = storage #the (whatever)_list in this case. This has to be replaced with the read .csv list

    def create(self):
        ui.show_loading_message(f"Creating {self.model.__name__}")

        try:
            values = collect_data(self.schema)
            obj = self.model(**values)
            validate_object(obj, self.schema)
            self.storage.append(obj)
            ui.pause_message(f"{self.model.__name__} created successfully!")
        
        except Exception as e:
            ui.throw_exception(f"Error creating {self.model.__name__}", e)
            ui.pause()
        
    def read(self):
        ui.show_cards(self.storage)
    
    def update(self):
        ui.pause_message("updating obj")

    def delete(self):
        ui.pause_message("deleting obj")

    def search(self):
        ui.pause_message("searching obj")