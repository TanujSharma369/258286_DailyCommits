class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end='')
                temp = temp.next


list = LinkedList()
list.insert(5)
list.insert(4)
list.insert(6)
list.insert(3)
list.insert(7)
list.display()