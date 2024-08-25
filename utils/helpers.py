import re
import json
import base64
from datetime import datetime, timedelta
from typing import Any, List, Dict, Union

def camel_case_to_snake_case(s: str) -> str:
    """Convert camelCase to snake_case"""
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

def snake_case_to_camel_case(s: str) -> str:
    """Convert snake_case to camelCase"""
    return ''.join(word.capitalize() for word in s.split('_'))

def json_dumps(data: Any, indent: int = 4) -> str:
    """Dump JSON data with indentation"""
    return json.dumps(data, indent=indent)

def json_loads(data: str) -> Any:
    """Load JSON data from string"""
    return json.loads(data)

def base64_encode(data: str) -> str:
    """Base64 encode a string"""
    return base64.b64encode(data.encode()).decode()

def base64_decode(data: str) -> str:
    """Base64 decode a string"""
    return base64.b64decode(data.encode()).decode()

def format_datetime(dt: datetime, format: str = '%Y-%m-%d %H:%M:%S') -> str:
    """Format a datetime object"""
    return dt.strftime(format)

def parse_datetime(s: str, format: str = '%Y-%m-%d %H:%M:%S') -> datetime:
    """Parse a datetime string"""
    return datetime.strptime(s, format)

def get_current_timestamp() -> int:
    """Get the current timestamp in seconds"""
    return int(datetime.now().timestamp())

def get_current_datetime() -> datetime:
    """Get the current datetime object"""
    return datetime.now()

def get_future_timestamp(seconds: int) -> int:
    """Get a future timestamp in seconds"""
    return get_current_timestamp() + seconds

def get_future_datetime(seconds: int) -> datetime:
    """Get a future datetime object"""
    return get_current_datetime() + timedelta(seconds=seconds)

def is_list_like(obj: Any) -> bool:
    """Check if an object is list-like"""
    return isinstance(obj, (list, tuple))

def is_dict_like(obj: Any) -> bool:
    """Check if an object is dict-like"""
    return isinstance(obj, dict)

def merge_dicts(dict1: Dict, dict2: Dict) -> Dict:
    """Merge two dictionaries"""
    return {**dict1, **dict2}

def get_nested_value(obj: Union[Dict, List], path: str) -> Any:
    """Get a nested value from a dictionary or list"""
    path_parts = path.split('.')
    current = obj
    for part in path_parts:
        if isinstance(current, dict):
            current = current.get(part)
        elif isinstance(current, list):
            current = current[int(part)]
        if current is None:
            break
    return current
