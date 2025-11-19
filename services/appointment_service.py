from services.iService import IService

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
        