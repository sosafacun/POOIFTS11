from utils.rich_ui import console, make_panel, make_menu, display_centered, pause, crud_menu
from rich.panel import Panel

def show_employee_menu():
    items = [
        ("1", "Register new employee"),
        ("2", "View all employees"),
        ("3", "Update employee information"),
        ("4", "Delete employee"),
        ("5", "Search for an employee"),
        ("B", "Back to Main Menu"),
    ]

    for choice in crud_menu("Employee Management Menu", "CRUD operations + Search", items):
        if(choice == "1"):
            console.print(Panel("[bold green]Registering new employee...[/bold green]"))
        elif(choice == "2"):
            console.print(Panel("[bold cyan]Displaying all employees...[/bold cyan]"))
        elif(choice == "3"):
            console.print(Panel("[bold yellow]Updating employee information...[/bold yellow]"))
        elif(choice == "4"):
            console.print(Panel("[bold red]Deleting an employee...[/bold red]"))
        elif(choice == "5"):
            console.print(Panel("[bold blue]Searching for a employee...[/bold blue]"))


if __name__ == "__main__":
    show_employee_menu()
