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

    def bfs(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while queue:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return results

    def dfs_Preorder(self):
        results = []
        def traversal(current_node):
            results.append(current_node.value)
            if current_node.left:
                traversal(current_node.left)
            if current_node.right:
                traversal(current_node.right)
        traversal(self.root)
        return results


    def dfs_postorder(self):
        results = []
        def traversal(current_node)
            if current_node.left:
                traversal(current_node.left)
            if current_node.right:
                traversal(current_node.right)
            result.append(current_node.value)
        traversal(self.root)
        return results

    def dfs_inorder(self):
        results = []
        def traversal(current_node)
            if current_node.left:
                traversal(current_node.left)
            result.append(current_node.value)
            if current_node.right:
                traversal(current_node.right)
        traversal(self.root)
        return results

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
