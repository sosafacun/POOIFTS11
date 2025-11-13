from utils.rich_ui import RichUI as ui
from rich.panel import Panel


def show_client_menu():
    #menu items
    items = [
        ("1", "Register new client"),
        ("2", "View all clients"),
        ("3", "Update client information"),
        ("4", "Delete client"),
        ("5", "Search for a client"),
        ("Q", "Back to Main Menu"),
    ]

    #calls ui crud_menu creation.
    for choice in ui.crud_menu("Client Management Menu", "CRUD operations + Search", items):
        if choice == "1":
            ui.console.print(Panel("[bold green]Registering new client...[/bold green]"))
        elif choice == "2":
            ui.console.print(Panel("[bold cyan]Displaying all clients...[/bold cyan]"))
        elif choice == "3":
            ui.console.print(Panel("[bold yellow]Updating client information...[/bold yellow]"))
        elif choice == "4":
            ui.console.print(Panel("[bold red]Deleting a client...[/bold red]"))
        elif choice == "5":
            ui.console.print(Panel("[bold blue]Searching for a client...[/bold blue]"))
