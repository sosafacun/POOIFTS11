from utils.rich_ui import RichUI as ui
from utils.builder import build

controllers = build()

def build_crud_menu(controller):
    return[
    ("1",f"Register new {controller.name}"),
    ("2",f"View all {controller.name}"),
    ("3",f"Update existing {controller.name}"),
    ("4",f"Delete existing {controller.name}"),
    ("5",f"Search for {controller.name}"),
    ("Q","Go back to the main menu")
]

def main():

    while True:
        choice = ui.simple_menu(
            "Final OOP Project     |\t\t       IFTS N°11",
            "Student: Facundo Sosa | Professor: Emiliano Billi",
            [
                ("1","Client Menu"),
                ("2","Employee Menu"),
                ("3","Appointment Menu"),
                ("Q","Exit Program")
            ]
        )

        if choice == "Q":
            ui.show_loading_message(". . .")
            break
        
        controller = controllers.get(choice)
        if controller:
            controller.run_menu(build_crud_menu(controller))

if __name__ == "__main__":
    main()
