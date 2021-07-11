class Node:
    def __init__(self, data="Head", next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node()

    def add_beg(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def add_last(self, data):
        new_node = self.head
        while new_node.next:
            new_node = new_node.next
        
        node = Node(data, None)
        new_node.next = node

    def get_len(self):
        count = 0
        node = self.head.next
        while node != None:
            node = node.next
            count = count + 1
        return count

        
    def insert_at(self, location, data):
        if self.head.next == None:
            print('Empty')
            return
        
        if location<0 and location>self.get_len():
            print('Invalid Position')
            return
        
        count = 0
        new_node = self.head
        while new_node != None:
            if count == location -1:
                # print("Get the location of Linked list")
                node = Node(data, new_node.next)
                new_node.next = node
                

            count = count + 1
            new_node = new_node.next


    def search_ll(self, data):
        new_node = self.head
        while new_node != None:
            if new_node.data == data:
                print('Data Found Bro')
            # else:
            new_node = new_node.next

        print('Data Not Found Bro')
            

        
        
    def remove(self, data):
        new_node = self.head
        while new_node != None:
            if new_node.data == data:
                new_node = Node(data, None)
                return

            new_node = new_node.next

            
        

        

    def print_func(self):
        if self.head.next == None:
            print('Empty String')
        
        new_node = self.head
        result = ''
        while new_node != None:
            result = result + str(new_node.data) + '-->'
            new_node = new_node.next
        print(result)


ll = LinkedList()
ll.add_beg(5)
ll.add_beg(15)
ll.add_beg(25)
ll.print_func()

ll.add_last(35)
ll.add_last(45)
ll.add_last(55)
ll.print_func()


ll.insert_at(2, 100)
ll.insert_at(5, 50)
print(ll.get_len())
ll.print_func()



ll.search_ll(6)
ll.insert_at(9, 60)
ll.print_func()
print(ll.get_len())


ll.remove(55)
ll.print_func()
print(ll.get_len())






        

        
        

        