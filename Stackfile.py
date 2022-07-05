# stacks last in and first out LIFO
# example tennis balls in glass jar

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1
        
    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return 
        else:
            temp = self.top.next
            self.top = temp
            self.length -= 1
    
    def print_list(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

stack = Stack(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.pop()
stack.print_list()


