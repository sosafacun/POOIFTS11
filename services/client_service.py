from services.iService import IService

class ClientService(IService):

    def create(self):
        print("Creating client")

    def read(self):
        print("Reading clients")

    def update(self):
        print("Updating client")

    def delete(self):
        print("Deleting client")

    def search(self):
        print("Searching client")
        