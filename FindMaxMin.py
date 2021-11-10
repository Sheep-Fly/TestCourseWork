# Take the node node as the root node to find the largest node
def tree_maximum(self, node):
    """
Find the maximum node of the tree with node node as the root node,
and return the rightmost node with this node as the root node.
    :param node: Tree with this node as the root node
    :return: Maximum node
    """
    temp_node = node
    while temp_node.right:
        temp_node = temp_node.right
    return temp_node

# Take the node node as the root node and find the smallest node
def tree_minimum(self, node):
    """
    Find the minimum node of the tree with node node as the root node,
    and return the leftmost node with this node as the root node
    :param node: Tree with this node as the root node
    :return: Minimum node
    """
    temp_node = node
    while temp_node.left:
        temp_node = temp_node.left
    return temp_node