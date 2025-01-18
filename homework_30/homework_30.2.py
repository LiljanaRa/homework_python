class  BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return f"Баланс обновлен. Новый баланс: {self.__balance}"

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            return f"Баланс обновлен. Новый баланс: {self.__balance}"
        else:
            return "Недостаточно средств на счете"

bank_acc = BankAccount("e0476t5464", 1835)

#print(bank_acc.deposit(520))
#print(bank_acc.withdraw(1513))
print(bank_acc.withdraw(2562))