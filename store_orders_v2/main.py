# main.py
from models import Order, Delivery_Order, PickupOrder
from storage import load_orders, save_orders

orders = load_orders()

while True:
    print(
        "1 - добавить обычный заказ\n"
        "2 - добавить заказ с доставкой\n"
        "3 - добавить заказ самовывозом\n"
        "4 - показать все заказы\n"
        "5 - выйти"
    )

    choise = input("выбор: ")

    if choise == "1":
        customer_name = input("имя: ")
        total_price = input("Сумма заказа: ")
        orders.append(Order(customer_name, total_price))
        print()
    elif choise == "2":
        customer_name = input("имя: ")
        total_price = input("Сумма заказа: ")
        address = input("Адрес доставки: ")
        orders.append(Delivery_Order(customer_name, total_price, address))
        print("Заказ с доставкой добавлен")
        print()
    elif choise == "3":
        customer_name = input("имя: ")
        total_price = input("Сумма заказа: ")
        print("1 - Mega Park\n" "2 - Forum\n" "3 - Moskva")
        pickup = input("выберите место где зотите получить заказ: ")
        if pickup == "1":
            pickup_order = "Mega Park"
        elif pickup == "2":
            pickup_order = "Forum"
        elif pickup == "3":
            pickup_order = "Moskva"
        orders.append(PickupOrder(customer_name, total_price, pickup_order))
        print("Заказ с самовывозом добавлен")
        print()
    elif choise == "4":
        for order in orders:
            order.show_info()
            print()
    elif choise == "5":
        save_orders(orders)
        break
