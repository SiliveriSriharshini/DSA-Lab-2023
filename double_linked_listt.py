class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data
class Dlinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_begin(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    def add_after(self, prev_node, new_data):
        if prev_node is None:
            print("This node doesn't exist in DLL")
            return
        new_node = Node(data=new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node
    def add_end(self, new_data):
        new_node = Node(data=new_data)
        last = self.head
        new_node.next = None
        # 4. If the Linked List is empty, then
        # make the new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        # 5. Else traverse till the last node
        while (last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last
    def printList(self, node):

        print("\nTraversal in forward direction")
        while node:
            print("{}".format(node.data), end =" ")
            last = node
            node = node.next
        print("\nTraversal in reverse direction")
        while last:
            print("{}".format(last.data), end =" ")
            last = last.prev
    def delete_begin(self):
        if self.head == None:
            print('list is empty')
            return
        else:
            curr_node = self.head
            curr_node.next.prev = None
            self.head = curr_node.next
            curr_node.next = None
            return curr_node.data 
    def delete_End(self): 
        if(self.head == None):
            return
        else:
            lastnode = self.head
            while (lastnode.next is not None):
                lastnode = lastnode.next
            temp = lastnode
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev=None
            return temp.data
    def delete(self, value):
        # Delete a specific item
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False

        elif current.data == value:
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.data == value:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
                if current.data == value:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next


if __name__ == "__main__":
    myDLL = Dlinkedlist()
    myDLL.add_begin(6)
    myDLL.add_end(7)
    myDLL.add_end(4)
    myDLL.add_after(myDLL.head.next,8)
    print('created DLL is :', end = ' ')
    myDLL.printList(myDLL.head)
    myDLL.delete_begin()
    myDLL.delete_End()
    print('created DLL is :', end = ' ')
    myDLL.printList(myDLL.head)
    myDLL.delete(8)
    print('created DLL is :', end = ' ')
    myDLL.printList(myDLL.head)



    