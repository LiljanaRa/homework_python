import logging
from typing import Callable

logging.basicConfig(
    level=logging.INFO,
    filename="log.txt"
)


def log_args(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Аргументы: {args}, Результат: {result}")

        return result

    return wrapper


@log_args
def mul(a, b):
    return a * b


mul(5, 3)
mul(8, 9)