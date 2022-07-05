# Queues first in and first out FIFO
# example queue in movie ticket counter

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            return 
        if self.length == 1:
            self.first = None
            self.last = None
            self.length -= 1
            return 
        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.length -= 1
        return temp
    
    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

queue = Queue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
#print(queue.first.value)
#print(queue.last.value)
queue.dequeue()
queue.print_queue()
print('len', queue.length)


