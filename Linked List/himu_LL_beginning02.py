class Node:
    def __init__(self, data = "Head", next = None):
        self.data = data
        self.next = next
    

class LinkedList:
    def __init__(self):
        self.head = Node()
    

    def add_at_begin(self, data):
        node = Node(data, self.head.next)
        self.head.next = node
    
    def print_func(self):
        if self.head.next == None:
            print("Empty List")
            return

        new_node = self.head
        res_str = ''
        while new_node != None:
            res_str = res_str + str(new_node.data) + "==>"
            new_node = new_node.next
        print(res_str)


ll = LinkedList()
ll.add_at_begin(10)
ll.add_at_begin(25)
ll.print_func()

        

        