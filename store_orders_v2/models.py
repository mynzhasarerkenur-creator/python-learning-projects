#models.py
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