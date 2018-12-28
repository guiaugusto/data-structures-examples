class Node():
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


def add_node(self):
    pass


def remove_node(self):
    """
    This method have to do this following orders:

    1. Have to find the node in Binary Tree
    2. If the node was found, it have to remove the following node
    3. Have to rebalance the following tree
    """
    pass


def search_node(self):
    pass


def list_in_order(tree):
    if tree:
        list_in_order(tree.left)
        print('{} '.format(tree.value))
        list_in_order(tree.right)


node_2 = Node(2)

node_1 = Node(1)

node_4 = Node(4)

node_2.right = node_4
node_2.left = node_1

list_in_order(node_2)
