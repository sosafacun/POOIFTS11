from utils.rich_ui import RichUI as ui
from rich.panel import Panel

# menus
from menus.main_menu import show_main_menu
from menus.client_menu import show_client_menu
from menus.employee_menu import show_employee_menu
from menus.appointment_menu import show_appointment_menu


def load_dummy_data():
    #it was bothering me so i just deleted it. I'll add something later down the line.
    pass


if __name__ == "__main__":
    #TODO: change this to load .csv files
    load_dummy_data()

    while True:
        try:
            option = show_main_menu()
            ui.clear()

            if option == "1":
                show_client_menu()

            elif option == "2":
                show_employee_menu()

            elif option == "3":
                show_appointment_menu()

            elif option == "4":
                ui.confirm_action("Are you sure you want to exit?", "Any unsaved data will be lost...")

            elif option == "Q":
                ui.console.print(Panel("[bold red]Exiting...[/bold red]"))
                break

        except Exception as e:
            ui.console.print(Panel(f"[red]Unhandled Exception: {e}[/red]"))
            ui.pause("Please press 'Enter' key to continue...")
