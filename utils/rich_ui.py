from typing import List, Tuple

#rich libraries
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich import box
from rich.prompt import Prompt
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.live import Live
from rich.columns import Columns

#libs for the loading bards
import time
import random
from math import ceil

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
    #if it does 2 things then maybe i need to split it? idk. It's a menu core, so maybe it's fine for it to do 2 things.
    @staticmethod
    def _menu_core(title: str, subtitle: str, items: List[Tuple[str, str]]):
        RichUI.clear()
        RichUI.center(RichUI.make_panel(title, subtitle))
        menu = RichUI.make_menu(items)
        RichUI.center(menu)

        #create valid keys (inputs)
        valid_keys = [key.lower() for key, _ in items]

        return RichUI._option_select(valid_keys, "Q")

    @staticmethod
    def _option_select(valid_keys, default_opt):
        choice = Prompt.ask(
            "\n[bold white]Select an option[/bold white]",
            choices=valid_keys,
            default=default_opt
        ).upper()
        if(choice != "Q"):
            pass

        return choice
    
    @staticmethod
    def prompt_user(msg: str):
        while True:
            user_input = Prompt.ask(f"\n[bold white]{msg}[/bold white]").strip()
            if(user_input):
                return user_input
            RichUI.warning("\nField cannot be blank")
            
    #simple menu. It does what it seems. Renders a simple menu
    @staticmethod
    def simple_menu(title: str, subtitle: str, items: List[Tuple[str, str]]):
        RichUI.show_loading_message(title)
        try:
            return RichUI._menu_core(title, subtitle, items)
        except Exception as e:
            RichUI.console.print(Panel(f"[red]Error creating menu: {e}[/red]"))
            RichUI.pause()

    #fancy loading bar. It doesn't do anything else
    #i felt as tho going from one screen to the other was too jarring.
    @staticmethod
    def _show_loading_bar():
        duration = random.uniform(0.5, 1.5)

        progress = Progress(
            BarColumn(),
            TimeRemainingColumn(),
            expand=False,
            console=RichUI.console
        )

        task = progress.add_task("", total=duration)
        centered = Align.center(progress)

        #since i need the bar centered, this will
        #refresh the display (cannot center AND have a progressive bar)
        with Live(centered, refresh_per_second=30, console=RichUI.console):
            start = time.perf_counter()
            while True:
                elapsed = time.perf_counter() - start
                if elapsed >= duration:
                    progress.update(task, completed=duration)
                    break

                progress.update(task, completed=elapsed)
                time.sleep(0.05)

        RichUI.clear()

    #this is how it gets called from any menu
    @staticmethod
    def show_loading_message(message: str):
        panel = Panel.fit(
            f"[bold cyan]Loading {message}[/bold cyan]",
            border_style="bright_blue"
        )

        RichUI.center(panel)
        RichUI._show_loading_bar()

    #warning message that will have any string displayed          
    @staticmethod
    def confirm_action(message: str, subtitle: str) -> bool:
        warning_panel = Panel.fit(
            f"[bold bright_yellow]WARNING[/bold bright_yellow]\n\n"
            f"[bold white]{message}[/bold white]\n\n"
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

        RichUI.show_loading_message(". . .")
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
    def pause_message(message: str):
        RichUI.console.input(f"\n[dim]{message}[/dim]")

    @staticmethod
    def pause():
        RichUI.console.input(f"\n[dim]Press 'Enter' to continue . . .[/dim]")
    
    @staticmethod
    def throw_exception(msg,e):
        RichUI.console.print(Panel(f"[red]{msg}: {e}[/red]"))

    @staticmethod
    def warning_message(msg: str):
        RichUI.console.print(Panel(f"[red]{msg}[/red]"))

    @staticmethod
    def show_cards(items):
        RichUI.show_loading_message(". . .")
        RichUI.paginate(items, 6)

    #having 10+ entries was making the ui ugly
    #pagination only shows 6
    #. increases the page number
    #, decreases the page number
    #q goes back to the previous menu
    @staticmethod
    def paginate(items, page_size):
        #ceiling rounds up the number of pages needed
        pages = ceil(len(items) / page_size)
        index = 0

        while True:
            RichUI.clear()

            start = index * page_size
            end = start + page_size
            chunk = items[start:end]

            #create the cards
            panels = []
            for obj in chunk:
                left, right = obj.card_header()
                header = f"{left:<15} | {right}"

                line = "─" * len(header)
                line = f"[cyan]{line}[/cyan]"

                body_lines = [f"{label}: {value}" for label, value in obj.card_body()]
                body = "\n".join(body_lines)
                content = f"{header}\n{line}\n{body}"

                panels.append(Panel(content, border_style=obj.card_color()))

            RichUI.center(Columns(panels, equal=True, expand=True))

            #show navigational options
            nav_text = f"[dim]Page {index+1}/{pages} | '.' next | ',' prev | 'Q' Go Back[/dim]"
            RichUI.console.print(f"\n{nav_text}")

            #get navigational options
            choice = Prompt.ask("", choices=[".", ",", "Q", "q"], default="Q")
            
            if choice.upper() == "Q":
                break

            if choice == "." and index < pages - 1:
                index += 1

            elif choice == "," and index > 0:
                index -= 1