# Recursion Traversal Method
def PreorderTraversal(self, node):
    if node == None:
        return
    print(node.value)
    self.PreorderTraversal(node.left)
    self.PreorderTraversal(node.right)

def InorderTraversal(self, node):
    global TempList
    if node == None:
        return
    self.InorderTraversal(node.left)
    print(node.value)
    # TempList.append(node.value)
    self.InorderTraversal(node.right)

def PostorderTraversal(self, node):
    if node == None:
        return
    self.PostorderTraversal(node.left)
    self.PostorderTraversal(node.right)
    print(node.value)

# def printTree(self, node):
#     # In order to traverse the binary tree and print
#     if node == None:
#         return
#     self.printTree(node.left)
#     print(node.val, end = ' ')
#     self.printTree(node.right)