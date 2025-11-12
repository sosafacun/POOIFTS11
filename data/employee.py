from data.iPerson import Person

class Employee(Person):
    def __init__(self, name: str, dob: str, email: str, phone:str, employee_id: int):
        super().__init__(name, dob, email, phone)
        self.employee_id = employee_id
        
    def __str__(self):
        return f"Employee {self.employee_id}:\nName: {self.name}\ne-Mail: {self.email}\nAge:{self.get_age()}"