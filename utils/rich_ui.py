from typing import List, Tuple
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich import box
from rich.prompt import Prompt

console = Console()

# Makes a header
def make_panel(title: str,subtitle: str = "", color: str = "bright_blue"):
    text = f"[bold cyan]{title}[/bold cyan]"
    if(subtitle):
        text += f"\n[dim]{subtitle}[/dim]"
    return Panel.fit(text, border_style=color)


# Makes a menu
def make_menu(title: str, items: List[Tuple[str, str]], border_color: str = "bright_magenta") -> Table:
    menu = Table(
        title=f"[bold yellow]{title}[/bold yellow]",
        title_style="bold yellow",
        box=box.DOUBLE_EDGE,
        border_style=border_color,
        show_header=False,
        padding=(0, 2)
    )
    for key, desc in items:
        menu.add_row(f"[green]{key}[/green]", desc)
    return menu


# Centers the drawn consoles
def display_centered(panel_or_table):
    console.print(Align.center(panel_or_table))


# Waits for user input
def pause():
    console.input("\n[dim]Press Enter to continue...[/dim]")

# Default Menu for CRUD (employees, clients and appointments). This is a template.
def crud_menu(title: str, subtitle: str, items: List[Tuple[str, str]], border_color: str = "bright_green"):
    while True:
        try:
            # Manage the header and prompt
            console.clear()
            display_centered(make_panel(title, subtitle))
            menu = make_menu(title, items, border_color)
            display_centered(menu)
            display_centered("[bold white]Select an option[/bold white]")

            # Get user choice
            choice = Prompt.ask(
                "\n[bold bright_cyan]Enter your choice[/bold bright_cyan]",
                choices=[key for key, _ in items] + ["b", "B"],
                default="B"
            ).upper()

            console.clear()

            # Handle user input
            if(choice == "B"):
                console.print(Panel("[bright_red]Returning to main menu...[/bright_red]"))
                break
                console.print(Panel(throw_exception(2)))

            # "send" the info back to the menu
            yield choice
        except Exception as e:
            console.print(Panel(f"[red]Unhandled exception: {e}[/red]"))
            pause()
