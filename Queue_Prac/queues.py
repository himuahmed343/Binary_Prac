class Queue:
    def __init__(self):
        self.queue = []
        # self.size = size

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.queue == []

    def isFull(self):
        return len(self.queue) == self.size

    def enqueue(self, item):
        if self.isFull() != True:
            self.queue.append(item)
        else:
            print("Queue is full.")
        
    def dequeue(self):
        if self.isEmpty() != True:
            self.queue.pop(0)
        else:
            print("Queue is empty")

    def peek(self):
        if self.isEmpty() != True:
            print("Peek element :", self.queue[0])
        else:
            print('Queue is Empty!')

    def display(self):
        print("QUEUE : ", self.queue)


myQueue = Queue()
myQueue.enqueue(4)
myQueue.enqueue(5)
myQueue.enqueue(6)
    
myQueue.display()

myQueue.peek()

myQueue.dequeue()
myQueue.dequeue()

myQueue.display()

myQueue.peek()

myQueue.display()

myQueue.dequeue()

myQueue.display()

myQueue.peek()