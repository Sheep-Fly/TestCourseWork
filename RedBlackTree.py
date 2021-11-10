# import functionSupport
import InsertDeleteSearch
import Traversal
import Rotation
import RBcheckColorChange
import FindMaxMin

# Red-Black Tree Node
class RBNode:
    def __init__(self, value, color="R"):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1  # Number of node elements: the total number of nodes in the subtree with node as the root node

    def is_black_node(self):
        return self.color == "B"

    def is_red_node(self):
        return self.color == "R"

    def set_black_node(self):
        self.color = "B"

    def set_red_node(self):
        self.color = "R"

#     def printNode(self):
#         if self.left:
#             self.left.print()
#         print(self.value)
#         if self.right:
#             self.right.print()

# Red-Black Tree
class RBTree:

    def __init__(self):
        self.root = None
        self.index = 1
        self.action = ""

    # Pre-order Traversal
    def PreorderTraversal(self, root):
        return Traversal.PreorderTraversal(self, root)

    # In-order Traversal
    def InorderTraversal(self, root):
        return Traversal.InorderTraversal(self, root)

    # Post-order Traversal
    def PostorderTraversal(self, root):
        return Traversal.PostorderTraversal(self, root)

    # Left Rotation
    def left_rotate(self, node):
        return Rotation.left_rotate(self, node)

    # Right Rotation
    def right_rotate(self, node):
        return Rotation.right_rotate(self, node)

    # Insert Check
    def check_node(self, node):
        return RBcheckColorChange.check_node(self, node)

    # Delete Check
    def check_delete_node(self, node):
        return RBcheckColorChange.check_delete_node(self, node)

    # Insert Node
    def insert_node(self, node):
        return InsertDeleteSearch.insert_node(self, node)

    # Delete Node
    def delete_node(self, value):
        return InsertDeleteSearch.delete_node(self, value)
    def pre_delete_node(self, node):
        return InsertDeleteSearch.pre_delete_node(self, node)
    def real_delete_node(self, node):
        return InsertDeleteSearch.real_delete_node(self, node)

    # Search Node
    def get_node(self, value):
        return InsertDeleteSearch.get_node(self, value)
    def get_pre_node(self, node):
        return InsertDeleteSearch.get_pre_node(self, node)
    def get_post_node(self, node):
        return InsertDeleteSearch.get_post_node(self, node)

    # Take the node node as the root node to find the largest node
    def tree_maximum(self, node):
        """
        Find the maximum node of the tree with node as the root node,
        and return the rightmost node with this node as the root node.
        :param: node as root
        :return: maximum node
        """
        temp_node = node
        while temp_node.right:
            temp_node = temp_node.right
        return temp_node

    # Find the smallest node based on root node
    def tree_minimum(self, node):
        """
        Find the minimum node of the tree with node as the root node,
        and return the leftmost node with this node as the root node
        :param: node as root
        :return: minimum node
        """
        temp_node = node
        while temp_node.left:
            temp_node = temp_node.left
        return temp_node

    # Add Node
    def add_node(self, node):
        self.action = 'inser node {}'.format(node.value)
        self.insert_node(node)
        self.check_node(node)
        pass

