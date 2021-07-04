class Queue(object):
    def __init__(self, size):
        self.queue = []
        self.size = size

    def __str__(self):
        myString = ','.join(str(i) for i in self.queue)
        return myString

    def enqueue(self, item):
        '''This function adds an item to the rear end of the queue '''
        if(self.isFull() != True):
            self.queue.append(item)
        else:
            print('Queue is Full!')

    def dequeue(self):
        ''' This function removes an item from the front end of the queue '''
        if(self.isEmpty() != True):
            return self.queue.pop()
        else:
            print('Queue is Empty!')

    def isEmpty(self):
        ''' This function checks if the queue is empty '''
        return self.queue == []

    def isFull(self):
        ''' This function checks if the queue is full '''
        return len(self.queue) == self.size

    def peek(self):
        ''' This function helps to see the first element at the fron end of the queue '''
        if(self.isEmpty() != True):
            return self.queue[-1]
        else:
            print('Queue is Empty!')
            

myQueue = Queue()
myQueue.enqueue(4)
myQueue.enqueue(5)
myQueue.enqueue(6)
    
print(myQueue)
    
# myQueue.enqueue(1)
# myQueue.enqueue(2)
# myQueue.enqueue(3)
    
# print(myQueue)
    
# myQueue.dequeue()
    
# print(myQueue)







class Queue():
    def __init__(self, size):
        self.queue = []
        self.size = size


    def __str__(self):
        myString = ','.join(str(i) for i in self.queue)
        return myString


    def enqueue(self, item1):
        if(self.is_Full() != True):
            self.queue.append(item1)
        else:
            print("Queue is full.")
        
    def dequeue(self):
        if (self.is_Empty() != True):
            self.queue.pop()
        else:
            print("Queue is empty")


    def is_Empty(self):
        return self.queue == []

    def is_Full(self):
        return len(self.queue) == self.size



    def peek(self):
        if (self.is_Empty() != True):
           return self.queue[-1]
        else:
            print('Queue is Empty!')


myQueue = Queue(10)
myQueue.enqueue(4)
myQueue.enqueue(5)
myQueue.enqueue(6)
print(myQueue)
# myQueue.display1()