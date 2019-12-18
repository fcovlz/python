from random import randint


class NodeBinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = NodeBinaryTree(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = NodeBinaryTree(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = NodeBinaryTree(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value already in tree")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print (cur_node.value)
            self._print_tree(cur_node.right)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left is not None:
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right is not None:
            return self._search(value, cur_node.right)
        else:
            return False


def fill_tree(tree, num_elem, max_int):
    for index in range(num_elem):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree


def tree_sample():
    tree = BinarySearchTree()
    tree.insert(2)
    tree.insert(10)
    tree = fill_tree(tree, 100, 1000)
    tree.print_tree()
    print("tree height is ", str(tree.height()))
    print(tree.search(2))
    print(tree.search(0))
    print(tree.search(1010))
