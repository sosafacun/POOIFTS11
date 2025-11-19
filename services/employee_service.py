from services.iService import IService

class EmployeeService(IService):

    def create(self):
        print("Creating Employee")

    def read(self):
        print("Reading Employees")

    def update(self):
        print("Updating Employee")

    def delete(self):
        print("Deleting Employee")

    def search(self):
        print("Searching Employee")
        