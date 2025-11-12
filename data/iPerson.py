from abc import ABC, abstractmethod # Used to create non-instanciable calsses and methods. Not supported by Python directly.
from datetime import date, datetime

class Person(ABC):
    def __init__(self, name: str, dob: str, email: str, phone: str):
        self.name = name
        self.dob = datetime.strptime(dob, "%Y-%m-%d").date()
        self.email = email
        self.phone = phone

    # Will then be overwritten by Client and Employee __str__ implementations.
    @abstractmethod
    def __str__(self):
        pass
    
    def get_age(self) -> int:
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))