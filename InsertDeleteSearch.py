# Search Node
def get_node(self, value):
    '''
    Query node information based on value
    :param value:
    :return:
    '''
    if not self.root:
        return None
    node = self.root
    while node:
        if node.value == value:
            break
        if node.value > value:
            node = node.left
            continue
        else:
            node = node.right
    return node

def get_pre_node(self, node):
    '''
    Get the predecessor node, the largest value among the nodes smaller than node in the tree
    :param node:
    :return:
    '''
    if not node.left:
        return None
    pre_node = node.left
    while pre_node.right:
        pre_node = pre_node.right
    return pre_node

def get_post_node(self, node):
    '''
    Get subsequent nodes
    :param node:The smallest value among nodes larger than node in the tree
    :return:
    '''
    if not node.right:
        return None
    post_node = node.right
    while post_node.left:
        post_node = post_node.left
    return post_node

# Insert Node
def insert_node(self, node):
    '''
    Add a binary tree to add a red node to the red-black tree
    :param node:
    :return:
    '''

    # Assign a node to the root of the tree when the tree is empty
    if not self.root:
        self.root = node
        return
    # Use a temporary tree root as the root of each binary
    TemporaryRoot = self.root
    while TemporaryRoot:
        # The new node is compared from the real tree root to determine
        # whether it belongs to the left subtree or the right subtree
        # Right subtree
        if TemporaryRoot.value < node.value:
            # The new node is larger than the temporary root
            if not TemporaryRoot.right:
                node.parent = TemporaryRoot
                TemporaryRoot.right = node
                break
            TemporaryRoot = TemporaryRoot.right
            continue  # Here we use continue in order to determine whether it can be left or right twice.

        # The new node is compared from the real tree root to determine
        # whether it belongs to the left subtree or the right subtree
        # Left subtree
        if TemporaryRoot.value > node.value:
            # The new node is smaller than the temporary tree root
            if not TemporaryRoot.left:
                node.parent = TemporaryRoot
                TemporaryRoot.left = node
                break
            # Find the position where the left subtree of the temporary tree root is the leaf node
            TemporaryRoot = TemporaryRoot.left
    pass

# Delete Node
def pre_delete_node(self, node):
    '''
    Check before deleting and return to the final point to be deleted
    :param node:
    :return:
    '''
    post_node = self.get_post_node(node)
    if post_node:
        node.value, post_node.value = post_node.value, node.value
        return self.pre_delete_node(post_node)
    pre_node = self.get_pre_node(node)
    if pre_node:
        pre_node.value, node.value = node.value, pre_node.value
        return self.pre_delete_node(pre_node)
    # No predecessor node, and no follow-up node
    return node

def delete_node(self, value):

    node = self.get_node(value)
    if not node:
        print("node error {}".format(value))
        return
    # save_rb_tree(self.root, "{}_delete_0".format(value))
    # Get the node to be deleted
    node = self.pre_delete_node(node)
    # save_rb_tree(self.root, "{}_delete_1".format(value))
    # The node must not be empty, and the child nodes are also empty
    self.check_delete_node(node)
    # save_rb_tree(self.root, "{}_delete_2".format(value))
    # Actually delete the node to be deleted
    self.real_delete_node(node)
    # save_rb_tree(self.root, "{}_delete_3".format(value))
    pass

def real_delete_node(self, node):
    '''
    Really delete node function
    :param node:
    :return:
    '''
    if self.root == node:
        self.root = None
        return
    if node.parent.left == node:
        node.parent.left = None
        return
    if node.parent.right == node:
        node.parent.right = None
    return