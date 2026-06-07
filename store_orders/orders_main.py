import json


class Order:
    def __init__(self, customer_name, total_price):
        self.customer_name = customer_name
        self.total_price = total_price

    def show_info(self):
        print(f"Клиент: {self.customer_name}")
        print(f"Сумма заказа: {self.total_price}")

    def to_dict(self):
        return {"customer_name": self.customer_name, "total_price": self.total_price}


class Delivery_Order(Order):
    def __init__(self, customer_name, total_price, address):
        super().__init__(customer_name, total_price)
        self.address = address

    def show_info(self):
        super().show_info()
        print(f"Адрес доставки: {self.address}")

    def to_dict(self):
        dat = super().to_dict()
        dat["address"] = self.address
        return dat


class PickupOrder(Order):
    def __init__(self, customer_name, total_price, pickup_order):
        super().__init__(customer_name, total_price)
        self.pickup_order = pickup_order

    def show_info(self):
        super().show_info()
        print(f"Пункт выдачи: {self.pickup_order}")

    def to_dict(self):
        dat = super().to_dict()
        dat["pickup_order"] = self.pickup_order
        return dat


def load_orders():
    orders = []
    try:
        with open("store_orders/orders.json", "r") as files:
            orders_data = json.load(files)
            for data in orders_data:
                if "address" in data:
                    orders.append(
                        Delivery_Order(
                            data["customer_name"], data["total_price"], data["address"]
                        )
                    )
                elif "pickup_order" in data:
                    orders.append(
                        PickupOrder(
                            data["customer_name"],
                            data["total_price"],
                            data["pickup_order"],
                        )
                    )
                else:
                    orders.append(Order(data["customer_name"], data["total_price"]))
    except (FileNotFoundError, json.JSONDecodeError):
        orders = []
    return orders


def save_orders():
    orders_data = []
    for order in orders:
        orders_data.append(order.to_dict())
    with open("store_orders/orders.json", "w") as files:
        json.dump(orders_data, files, indent=4)


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
        save_orders()
        break
