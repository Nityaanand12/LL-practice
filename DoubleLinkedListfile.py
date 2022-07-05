class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoubleLinkedList:
    
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
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        if self.length == 0:
            self.append(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
    
    def get(self, index):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        if index <0 or index > self.length -1:
            return 
        elif index <= self.length -1:
            temp = self.get(index)
            temp.value = value 
    
    def pop(self):
        if self.length == 0:
            return 
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.tail
            previous = self.tail.prev
            temp.prev = None
            previous.next = None
            self.tail = previous
        self.length -= 1
        return temp
    
    def popfirst(self):
        if self.length == 1:
            return self.pop()
        elif self.length >1:
            temp = self.head
            next_val = self.head.next
            next_val.prev = None
            self.head = next_val
            self.length -= 1
            return temp
        else:
            return None
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return 
        elif (0 < index <= self.length -1):
            new_node = Node(value)
            previous = self.get(index -1)
            temp = self.get(index)
            previous.next = new_node
            new_node.prev =previous
            new_node.next = temp
            temp.prev = new_node
            self.length += 1
        elif index == 0:
            self.prepend(value)
    
    def remove(self, index):
        if self.length > 0:
            if index == 0:
                self.popfirst()
            elif index == self.length -1:
                self.pop()
            elif 0<index<self.length-1:
                previous = self.get(index-1)
                temp = self.get(index)
                nextvalue = self.get(index + 1)
                previous.next = nextvalue
                nextvalue.prev = previous
                self.length -= 1
                return temp
        else:
            return
    
    
    def reverse(self):
        temp = self.head
        after = self.head
        before = None
        self.head = self.tail
        self.tail = temp
        while after:
            after = after.next
            temp.next = before
            temp.prev = after
            before = temp
            temp = after
        
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


mydll = DoubleLinkedList(4)
mydll.append(5)
mydll.append(6)
mydll.insert(2,1)
mydll.insert(3,5)
mydll.remove(5)
# print(mydll.popfirst())
# print(mydll.popfirst())
# print(mydll.popfirst())
# mydll.append(6)
# mydll.prepend(7)
# mydll.set_value(2, 2)
# print(mydll.get(4))
mydll.print_list()
print("++++")
mydll.reverse()
#print(mydll.pop())
#print(mydll.pop())
# print(mydll.head.value)
# print(mydll.head.prev)
# print(mydll.head.next.value)
# print("------")
# print(mydll.tail.value)
# print(mydll.tail.prev.value)
# print(mydll.tail.next)

mydll.print_list()

        
        
