# universal_manager.py

from utils.rich_ui import RichUI as ui
from rich.panel import Panel

class UniversalManager:

    def __init__(self, entity_name, entity_class, datastore: list):
        self.entity_name = entity_name          # "Client", "Employee", "Appointment"
        self.entity_class = entity_class        # class Client / Employee / Appointment
        self.datastore = datastore              # the in-memory list holding them

    # CREATE
    def create(self):
        ui.clear()
        ui.center(Panel(f"[bold green]Register new {self.entity_name}[/bold green]"))

        try:
            fields = self.entity_class.required_fields()

            inputs = {}
            for field in fields:
                inputs[field] = ui.console.input(f"{field}: ")

            obj = self.entity_class(**inputs)
            self.datastore.append(obj)

            ui.console.print(Panel(f"[bold green]{self.entity_name} created successfully[/bold green]"))

        except Exception as e:
            ui.console.print(Panel(f"[red]Error creating {self.entity_name}: {e}[/red]"))

        ui.pause()

    # READ ALL
    def view_all(self):
        ui.clear()
        ui.center(Panel(f"[bold cyan]All {self.entity_name}s[/bold cyan]"))

        if not self.datastore:
            ui.console.print(Panel(f"[yellow]No {self.entity_name}s found[/yellow]"))
        else:
            for obj in self.datastore:
                ui.console.print(Panel(str(obj)))

        ui.pause()

    # UPDATE
    def update(self):
        ui.clear()
        ui.center(Panel(f"[bold yellow]Update {self.entity_name}[/bold yellow]"))

        obj_id = ui.console.input("Enter ID: ")

        target = None
        for obj in self.datastore:
            if str(obj.id) == obj_id:
                target = obj
                break

        if not target:
            ui.console.print(Panel(f"[red]{self.entity_name} not found[/red]"))
            ui.pause()
            return

        fields = target.to_dict()

        for key, value in fields.items():
            new_val = ui.console.input(f"{key} [{value}]: ")
            if new_val.strip():
                setattr(target, key, new_val)

        ui.console.print(Panel(f"[bold green]{self.entity_name} updated successfully[/bold green]"))
        ui.pause()

    # DELETE
    def delete(self):
        ui.clear()
        ui.center(Panel(f"[bold red]Delete {self.entity_name}[/bold red]"))

        obj_id = ui.console.input("Enter ID: ")

        for i, obj in enumerate(self.datastore):
            if str(obj.id) == obj_id:

                if ui.confirm_action(f"Delete {self.entity_name}?", "This action cannot be undone."):
                    del self.datastore[i]
                    ui.console.print(Panel(f"[bold red]{self.entity_name} deleted[/bold red]"))
                else:
                    ui.console.print(Panel("[yellow]Deletion cancelled[/yellow]"))

                ui.pause()
                return

        ui.console.print(Panel(f"[red]{self.entity_name} not found[/red]"))
        ui.pause()

    # SEARCH
    def search(self):
        ui.clear()
        ui.center(Panel(f"[bold blue]Search {self.entity_name}[/bold blue]"))

        needle = ui.console.input("Search: ")

        results = []
        for obj in self.datastore:
            if obj.matches(needle):
                results.append(obj)

        if results:
            for obj in results:
                ui.console.print(Panel(str(obj)))
        else:
            ui.console.print(Panel("[yellow]No matches found[/yellow]"))

        ui.pause()
