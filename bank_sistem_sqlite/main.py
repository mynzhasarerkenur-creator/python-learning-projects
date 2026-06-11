from models import BankAccount
import storage

storage.create_table()
while True:
    print("________BANK_SISTEM________")
    print("1. create account")
    print("2. show account")
    print("3. deposite ")
    print("4. withdraw")
    print("5. exit")

    choise = input("your choise: ")

    if choise == "1":
        owner_input = input("владелец: ")
        new_accout = BankAccount(owner=owner_input)
        storage.save_account(new_accout)
    elif choise == "2":
        accounts = storage.get_account()
        for account in accounts:
            print(account)
    elif choise == "3":
        try:
            owner = input("владелец: ")
            amount = float(input("сумма: "))

            if amount <= 0:
                print("сумма должно быть больше нуля")
            else:
                success, old_balance, new_balance = storage.deposit_account(
                    owner, amount
                )
                if success:
                    print(f"баланс пополнен на {amount}tg")
                    print(f"ваш баланс: {new_balance}")
                else:
                    print("пользователь не найден")
        except ValueError:
            print("введите корректное число")

    elif choise == "4":
        try:
            owner = input("владелец: ")
            amount = float(input("сумма: "))
            if amount <= 0:
                print("сумма должно быть больше нуля")
            else:
                status, old_balance, new_balance = storage.withdraw_account(
                    owner, amount
                )

                if status == "success":
                    print(f"снято: {amount}tg")
                    print(f"было: {old_balance}tg")
                    print(f"стало: {new_balance}tg")

                elif status == "not_enough_money":
                    print("недостаточно средств")
                    print(f"ваш баланс: {old_balance}tg")

                elif status == "not_found":
                    print("пользователь не найден")

        except ValueError:
            print("введите корректное число")
    elif choise == "5":
        print("Gud bye! ")
        break
