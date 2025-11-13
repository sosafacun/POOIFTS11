from utils.rich_ui import RichUI as ui
from rich.panel import Panel


def show_appointment_menu():
    #menu items
    items = [
        ("1", "Register new appointment"),
        ("2", "View all appointments"),
        ("3", "Update appointment information"),
        ("4", "Delete appointment"),
        ("5", "Search for an appointment"),
        ("Q", "Back to Main Menu"),
    ]

    #calls ui crud_menu creation.
    for choice in ui.crud_menu("appointment Management Menu", "CRUD operations + Search", items):
        if choice == "1":
            ui.console.print(Panel("[bold green]Registering new appointment...[/bold green]"))
        elif choice == "2":
            ui.console.print(Panel("[bold cyan]Displaying all appointments...[/bold cyan]"))
        elif choice == "3":
            ui.console.print(Panel("[bold yellow]Updating appointment information...[/bold yellow]"))
        elif choice == "4":
            ui.console.print(Panel("[bold red]Deleting an appointment...[/bold red]"))
        elif choice == "5":
            ui.console.print(Panel("[bold blue]Searching for an appointment...[/bold blue]"))
