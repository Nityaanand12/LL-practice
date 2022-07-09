class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

class BinarySearchTree:
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp.value == new_node.value:
                return False
            if new_node.value > temp.value:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
    
    def contains(self, value):
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            elif temp.value > value:
                temp = temp.left
            else:
                temp = temp.right
        return False
    
    def minimum(self, current_node):
        temp = current_node
        if temp is None:
            return False
        while temp.left:
            temp = temp.left
        return temp.value



BST = BinarySearchTree()
BST.insert(5)
BST.insert(7)
BST.insert(3)
BST.insert(2)
BST.insert(4)
print(BST.contains(12))
print(BST.minimum(BST.root.right))

# print(BST.root.value)
# print(BST.root.left.value)
# print(BST.root.right.value)
