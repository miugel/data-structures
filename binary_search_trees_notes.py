'''
trees:
similar to linked lists but nodes (tree nodes) can link to multiple nodes
maximum number of nodes a node can point to
binary tree, two max
ternary tree, 3 nodes max
4-ary tree, 4 notes max, etc.
root, topmost node in the tree
child, a node directly connected to another node when moving away from the root node
parent, a node directly connected to another node when moving towards the root node,
siblings, nodes that share the same parent
leaf, a node that does not have any children
binary search trees, nodes on the left side are less than or equal to the root node
more efficient to search for an element, but not more efficient to insert
'''

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # recursive 'insert' implementation
    # does not return anything when executed
    def insert(self, value):
        # base case - we found a parking spot
        # we're in an empty spot in the tree
        if self is None:
            self = BinarySearchTreeNode(value)
        # if we aren't at base case, move towards it
        else:
            # self is a node with a value
            # comapre the value to the value at this node
            if value < self.value:
                # move to the left
                self.left.insert(value)
            # otherwise, value >= self.value
            else:
                self.right.insert(value)

    def insert(self, value):
        # self.left and/or self.right need to be valid nodes for us to call 'insert' on them
        if value < self.value:
            # check if self.left is a valid node
            if self.left:
                self.left.insert(value)
            # the left side is empty
            else:
                # we've found a valid parking spot
                self.left = BinarySearchTreeNode(value)
        # otherwise, value >= self.value
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTreeNode(value)

    def contains(self, target):
        pass

    def get_max(self):
        pass

    def for_each(self, cb):
        pass

'''
LRU cache
fast access
    fetch element by its index, O(1)
    fetch value by its key, O(1)
        association given by key, unlike array
        hash tables don't guarantee order though
        python 3.7, dictionaries guarantee order
'''