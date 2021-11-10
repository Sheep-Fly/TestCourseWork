# Rotation left/right
def left_rotate(self, node):
    parent = node.parent
    right = node.right

    # Step 1: Assign the left child node of the right child node to the right node
    node.right = right.left
    if node.right:
        node.right.parent = node

    # Step 2: Turn this node into the left child node of its right child node
    right.left = node
    node.parent = right

    # Step 3: The child node of the right child node becomes the parent node of the original node
    right.parent = parent
    if not parent:
        self.root = right
    else:
        if parent.left == node:
            parent.left = right
        else:
            parent.right = right
    pass


def right_rotate(self, node):
    # print("right rotate", node.value)

    parent = node.parent
    left = node.left

    # Step 1
    node.left = left.right
    if node.left:
        node.left.parent = node

    # Step 2
    left.right = node
    node.parent = left

    # Step 3
    left.parent = parent
    if not parent:
        self.root = left
    else:
        if parent.left == node:
            parent.left = left
        else:
            parent.right = left
    pass
