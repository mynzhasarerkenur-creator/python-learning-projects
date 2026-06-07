from models import BankAccount
from storage import load_json, save_json


owners = load_json()

while True:
    print(
        '1 - создать счёт\n' \
        '2 - показать счета\n' \
        '3 - пополнить счёт\n' \
        '4 - снять деньги\n' \
        '5 - выйти'
    )

    choise = input('выбор: ')

    try:
        if choise == '1':
            owner = input('владелец:')
            owners.append(BankAccount(owner))
            print('счет успешно создан')
            print()
            save_json(owners)
        elif choise == '2':
            if not owners:
                print('еще нет зарегистрированных счетов')
            else:
                for owner in owners:
                    owner.show_info()
                    print('-'* 20)
        elif choise == '3':
            owner_input = input('владелец: ')
            user_found = False

            for owner in owners:
                if owner.owner == owner_input:
                    amount = int(input('введите сумму: '))
                    owner.deposit(amount)
                    user_found = True
                    save_json(owners)
                    break

            if not user_found:
                print("Пользователь не найден.")

        elif choise == '4':
            owner_input = input('владелец: ')
            user_found = False

            for owner in owners:
                if owner.owner == owner_input:
                    amount = int(input('введите сумму: '))
                    owner.withdraw(amount)
                    user_found = True
                    save_json(owners)
                    break

            if not user_found:
                print("Пользователь не найден.")
        elif choise == '5':
            save_json(owners) 
            break
    except ValueError:
        print("Сумма должна быть числом")
