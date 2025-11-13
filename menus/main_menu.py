from utils.rich_ui import RichUI as ui
from rich.panel import Panel


def show_main_menu():
    items = [
        ("1", "Client Menu"),
        ("2", "Employee Menu"),
        ("3", "Appointment Menu"),
        ("4", "Non-existent Menu"),
        ("Q", "Quit the program"),
    ]

    return ui.simple_menu(
        "OOP Final Project\t\t|\t\tIFTS N°11",
        "Teacher: Billi, Emiliano | Student: Sosa, Facundo Nicolás",
        items
    )
