# Напишите функцию, которая принимает на вход список чисел
# и возвращает сумму квадратов только четных чисел из списка,
# используя функциональные подходы (например, map, filter и reduce).

from functools import reduce

def even_square_sum(x,y):
            return x + y

nums = [int(i) for i in input("Введите числа, разделенные запятыми и пробелами: ").split(", ") if i.isdigit()]

even_nums = list(map(lambda x: x ** 2 if x % 2 == 0 else 0, nums))

result = reduce(even_square_sum ,even_nums)

print(f"Результат: {result}")