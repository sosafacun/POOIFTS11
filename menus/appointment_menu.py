from utils.rich_ui import console, make_panel, make_menu, display_centered, pause, crud_menu
from rich.panel import Panel

def show_appointment_menu():
    items = [
        ("1", "Register new appointment"),
        ("2", "View all appointments"),
        ("3", "Re-schedule an appointment"),
        ("4", "Delete appointment"),
        ("5", "Search for an appointment"),
        ("B", "Back to Main Menu"),
    ]

    for choice in crud_menu("Appointment Management Menu", "CRUD operations + Search", items):
        if(choice == "1"):
            console.print(Panel("[bold green]Registering new appointment...[/bold green]"))
        elif(choice == "2"):
            console.print(Panel("[bold cyan]Displaying all appointments...[/bold cyan]"))
        elif(choice == "3"):
            console.print(Panel("[bold yellow]Re-scheduling an appointment...[/bold yellow]"))
        elif(choice == "4"):
            console.print(Panel("[bold red]Deleting an appointment...[/bold red]"))
        elif(choice == "5"):
            console.print(Panel("[bold blue]Searching for an appointment...[/bold blue]"))


if __name__ == "__main__":
    show_appointment_menu()
