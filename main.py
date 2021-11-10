from RedBlackTree import RBTree, RBNode
import InsertDeleteSearch

import random

# For trees t1, t2 intersection operation
def TraversalBeforeIntersection(node):
    """Store List 'TempListTree2' by In-order Traversal"""
    global TempListTree2
    if node == None:
        return
    TraversalBeforeIntersection(node.left)
    # Insert same value into a new global list 'TempListTree2'
    TempListTree2.append(node.value)
    TraversalBeforeIntersection(node.right)

# Time complexity: O(n + nlogn)
def Intersection(t1, t2):
    SameValueList = []
    if not (t1.root and t2.root):   # exit condition
        return 'There is no matched elements in both t1 and t2.'
    TraversalBeforeIntersection(t2.root)

    for i in range(len(TempListTree2)):
        BoolValue = t1.get_node(TempListTree2[i])
        if BoolValue:
            SameValueList.append(TempListTree2[i])
            continue
    return SameValueList

# For calculating tree t1 median operation
def TraversalForMedian(node):
    """Store List 'TempListTree1' by In-order Traversal"""
    global TempListTree1
    if node == None:
        return
    TraversalForMedian(node.left)
    # Insert same value into a new global list 'TempListTree1'
    TempListTree1.append(node.value)
    TraversalForMedian(node.right)
    return TempListTree1

# middle number
def median(tree):
    TempList = TraversalForMedian(tree.root)
    midIndex = int(len(TempList) // 2)  # median index

    if len(TempList) % 2 == 0:  # even
        mid = (TempList[midIndex-1] + TempList[midIndex]) / 2
    else:   # odd
        mid = TempList[midIndex]
    return mid

if __name__ == '__main__':

    TempListTree1 = []  # Store the new list for calculate the median of 'tree1'
    tree1 = RBTree()
    # data1 = list(range(1, 21))  # create numbers for creating tree
    # random.shuffle(data1)    # random sort 'data1'
    data1 = random.sample(range(1, 21), 15)
    print('\n20 numbers from 1 to 20 random sort in data1: ', data1)
    # Insert
    for elem in data1:    # add numbers in 'data1' into 'tree1'
        tree1.add_node(RBNode(elem))

    TempListTree2 = []  # Store the new list of intersection(t1, t2)
    tree2 = RBTree()    # tree t2 is merged target
    data2 = random.sample(range(-10, 20), 5)
    print('\n5 numbers between -10 and 30 in data2: ', data2)
    for elem in data2:     # add numbers in 'data2' into 'tree2'
        tree2.add_node(RBNode(elem))

    # Traversal
    print('\nInorderTraversal:')
    tree1.InorderTraversal(tree1.root)

    # Intersection
    print('\nThe numbers both in t1 and t2:', Intersection(tree1, tree2))

    # Search
    random.shuffle(data1)   # Re-order data1
    print('\nThe number I want to find is the last number after re-order data1 is:', data1[-1])
    findNumber = tree1.get_node(data1[-1])     # get node
    # output number?

    # max
    maxValueNode = tree1.tree_maximum(tree1.root)
    print('\nMax:', maxValueNode.value)
    # min
    minValueNode = tree1.tree_minimum(tree1.root)
    print('\nMin:', minValueNode.value)
    # mid
    midValue = median(tree1)
    print('\nMid:', midValue)

    # print('\nIn-Order Traversal:')
    # tree1.InorderTraversal(tree1.root)

    # Delete
    random.shuffle(data1)   # Re-order data1
    print('\nThe number I want to find is the last number after re-order data1 is:', data1[0])     # Delete the first number after re-order 'data1'
    tree1.delete_node(data1[0])
    print('\nCheck the new tree after delete:')
    tree1.InorderTraversal(tree1.root)

    pass
