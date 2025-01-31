from functools import reduce
from itertools import accumulate


def num_product(data):
    result = reduce(lambda x, y: x * y, data)

    acc_result = list(accumulate(data, lambda x, y: x * y))

    return f"Произведение всех чисел в списке: {result}\nНакопленные произведения: {acc_result}"


user_input = list(map(lambda x: int(x), input("Введите числа, разделенныe запятой и пробелом: ").split(", ")))

print(num_product(user_input))