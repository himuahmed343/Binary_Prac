class Queue1:
    def __init__(self):
        self.queue1 = []

    def size1(self):
        print("Length of Queue :", len(self.queue1))

    def is_Empty(self):
        return self.queue1 == []

    def is_Full(self):
        return len(self.queue1) == self.size1

    def enqueue1(self, item1):
        if self.is_Full() != True:
            self.queue1.append(item1)
        else:
            print("Queue is full.")
        
    def dequeue1(self):
        if self.is_Empty() != True:
            self.queue1.pop(0)
        else:
            print("Queue is empty")

    def peek(self):
        if self.is_Empty() != True:
            print("Peak element :", self.queue1[0])
        else:
            print('Queue is Empty!')

    def display1(self):
        print("QUEUE : ", self.queue1)

myQueue = Queue1()
myQueue.enqueue1(4)
myQueue.enqueue1(5)
myQueue.enqueue1(6)
    
myQueue.display1()

myQueue.peek()

myQueue.dequeue1()
myQueue.dequeue1()

myQueue.display1()

myQueue.peek()

myQueue.display1()

myQueue.dequeue1()

myQueue.display1()

myQueue.size1()
myQueue.peek()