class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def reverse(self):
        
        temp = self.head
        before = None
        after = self.head
        self.head = self.tail
        self.tail = temp
        while after:
            after = after.next
            temp.next = before
            before = temp
            temp = after
            
            

mylinkedlist = LinkedList(1)
mylinkedlist.append(2)
mylinkedlist.append(3)
mylinkedlist.reverse()
mylinkedlist.print_list()

print(mylinkedlist.head.value)
print(mylinkedlist.tail.value)
print(mylinkedlist.head.next)
print(mylinkedlist.tail.next)
        
