from utils.rich_ui import console, make_panel, make_menu, display_centered, pause
from rich.prompt import Prompt
from rich.panel import Panel

def show_appointment_menu():
    while True:
        console.clear()

        # Header
        display_centered(make_panel("Appointment Management Menu", "CRUD operations + Search"))

        # Menu
        items = [
            ("1", "Register new appointment"),
            ("2", "View all appointments"),
            ("3", "Re-schedule an appointment"),
            ("4", "Delete an appointment"),
            ("5", "Search for an appointment"),
            ("B", "Back to Main Menu"),
        ]
        menu = make_menu("Appointment Menu", items, border_color="bright_green")
        display_centered(menu)
        display_centered("[bold white]Select an option (1–5 or B)[/bold white]")

        choice = Prompt.ask(
            "\n[bold bright_cyan]Enter your choice[/bold bright_cyan]",
            choices=[str(i) for i in range(1, 6)] + ["B", "b"],
            default="B"
        ).upper()


        console.clear()

        if choice == "B":
            console.print(Panel("[bright_red]Returning to main menu...[/bright_red]"))
            break

        elif choice == "1":
            console.print(Panel("[bold green]Registering new appointment...[/bold green]"))
        elif choice == "2":
            console.print(Panel("[bold green]Displaying all appointments...[/bold green]"))
        elif choice == "3":
            console.print(Panel("[bold green]Re-scheduling an appointment...[/bold green]"))
        elif choice == "4":
            console.print(Panel("[bold green]Deleting an appointment...[/bold green]"))
        elif choice == "5":
            console.print(Panel("[bold green]Searching for appointment...[/bold green]"))

        pause()


if __name__ == "__main__":
    show_appointment_menu()
