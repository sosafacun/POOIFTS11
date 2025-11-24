from datetime import datetime

#exception thrower to catch any non-filled fields
def require(value: str, field_name: str):
    if not value or not value.strip():
        raise ValueError(f"{field_name} is required!")
    return value.strip()

def require_date(value: str, field_name: str):
    value = require(value, field_name)  # reuse the existing validation

    try:
        parsed = datetime.strptime(value, "%Y-%m-%d")
        return parsed.date().isoformat()
    except ValueError:
        raise ValueError(f"{field_name} must be in YYYY-MM-DD format")