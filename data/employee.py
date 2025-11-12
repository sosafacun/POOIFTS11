from datetime import datetime
from rich.console import Console
from rich.table import Table
from data.iPerson import Person


class Employee(Person):
    def __init__(self, name: str, dob: str, email: str, phone: str, employee_id: int, is_bday_gift_active: bool):
        super().__init__(name, dob, email, phone, is_bday_gift_active)
        self.employee_id = employee_id

    def __str__(self):
        table = Table(
            title=f"Employee {self.employee_id}",
            title_style="bold blue",
            border_style="magenta",
            show_header=False
        )

        table.add_row("[green]Name[/green]", f"[white]{self.name}[/white]")
        table.add_row("[green]e-Mail[/green]", f"[white]{self.email}[/white]")
        table.add_row("[green]Age[/green]", f"[white]{self.get_age()}[/white] | [dim]{self.dob}[/dim]")

        console = Console()
        console.print(table)
        return ""