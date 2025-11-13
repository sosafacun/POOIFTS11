from utils.rich_ui import RichUI as ui
from rich.panel import Panel


def show_employee_menu():
    #menu items
    items = [
        ("1", "Register new employee"),
        ("2", "View all employees"),
        ("3", "Update employee information"),
        ("4", "Delete employee"),
        ("5", "Search for an employee"),
        ("Q", "Back to Main Menu"),
    ]

    #calls ui crud_menu creation.
    for choice in ui.crud_menu("Employee Management Menu", "CRUD operations + Search", items):
        if choice == "1":
            ui.console.print(Panel("[bold green]Registering new employee...[/bold green]"))
        elif choice == "2":
            ui.console.print(Panel("[bold cyan]Displaying all employees...[/bold cyan]"))
        elif choice == "3":
            ui.console.print(Panel("[bold yellow]Updating employee information...[/bold yellow]"))
        elif choice == "4":
            ui.console.print(Panel("[bold red]Deleting an employee...[/bold red]"))
        elif choice == "5":
            ui.console.print(Panel("[bold blue]Searching for an employee...[/bold blue]"))
