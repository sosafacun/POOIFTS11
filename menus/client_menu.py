from utils.rich_ui import console, make_panel, make_menu, display_centered, pause, crud_menu
from rich.panel import Panel

def show_client_menu():
    items = [
        ("1", "Register new client"),
        ("2", "View all clients"),
        ("3", "Update client information"),
        ("4", "Delete client"),
        ("5", "Search for a client"),
        ("B", "Back to Main Menu"),
    ]

    for choice in crud_menu("Client Management Menu", "CRUD operations + Search", items):
        if(choice == "1"):
            console.print(Panel("[bold green]Registering new client...[/bold green]"))
        elif(choice == "2"):
            console.print(Panel("[bold cyan]Displaying all clients...[/bold cyan]"))
        elif(choice == "3"):
            console.print(Panel("[bold yellow]Updating client information...[/bold yellow]"))
        elif(choice == "4"):
            console.print(Panel("[bold red]Deleting a client...[/bold red]"))
        elif(choice == "5"):
            console.print(Panel("[bold blue]Searching for a client...[/bold blue]"))


if __name__ == "__main__":
    show_client_menu()
