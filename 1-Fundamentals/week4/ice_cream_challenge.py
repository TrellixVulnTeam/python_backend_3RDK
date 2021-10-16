class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)

    def show(self):
        return self.items

class IceCreamShoppe:
    def __init__(self, flavors:list):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, name, flavor, scoops):
        if flavor not in self.flavors:
            print(f"{flavor} isn't valid. Please select a valid flavor.")
            return
        if scoops < 1 or scoops > 3:
            print(f"{scoops} is not valid. Please select 1 -3 scoops.")
            return
        order = {"name": name, "flavor": flavor, "scoops": scoops}
        print("New order created.")
        self.orders.enqueue(order)

    def show_all_orders(self):
        for order in self.orders.show():
            print(order)

    def next_order(self):
        print("Next order up: ", self.orders.dequeue())

shop = IceCreamShoppe(['rocky_road', 'mint_chip', 'pistachio'])
shop.take_order("Zachary","pistachio", 3)
shop.take_order("Marcy","mint_chip", 1)
shop.take_order("Leopoad", "vanilla", 2)
shop.take_order("Bruce", "rocky_road", 0)
shop.show_all_orders()
print("-------------------------")
shop.next_order()
shop.show_all_orders()