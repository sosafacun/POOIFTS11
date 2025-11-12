from datetime import datetime
from data.iPerson import Person


class Client(Person):
    def __init__(self,
        name: str,
        dob: str,
        email: str,
        phone: str,
        client_id: int,
        is_bday_gift_active: bool,
        last_visit: str):

        super().__init__(name, dob, email, phone, is_bday_gift_active)
        
        self.client_id = client_id
        self.last_visit = datetime.strptime(last_visit, "%Y-%m-%d").date()

    def to_dict(self):
        return{
            "client_id": self.client_id,
            "name": self.name,
            "dob": self.dob.strftime("%Y-%m-%d"),
            "email": self.email,
            "phone": self.phone,
            "is_bday_gift_active": self.is_bday_gift_active,
            "last_visit": self.last_visit.strftime("%Y-%m-%d")
        }