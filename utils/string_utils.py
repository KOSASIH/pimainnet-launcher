import re

def slugify(s: str) -> str:
    """Convert a string to a slug"""
    s = re.sub(r'[^\w\s-]', '', s).strip().lower()
    return re.sub(r'[\s]+', '-', s)

def truncate(s: str, length: int = 100) -> str:
    """Truncate a string to a maximum length"""
    if len(s) > length:
        return s[:length] + '...'
    return s
