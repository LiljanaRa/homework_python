# Напишите функцию, которая принимает на вход список функций и значение,
# а затем применяет композицию этих функций к значению, возвращая конечный результат.

from functools import reduce


def compose_functions(funcs, x):
    return reduce(lambda acc, func: func(acc), funcs, x)

add_one = lambda x: x + 1
double = lambda x: x * 2
subtract_three = lambda x: x - 3

functions = [add_one, double, subtract_three]

result = compose_functions(functions, 5)

print(f"Конечный результат: {result}")