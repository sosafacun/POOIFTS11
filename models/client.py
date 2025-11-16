# client.py
from datetime import datetime
from models.iPerson import Person

class Client(Person):
    def __init__(
        self,
        name: str,
        dob: str,
        email: str,
        phone: str,
        client_id: int,
        is_bday_gift_active: bool,
        last_visit: str
    ):
        super().__init__(name, dob, email, phone, is_bday_gift_active)
        self.client_id = client_id
        self.last_visit = datetime.strptime(last_visit, "%Y-%m-%d").date()

    #needed in order to check for unfilled fields.
    @staticmethod
    def required_fields():
        return ["name",
        "dob",
        "email",
        "phone",
        "client_id",
        "is_bday_gift_active",
        "last_visit"]
    
    #obj -> dict converter
    def to_dict(self):
        return {
            "client_id": self.client_id,
            "name": self.name,
            "dob": self.dob.strftime("%Y-%m-%d"),
            "email": self.email,
            "phone": self.phone,
            "is_bday_gift_active": self.is_bday_gift_active,
            "last_visit": self.last_visit.strftime("%Y-%m-%d")
        }

    #search support
    def matches(self, needle: str):
        needle = needle.lower()
        return (
            needle in self.name.lower()
            or needle in self.email.lower()
            or needle in self.phone.lower()
            or needle == str(self.client_id)
        )

    #stringified output for display
    def __str__(self):
        return (
            f"[bold cyan]Client ID:[/bold cyan] {self.client_id}\n"
            f"Name: {self.name}\n"
            f"DOB: {self.dob}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}\n"
            f"Last Visit: {self.last_visit}"
        )
