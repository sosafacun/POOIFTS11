from utils.rich_ui import console, make_panel, make_menu, display_centered, pause
from rich.prompt import Prompt
from rich.panel import Panel

def show_client_menu():
    while True:
        console.clear()

        # Header
        display_centered(make_panel("Client Management Menu", "CRUD operations + Search"))

        # Menu
        items = [
            ("1", "Register new client"),
            ("2", "View all clients"),
            ("3", "Update client information"),
            ("4", "Delete client"),
            ("5", "Search for a client"),
            ("B", "Back to Main Menu"),
        ]
        menu = make_menu("Client Menu", items, border_color="bright_green")
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
            console.print(Panel("[bold green]Registering new client...[/bold green]"))
        elif choice == "2":
            console.print(Panel("[bold green]Displaying all clients...[/bold green]"))
        elif choice == "3":
            console.print(Panel("[bold green]Updating client information...[/bold green]"))
        elif choice == "4":
            console.print(Panel("[bold green]Deleting a client...[/bold green]"))
        elif choice == "5":
            console.print(Panel("[bold green]Searching for client...[/bold green]"))

        pause()


if __name__ == "__main__":
    show_client_menu()
