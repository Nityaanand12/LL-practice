# Queues last in and last out LILO
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
            new_node.next = self.first
            self.first = new_node
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
        while temp.next:
            previous = temp
            temp = temp.next
        previous.next = None
        self.last = previous
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


