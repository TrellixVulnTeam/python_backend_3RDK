class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)

    def show(self):
        return self.items

class IceCreamShop:
    def __init__(self, flavors:list):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print("Sorry, we don't have that flavor.")
            return
        if scoops < 1 and scoops > 3:
            print("Choose between 1 - 3 scoops")
            return
        order = {
            "Customer": customer,
            "Flavor": flavor,
            "Scoops": scoops
        }
        print("Order created!")
        self.orders.enqueue(order)

    def show_all_orders(self):
        for order in self.orders.show():
            print(order)

    def next_order(self):
        print("Next order up: ", self.orders.dequeue())

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()