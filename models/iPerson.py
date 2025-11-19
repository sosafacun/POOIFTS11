from abc import ABC, abstractmethod # Used to create non-instanciable calsses and methods. Not supported by Python directly.
from datetime import date, datetime

class Person(ABC):
    def __init__(self,
        name: str,
        dob: str,
        email: str,
        phone: str,
        is_bday_gift_active: bool):

        self.name = name
        self.dob = datetime.strptime(dob, "%Y-%m-%d").date()
        self.email = email
        self.phone = phone
        self.is_bday_gift_active = is_bday_gift_active
    
    # Will be overwritten by Client and Employee __to_dict__ implementations.
    @abstractmethod
    def to_dict(self):
        pass

    # Returns the age of a person.
    def get_age(self) -> int:
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))