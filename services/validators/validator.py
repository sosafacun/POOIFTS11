from datetime import datetime

#exception thrower to catch any non-filled fields
def require(value: str, field_name: str):
    if not value or not value.strip():
        raise ValueError(f"{field_name} is required!")
    return value.strip()

def require_date(value: str, field_name: str):
    is_present=_require(value, field_name)
    try:
        return datetime.strptime(cleaned, "%Y-%m-%d").date().isoformat() #I just copypasted this from stackoverflow. I *HATE* working with dates.
    except ValueError as e:
        raise ValueError(f"{field_name} must be in YYYY-MM-DD")