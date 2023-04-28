#CREATING A STACK USING PYTHON:
items = []
class Stack(object):
    def __init__(self):
        self.item = []
    def isfull(self):
        if len(self.item) == n:
            return True
        else:
            return print("not full")
    def push(self,item):
        if self.isfull():
            return None
        else:
            self.item.append(item)
        print(self.item)
        pass
    def isempty(self):
        if self.item ==[]:
            return print("YES IT's EMPTY")
        else:
            return print("NO IT's not EMPTY")
        pass
    def pop(self):
        if self.item == []:
            return print("stack-underflow")
        else:
            self.item.pop()
        print(self.item)
        pass
    def peek(self):
        if self.item:
            return print("THE TOP ELEMENT IS",self.item[-1])
        else:
            return print("EMPTY")
        pass
    def size(self):
        if self.item:
            return print("the size of the stack is : ",len(self.item))
        else:
            return print(" Size is 0")
        pass
if __name__ == "__main__":
    stack = Stack()
    n = int(input("ENTER THE NO. of elements u want to enter"))
    y =3
    print("Push operation Enter 1")
    print("top operation Enter 2")
    print("pop operation Enter 3")
    print("size/No. of elements of the STACK Enter 4")
    print("is empty or not 5")
    print("is full or not 6")
    
    while y>0:
        x = int(input("Which operation: "))
        if x == 1:
            for i in range(0,n):
                ite=input("enter the element u want to push:")
                stack.push(ite)
            else:
                print("stack-overflow")
                    
        elif x == 2:
            stack.peek()
        elif x==3:
            stack.pop()
        elif x==4:
            stack.size()
        elif x==5:
            stack.isempty()
        elif x==6:
            stack.isfull()