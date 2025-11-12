from enum import Enum

class Status(Enum):
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"
    NOT_CONFIRMED = "Not Confirmed"
    AWAITING_CONFIRMATION = "Awaiting Confirmation"

    def __str__(self):
        return self.value
