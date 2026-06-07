#models
class BankAccount():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        
    def show_info(self):
        print(f'владелец: {self.owner}')
        print(f'баланс: {self.balance}')

    def to_dict(self):
        return {'owner': self.owner, 'balance': self.balance }

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'ваш счет пополнен на {amount}tg')
            print(f'баланс: {self.balance}tg')
        else: 
            print('Сумма должна быть положительной!')
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f'из вашего счета снято {amount}tg')
                print(f'баланс: {self.balance}tg')
            else:
                print("Недостаточно средств")
        else:
            print('Сумма должна быть положительной!')
    