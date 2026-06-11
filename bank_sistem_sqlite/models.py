class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def show_info(self):
        print(f"владелец: {self.owner}")
        print(f"баланс: {self.balance}")

    def deposit(self, amout):
        if amout > 0:
            self.balance += amout
            print(f"ваш счет пополнен на {amout}тг")
            print(f"баланс: {self.balance}тг")

    def withdraw(self, amout):
        if amout > 0:
            if amout > self.balance:
                print(f"недостаточно средств, ваш баланс: {self.balance}тг")
            else:
                self.balance -= amout
                print(f"Из вашего баланса снято {amout}тг")
                print(f"Ваш баланс:{self.balance}")
