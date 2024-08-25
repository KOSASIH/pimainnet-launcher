import re
from typing import Any, List, Dict

def validate_email(email: str) -> bool:
    """Validate an email address"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_password(password: str) -> bool:
    """Validate a password"""
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    return bool(re.match(pattern, password))

def validate_list_like(obj: Any) -> bool:
    """Validate if an object is list-like"""
    return isinstance(obj, (list, tuple))

def validate_dict_like(obj: Any) -> bool:
    """Validate if an object is dict-like"""
    return isinstance(obj, dict)

def validate_schema(data: Any, schema: Dict) -> bool:
    """Validate data against a schema"""
    for key, value in schema.items():
        if key not in data:
            return False
        if isinstance(value, dict):
            if not validate_schema(data[key], value):
                return False
        elif not isinstance(data[key], type(value)):
            return False
    return True

def validate_required_fields(data: Any, required_fields: List[str]) -> bool:
    """Validate if all required fields are present"""
    for field in required_fields:
        if field not in data:
            return False
    return True
