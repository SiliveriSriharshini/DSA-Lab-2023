class queue: # Create a class queue
    def __init__(self, max_size, size=0, front= -1, rear= -1):
        self.queue = [[] for i in range(max_size)]
        self.max_size = max_size
        self.size = size
        self.front = front
        self.rear = rear
 
    # Methods of Queue
    
    def enqueue(self, data):
        if self.isFull():
            print("OVERFLOW")
        else:
            if(self.front == -1 & self.rear == -1):
                self.front = 0
                self.rear = 0
                self.queue[self.rear] = data
            else:
                self.rear += 1
                self.queue[self.rear] = data
            self.size += 1
 
    def dequeue(self):
        if self.isEmpty():
            print("UNDERFLOW")
        else:
            data = self.queue[self.front]
            if (self.front == self.rear):
                self.front = -1
                self.rear = -1
            else:
                data = self.queue[self.front]
                front = self.front + 1
            print(self.queue[self.front], 'is removed')
            self.size -= 1
    def isEmpty(self): # To check if the current queue is empty or not
        if self.size == 0:
            return self.front == -1 & self.rear == -1
    def isFull(self): # To check if the current queue is full or not
        if self.rear == self.max_size:
            return "queue is full"
    def show(self):
        print ('Queue contents are:')
        for i in range(self.size):
            print (self.queue[int((i+self.front)% self.max_size)])
q = queue(5)
print('Queue Insertion')
q.enqueue(1)
q.show()
q.enqueue(2)
q.show()
q.enqueue(3)
q.show()
q.enqueue(4)
q.show()
q.enqueue(5)
q.show()
print('Queue Deletion')
q.dequeue()
q.show()
q.dequeue()
q.show()
q.dequeue()
q.show()
q.dequeue()
q.show()
q.dequeue()
q.show()