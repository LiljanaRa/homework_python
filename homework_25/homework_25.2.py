def read_file(file: str) -> list[tuple[str, float, int]]:
    product_list = []
    try:
        with open(file, "r", encoding="UTF-8") as file:
            for line in file:
                name, price, quantity = line.strip("\n").split(",\t")
                product_list.append((name, float(price), int(quantity)))
    except FileNotFoundError:
        print("Файл не найден.")
    except ValueError:
        print("Неверный формат данных в файле")

    return product_list

def calculate_total_price(data: list[tuple[str, float, int]]) -> float:
    result = 0
    for name, price, quantity in data:
        result += price * quantity
    return result

product_list = read_file("products.txt")
total_price = calculate_total_price(product_list)

print(f"Общая стоимость продуктов: {total_price}")





