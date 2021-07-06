class Node:
    
    def __init__(self, data="Head", next = None):
        self.data = data
        self.next = next


class LinnkedList:
    def __init__(self):
        self.head = Node()

    def insert_begin(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def print_func(self):
        if self.head.next == None:
            print('Empty List')
            return
        
        curr_node = self.head
        result = ''
        while curr_node != None:
            result = result + str(curr_node.data) + '-->'
            curr_node = curr_node.next
        print(result)





if __name__ == '__main__':
    llt = LinnkedList()
    llt.insert_begin(10)
    llt.insert_begin(20)
    llt.insert_begin(30)
    llt.print_func()
        