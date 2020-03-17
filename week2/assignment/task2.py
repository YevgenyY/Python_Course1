import json
from functools import wraps

def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        raw = func(*args, **kwargs)
        result = json.dumps(raw)
        return result
    return wrapper


@to_json
def get_data():
    return {
        'data': 42
    }
        
print(type(get_data()))
print(get_data())  # вернёт '{"data": 42}'
#get_data()

