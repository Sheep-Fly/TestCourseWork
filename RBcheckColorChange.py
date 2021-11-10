# @tree_log
# Use for insert
def check_node(self, node):
    '''
    Check whether the node and parent node are damaged
    :param node:
    :return:
    '''
    # If it is the root node or the parent node is the root node, directly set it as a black node and exit
    if self.root == node or self.root == node.parent:
        self.root.set_black_node()
        # print("set black ", node.value)
        return

    # If the parent node is a black node, exit directly
    if node.parent.is_black_node():
        return

    # If the sibling node of the parent node is also a red node
    grand = node.parent.parent
    if not grand:
        self.check_node(node.parent)
        return
    if grand.left and grand.left.is_red_node() and grand.right and grand.right.is_red_node():
        grand.left.set_black_node()
        grand.right.set_black_node()
        grand.set_red_node()
        self.check_node(grand)
        return

    # If the sibling node of the parent node is also a black node
    # node node.parent node.parent.parent (different side)
    parent = node.parent
    if parent.left == node and grand.right == node.parent:
        self.right_rotate(node.parent)
        self.check_node(parent)
        return
    if parent.right == node and grand.left == node.parent:
        parent = node.parent
        self.left_rotate(node.parent)
        self.check_node(parent)
        return

    # node node.parent node.parent.parent (same side)
    parent.set_black_node()
    grand.set_red_node()
    if parent.left == node and grand.left == node.parent:
        self.right_rotate(grand)
        return
    if parent.right == node and grand.right == node.parent:
        self.left_rotate(grand)
        return

# for delete
def check_delete_node(self, node):
    '''
    check and delete node
    :param node:
    :return:
    '''
    if self.root == node or node.is_red_node():
        return

    node_is_left = node.parent.left == node
    brother = node.parent.right if node_is_left else node.parent.left
    # brother must not be none
    if brother.is_red_node():
        # If the node is a black node, the sibling node is a red node
        # Rotate the parent node: turn the child node into black, and the sibling node to black
        # Rebalance
        if node_is_left:
            self.left_rotate(node.parent)
        else:
            self.right_rotate(node.parent)
        node.parent.set_red_node()
        brother.set_black_node()
        print("check node delete more ")
        # Check the current node again
        self.check_delete_node(node)
        return

    all_none = not brother.left and not brother.right
    all_black = brother.left and brother.right and brother.left.is_black_node() and brother.right.is_black_node()
    if all_none or all_black:
        brother.set_red_node()
        if node.parent.is_red_node():
            node.parent.set_black_node()
            return
        self.check_delete_node(node.parent)
        return

    brother_same_right_red = node_is_left and brother.right and brother.right.is_red_node()
    brother_same_left_red = not node_is_left and brother.left and brother.left.is_red_node()
    if brother_same_right_red or brother_same_left_red:

        if node.parent.is_red_node():
            brother.set_red_node()
        else:
            brother.set_black_node()
        node.parent.set_black_node()

        if brother_same_right_red:
            brother.right.set_black_node()
            self.left_rotate(node.parent)
        else:
            brother.left.set_black_node()
            self.right_rotate(node.parent)

        return

    brother_diff_right_red = not node_is_left and brother.right and brother.right.is_red_node()
    brother_diff_left_red = node_is_left and brother.left and brother.left.is_red_node()
    if brother_diff_right_red or brother_diff_left_red:
        brother.set_red_node()
        if brother_diff_right_red:
            brother.right.set_black_node()
            self.left_rotate(brother)
        else:
            brother.left.set_black_node()
            self.right_rotate(brother)

        self.check_delete_node(node)
        return
