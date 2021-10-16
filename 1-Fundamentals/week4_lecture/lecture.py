# print("------------------------------------------------------------")
# print("------------Class and Object Oriented Language--------------")
# print("------------------------------------------------------------")
# class Vehicle:
#     def __init__(self, num_wheels, color):
#         self.num_wheels = num_wheels
#         self.color = color
#         self.fuel_percent = 0

#     def add_fuel(self, amount):
#         self.fuel_percent += amount
#         if self.fuel_percent > 100:
#             self.fuel_percent = 100

# motorcycle = Vehicle(2, 'black')

# print(motorcycle)
# print(motorcycle.color)
# print(motorcycle.fuel_percent)

# print("------------------------------------------------------------")
# print("-----------------------Class Inheritance 1--------------------")
# print("------------------------------------------------------------")
# class Vehicle:
#     def __init__(self, num_wheels, color):
#         self.num_wheels = num_wheels
#         self.color = color
#         self.fuel_percent = 0

# class Truck(Vehicle):
#     def __init__(self, num_wheels, color, num_doors):
#         super().__init__(num_wheels, color)
#         self.num_doors = num_doors

# print("------------------------------------------------------------")
# print("-----------------------Class Inheritance 2------------------")
# print("------------------------------------------------------------")
# class Parent:
#     def fold_shirt(self):
#         print("Parent Fold Shirt")

# class Child(Parent):
#     def fold_shirt(self):
#         print("Child Fold Shirt")

#     def fold_shirt_at_home(self):
#         super().fold_shirt()

# mother = Parent()
# child = Child()
# mother.fold_shirt()
# child.fold_shirt()
# child.fold_shirt_at_home()

# print("------------------------------------------------------------")
# print("-----------------------Link List----------------------------")
# print("------------------------------------------------------------")
# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

#     def __str__(self):
#         return str(self.data)

# class DoubleLinkList(Node):
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def append(self, data): 
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node

#     def print_list(self):
#         cur = self.head
#         while cur:
#             print(cur.data)
#             cur = cur.next

#     def remove(self, data):
#         cur = self.head
#         while cur:
#             if cur.data == data:
#                 if cur == self.head:
#                     self.head = cur.next
#                 elif cur == self.tail:
#                     self.tail = cur.prev
#                 else:
#                     cur.prev.next = cur.next
#                     cur.next.prev = cur.prev
#                 return
#             cur = cur.next
#     def remove_duplicate(self):
#         cur = self.head
#         while cur:
#             if cur.next:
#                 if cur.next.data == cur.data:
#                     cur.next = cur.next.next
#                     if cur.next:
#                         cur.next.prev = cur.prev
#                 else:
#                     cur = cur.next
#             else:
#                 return

# print("------------------------------------------------------------")
# print("-----------------------Stack--------------------------------")
# print("------------------------------------------------------------")
# class Stack:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()

#     def peek(self):
#         return self.items[len(self.items)-1]

#     def size(self):
#         return len(self.items)

# print("------------------------------------------------------------")
# print("-----------------------Conditional Expressions--------------")
# print("------------------------------------------------------------")
# num = 5
# result = "Pass" if num == 5 else "Fail"

# print("------------------------------------------------------------")
# print("-----------------------Queue--------------------------------")
# print("------------------------------------------------------------")
# class Queue():
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def enqueue(self, item):
#         self.items.insert(0, item)

#     def dequeue(self):
#         return self.items.pop()

#     def size(self):
#         return len(self.items)