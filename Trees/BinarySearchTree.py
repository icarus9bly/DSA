class BinarySearchTree:
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
                    self.left = BinarySearchTree(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = BinarySearchTree(data)
        else:
            self.data = data
    
    def print_tree(self):
        # This is in-order traversal lnr(left node right)
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def inorder_traversal(self):
        result = []
        if self.data:
            if self.left:
                result.append(self.left.data)
            result.append(self.data)
            if self.right:
                result.append(self.right.data)
        # To be continued
        return result

    def lookup(self, value):
        if value == self.data:
            return f'{self.data} Found!'
        elif value > self.data:
            if self.right:
                return self.right.lookup(value)
            else:
                return f'{self.data} not found!'
        else:
            if self.left:
                return self.left.lookup(value)
            else:
                return f'{self.data} not found!'

    def __repr__(self):
        return f"{self.data}"

root = BinarySearchTree(56)
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
print(root.lookup(777))
print(root.inorder_traversal())
def depth_first_traversal(bt):
    result = []
    stacki = []
    stacki.append(bt)
    if stacki:
        current = stacki.pop()
        print(current)
        if current.right:
            stacki.append(current.right)
        if current.left:
            stacki.append(current.left)
    print(stacki)
depth_first_traversal(root)