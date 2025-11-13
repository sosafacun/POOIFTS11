from typing import List, Tuple

#rich libraries
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich import box
from rich.prompt import Prompt
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn

#libs for the loading bards
import time
import random

class RichUI:
    console = Console()
    
    #builds the Title panel. The one that's on top of any menu
    @staticmethod
    def make_panel(title: str, subtitle: str = "", color: str = "bright_blue"):
        text = f"[bold cyan]{title}[/bold cyan]"
        if subtitle:
            text += f"\n[dim]{subtitle}[/dim]"
        return Panel.fit(text, border_style=color)

    #builds the menu frames and gets the data as a Tuple list to send it over to the _menu_core
    @staticmethod
    def make_menu(items: List[Tuple[str, str]], border_color: str = "bright_green") -> Table:
        menu = Table(
            box=box.DOUBLE_EDGE,
            border_style=border_color,
            show_header=False,
            padding=(0, 2)
        )
        for key, desc in items:
            menu.add_row(f"[green]{key}[/green]", desc)
        return menu
    
    #builds any menu. It needs a title, a subtitle and a tuple list (not quite like, but like an "unga bunga" dictionary) 
    #to list all the possible options
    #it also handles input verification
    @staticmethod
    def _menu_core(title: str, subtitle: str, items: List[Tuple[str, str]]):
        RichUI.clear()
        RichUI.center(RichUI.make_panel(title, subtitle))
        menu = RichUI.make_menu(items)
        RichUI.center(menu)

        #create valid keys
        valid_keys = [key.lower() for key, _ in items] + ["Q"]

        #ask for user input
        choice = Prompt.ask(
            "\n[bold white]Select an option[/bold white]",
            choices=valid_keys,
            default="Q"
        ).upper()
        if(choice != "Q"):
            RichUI.loading()

        return choice

    #CRUD menu builder for appointments, clients and employees
    @staticmethod
    def crud_menu(title: str, subtitle: str, items: List[Tuple[str, str]]):
        #stay in the menu until the user presses q-Q or Enter
        while True:
            try:
                choice = RichUI._menu_core(title, subtitle, items)

                if choice == "Q":
                    RichUI.console.print(Panel("[bright_red]Returning to main menu...[/bright_red]"))
                    RichUI.loading()
                    RichUI.clear()
                    break
                
                #i need to yield the choice in order to send it over to the menu
                #without exiting the loop from the crud_menu
                yield choice

            except Exception as e:
                RichUI.console.print(Panel(f"[red]Error creating the CRUD menu: {e}[/red]"))
                RichUI.pause()

    #main menu. It has a slightly diff set up since I need the while true in main.py, not in the menu itself
    #(this menu is either on screen or not on screen).
    @staticmethod
    def simple_menu(title: str, subtitle: str, items: List[Tuple[str, str]]):
        try:
            return RichUI._menu_core(title, subtitle, items)
        except Exception as e:
            RichUI.console.print(Panel(f"[red]Error creating the main menu: {e}[/red]"))
            RichUI.pause()

    #fancy loading bar. It doesn't do anything else
    #i felt as tho going from one screen to the other was just too jarring.
    @staticmethod
    def loading():
        duration = random.uniform(0.5, 1.5)

        with Progress(
            TextColumn("[bold cyan]Loading[/bold cyan]"),
            BarColumn(),
            TimeRemainingColumn(),
            transient=True,
            console=RichUI.console
        ) as progress:

            task = progress.add_task("", total=duration)
            start = time.perf_counter()

            while True:
                elapsed = time.perf_counter() - start
                if elapsed >= duration:
                    progress.update(task, completed=duration)
                    break
                progress.update(task, completed=elapsed)
                time.sleep(0.05)

    #warning message that will have any string displayed          
    @staticmethod
    def confirm_action(message: str, subtitle: str) -> bool:
        warning_panel = Panel.fit(
            f"[bold bright_yellow]{message}[/bold bright_yellow]\n\n"
            f"[dim]{subtitle}[/dim]\n\n"
            f"[cyan]Confirm? (Y/N)[/cyan]",
            border_style="bright_red"
        )

        RichUI.center(warning_panel)

        choice = Prompt.ask(
            "\n[bold white]Enter your choice[/bold white]",
            choices=["y", "n"],
            default="N"
        ).upper()

        RichUI.loading()
        return choice == "Y"

    #use and abuse the static methods
    #these are just normal methods from rich that I made static
    #so i can use them with ui.whatever()
    @staticmethod
    def clear():
        RichUI.console.clear()

    @staticmethod
    def center(obj):
        RichUI.console.print(Align.center(obj))

    @staticmethod
    def pause(message: str):
        RichUI.console.input(f"\n[dim]{message}[/dim]")
