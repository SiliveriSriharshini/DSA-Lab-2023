class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_after(self, data, after_data):
        if self.head is None:
            print("List is empty")
            return
        new_node = Node(data)
        current = self.head
        while current.next != self.head:
            if current.data == after_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        if current.data == after_data:
            new_node.next = current.next
            current.next = new_node
            return
        print(after_data, "not found in the list")

    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        prev = None
        while current.next != self.head:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    while current.next != self.head:
                        current = current.next
                    current.next = self.head.next
                    self.head = self.head.next
                return
            prev = current
            current = current.next
        if current.data == data:
            if prev:
                prev.next = current.next
            else:
                self.head = None
            return
        print(data, "not found in the list")

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=' ')
            current = current.next
            if current == self.head:
                break
        print()
#driver code
cll=CircularLinkedList()
cll.insert_begin(10)
cll.insert_begin(25)
cll.insert_begin(30)
cll.insert_after(15,10)
cll.insert_end(50)
cll.traverse()
print("deletion")
cll.delete(25)
cll.delete(30)
cll.traverse()
print("inserting")
cll.insert_after(55,15)
cll.insert_begin(35)
cll.insert_begin(23)
cll.insert_end(20)
cll.traverse()