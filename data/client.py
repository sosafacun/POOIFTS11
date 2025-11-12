from datetime import datetime
from rich.console import Console
from rich.table import Table
from data.iPerson import Person


class Client(Person):
    def __init__(self, name: str, dob: str, email: str, phone: str, client_id: int, is_bday_gift_active: bool, last_visit: str):
        super().__init__(name, dob, email, phone, is_bday_gift_active)
        self.client_id = client_id
        self.last_visit = datetime.strptime(last_visit, "%Y-%m-%d").date()

    def __str__(self):
        table = Table(
            title=f"Client {self.client_id}",
            title_style="bold yellow",
            border_style="cyan",
            show_header=False
        )

        table.add_row("[green]Name[/green]", f"[white]{self.name}[/white]")
        table.add_row("[green]e-Mail[/green]", f"[white]{self.email}[/white]")
        table.add_row("[green]Age[/green]", f"[white]{self.get_age()}[/white] | [dim]{self.dob}[/dim]")
        table.add_row("[green]Last visit[/green]", f"[white]{self.last_visit}[/white]")

        console = Console()
        console.print(table)
        return ""