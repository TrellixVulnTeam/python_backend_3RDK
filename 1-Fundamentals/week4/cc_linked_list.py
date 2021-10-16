class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.data)
            return

        currentnode = self.head
        while currentnode.next != None:
            currentnode = currentnode.next

        currentnode.next = new_node
        print("Appended new Node with value:", currentnode.next.data)

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.data)
            return

        new_node.next = self.head
        self.head = new_node

        print("Prepended new Head Node with value:", self.head.data)
        print("Node following head is:", self.head.next.data)

llist = LinkedList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")