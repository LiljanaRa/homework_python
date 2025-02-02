from typing import Callable


def validate_args(*expected_types):
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, expected_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Аргумент {arg} имеет неправильный тип {type(arg)}. Ожидается {expected_type}.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_args(str, int)
def greet(name, age):
    print(f"Привет, {name}! Тебе {age} лет.")

greet("Tom", 25)