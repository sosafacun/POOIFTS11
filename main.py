#rich libraries
from utils.rich_ui import console, make_panel, make_menu, display_centered, pause
from rich.prompt import Prompt
from rich.panel import Panel
from rich.align import Align

#exceptions
from utils.exceptions import throw_exception

#data packages
from data.client import Client
from data.employee import Employee

#menus
from menus.client_menu import show_client_menu
from menus.employee_menu import show_employee_menu
from menus.appointment_menu import show_appointment_menu


def load_dummy_data():

    # dummy testing data. I should delete this in favour of the .csv, but this will do for the time being, despite not returning anything.
    clients = [
        Client("Alice Johnson", "1990-05-12", "alice.johnson@email.com", "555-0142", 101, False, "2025-11-01"),
        Client("Brian Smith", "1985-09-23", "brian.smith@email.com", "555-0199", 102, False, "2025-10-18"),
        Client("Cynthia Lee", "1998-02-17", "cynthia.lee@email.com", "555-0283", 103, False, "2025-09-30"),
        Client("David Brown", "1977-11-02", "david.brown@email.com", "555-0355", 104, True, "2025-08-25"),
        Client("Elena Davis", "2001-08-30", "elena.davis@email.com", "555-0411", 105, False, "2025-11-05")
    ]

    employees = [
        Employee("Frank Wilson", "1982-03-14", "frank.wilson@company.com", "555-0510", 201, False),
        Employee("Grace Miller", "1995-12-08", "grace.miller@company.com", "555-0602", 202, False),
        Employee("Henry Clark", "1979-07-25", "henry.clark@company.com", "555-0714", 203, False),
        Employee("Isabella Moore", "1992-10-19", "isabella.moore@company.com", "555-0833", 204, False),
        Employee("Jack Taylor", "1988-01-05", "jack.taylor@company.com", "555-0976", 205, False)
    ]

def show_main_menu():
    console.clear()

    #Title
    display_centered(make_panel("OOP Final Project\t\t|\t\tIFTS N°11", "Teacher: Billi, Emiliano | Student: Sosa, Facundo Nicolás"))

    # Menu setup and display
    menu_options = [
        ("1", "Client Menu"),
        ("2", "Employee Menu"),
        ("3", "Appointment Menu"),
        ("4", "Non-existant Menu"),
        ("Q", "Quit the program")
    ]
    menu = make_menu("Main Menu", menu_options, border_color="bright_green")
    display_centered(menu)
    display_centered("[bold white]Select an option (1–4 or Q)[/bold white]")

    # Wait for user Input
    choice = Prompt.ask("\n[bold bright_cyan]Enter your choice[/bold bright_cyan]", choices=[str(i) for i in range(1, 5)] + ["q", "Q"], default="Q")
    return choice.upper()

if __name__ == "__main__":
    load_dummy_data()
    while True:
        try:
            option = show_main_menu()
            console.clear()

            if(option == "1"):
                show_client_menu()
            elif(option == "2"):
                show_employee_menu()
            elif(option == "3"):
                show_appointment_menu()
            elif(option == "4"):
                show_non_existent_menu()
            elif(option == "Q"):
                console.print(Panel("[bold red]Exiting...[/bold red]"))
                break
        
        except KeyError as e:
            console.print(Panel(f"[red]KeyError: {e}[/red]"))
        except ValueError as e:
            console.print(Panel(f"[red]ValueError: {e}[/red]"))
        except Exception as e:
            console.print(Panel(f"[red]Unhandled Exception: {e}[/red]"))

        console.input("\n[dim]Press Enter to return to the main menu...[/dim]")
