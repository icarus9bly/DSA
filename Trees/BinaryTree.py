class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = BinaryTree(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = BinaryTree(data)
        else:
            self.data = data
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
            
    def lookup(self, val):
        if val > self.data:
            pass
        elif val < self.data:
            pass
        else:
            pass


    def __repr__(self):
        return f"{self.data}"

root = BinaryTree(56)
# root.left = BinarySearchTree(45)
# root.right = BinarySearchTree(789)
root.insert(45)
root.insert(51)
root.insert(556)
root.insert(777)
root.insert(789)

print(root)
print(root.right)
print("*"*100)
root.print_tree()