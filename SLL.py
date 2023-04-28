class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def insert_begin(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode

    def insert_end(self, newdata):
        newnode = Node(newdata)
        if self.head is None:
            self.head = newnode
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = newnode

    def add_after_key(self, key, newdata):
        if self.head is None:
            return

        current = self.head
        while current is not None:
            if current.data == key:
                newnode = Node(newdata)
                newnode.next = current.next
                current.next = newnode
                return
            current = current.next

    def insert_middle(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        newnode = Node(newdata)
        newnode.next = middle_node.next
        middle_node.next = newnode

    def remove_node(self, Removekey):
        HeadVal = self.head

        if HeadVal is not None:
            if HeadVal.data == Removekey:
                self.head = HeadVal.next
                HeadVal = None
                return

        prev = None
        while HeadVal is not None:
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if HeadVal is None:
            return

        prev.next = HeadVal.next
        HeadVal = None

    def traverse(self):
        currentval = self.head
        while currentval is not None:
            print(currentval.data, end=' ')
            currentval = currentval.next
        print()


if __name__ == "__main__":
    llist = SLinkedList()
    llist.insert_begin(5)
    llist.insert_end(6)
    llist.insert_begin(7)
    llist.insert_end(8)
    llist.traverse()
    print("deletion")
    llist.remove_node(6)
    llist.traverse()
    print("llist after adding a new value")
    llist.insert_begin(6)
    llist.insert_end(10)
    llist.insert_middle(llist.head.next.next, 2)
    llist.add_after_key(2, 3)
    llist.traverse()
