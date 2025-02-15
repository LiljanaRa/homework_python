class Counter:
    def __init__(self, value: int = 0):
        self.value = value

    def __add__(self, other):
        self.value += other
        return self

    def __sub__(self, other):
        self.value -= other
        return self

    def __str__(self) -> str:
        return f"Значение счетчика: {self.value}"

    def __int__(self):
        return self.value


counter = Counter(8)

counter += 2

print(counter)

counter -= 10

print(int(counter))