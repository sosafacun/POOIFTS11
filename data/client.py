from data.iPerson import Person

class Client(Person):
    def __init__(self, name: str, dob: str, email: str, phone:str, client_id: int):
        super().__init__(name, dob, email, phone)
        self.client_id = client_id
        
    def __str__(self):
        return f"Client {self.client_id}:\nName: {self.name}\ne-Mail: {self.email}\nAge:{self.get_age()}"