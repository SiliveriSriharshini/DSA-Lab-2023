class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class bst:
    def create_node(self,data):
        return Node(data)

    def insert(self,node,data):
        if node is None:
            return self.create_node(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node

    def Inorder_traversal(self,root):
        if root is not None:
            self.Inorder_traversal(root.left)
            print(root.data)
            self.Inorder_traversal(root.right)

    def preorder_traversal(self,root):
        if root is not None:
            print(root.data)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self,root):
        if root is not None:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data)

    def delete(self,node,data):
        if node is None:
            return node
        if data<node.data:
            node.left=self.delete(node.left,data)
        elif data>node.data:
            node.right=self.delete(node.right,data)
        else:
            if node.left is None:
                temp=node.right
                node=None
                return temp
            elif node.right is None:
                temp=node.left
                node=None
                return temp
            else:
                temp=find_min(node.right)
                node.data=temp.data
                node.right=self.delete(node.right,temp.data)
        return node

def find_min(node):
    while node.left:
        node=node.left
    return node

#driver code
tree=bst()
root = tree.create_node(67)
tree.insert(root,100)
tree.insert(root,23)
tree.insert(root,200)
tree.insert(root,5)
print("INORDER TRAVERSAL")
tree.Inorder_traversal(root)
print("PREORDER TRAVERSAL")
tree.preorder_traversal(root)
tree.delete(root,5)
print("POSTORDER TRAVERSAL")
tree.postorder_traversal(root)
