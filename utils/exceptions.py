from rich.panel import Panel

def throw_exception(expc_code: int):
    from utils.rich_ui import console
    try: 
        if(expc_code == 1):
            return "E001 - Not a valid menu..."
        if(expc_code == 2):
            return "E002 - Escape key not valid..."
    except:
        return "Unhandled Exception."