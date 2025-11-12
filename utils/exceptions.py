from utils.rich_ui import console
from rich.panel import Panel

def throw_exception(expc_code: int):
    if(expc_code == 1):
        console.print(Panel("E001 - Not a valid menu..."))