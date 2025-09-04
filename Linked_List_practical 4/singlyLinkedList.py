class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        if elements:
            print(" -> ".join(map(str, elements)))
        else:
            print("List is empty")



    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        if current is None:
            raise IndexError("Position out of range")
        new_node.next = current.next
        current.next = new_node


    def delete(self, data):
        if not self.head:
            return False
        if self.head.data == data:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        return False


    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.insert(4, 1)
ll.delete(2)
print(ll.search(4))  # Output: 1
print(ll.search(5))  # Output: -1
ll.reverse()
ll.display()  # Output: 3 -> 4 -> 1





        




