#storage.py
import json
from models import Order, Delivery_Order, PickupOrder
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


def save_orders(orders):
    orders_data = []
    for order in orders:
        orders_data.append(order.to_dict())
    with open("store_orders/orders.json", "w") as files:
        json.dump(orders_data, files, indent=4)
