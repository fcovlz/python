class NodeBinaryTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self.tree = None

    def add(self, value):
        if self.tree is None:
            self.tree = NodeBinaryTree(value)
        else:
            self._add(self.tree, value)

    def _add(self, node, value):
        if value == node.value:
            print('This value is already on the tree. Try a new one')
            return
        if value < node.value:
            if node.left is not None:
                self._add(node.left, value)
            else:
                node.left = NodeBinaryTree(value)
        else:
            if node.right is not None:
                self._add(node.right, value)
            else:
                node.right = NodeBinaryTree(value)

    def traverse(self):
        self._traverse(self.tree)

    def _traverse(self, node, level=0):
        if node is not None:
            self._traverse(node.right, level+1)
            print('   ' * level + str(node.value))
            self._traverse(node.left, level+1)

    def binary_search(self, value):
        self._binary_search(self.tree, value)

    def _binary_search(self, node, value):
        if node is None:
            print(False)
        elif node.value == value:
            print(True)
        else:
            if value < node.value:
                self._binary_search(node.left, value)
            else:
                self._binary_search(node.right, value)

    @property
    def height(self):
        if self.tree is None:
            return 0
        else:
            return self._height1(self.tree)

    def _height1(self, node, current_height=0):
        if node is None:
            return current_height
        left_height = self._height1(node.left, current_height + 1)
        right_height = self._height1(node.right, current_height + 1)
        return max(left_height, right_height)

    def _height2(self, node, _is_balanced=True):
        if node is None:
            return 0
        left_height = self._height2(node.left)
        right_height = self._height2(node.right)
        print('#####################')
        print('left height: ', left_height)
        print('right height: ', right_height)
        print('comparison: ', max(left_height, right_height) + 1)
        return max(left_height, right_height) + 1

    @property
    def is_balanced(self):
        # formula (abs(LeftSubTreeHeight - RightSubTreeHeight) <= 1) = Balanced
        if isinstance(self._is_balanced(self.tree), bool):
            return False
        else:
            return True

    def _is_balanced(self, node):
        if node is None:
            return 0
        left_height = self._is_balanced(node.left)
        if self.is_instance_bool(left_height):
            return False

        right_height = self._is_balanced(node.right)
        if self.is_instance_bool(right_height):
            return False

        if abs(left_height - right_height) <= 1:
            return max(left_height, right_height) + 1
        else:
            return False

    def _is_balanced1(self, node):
        """
        This method is less efficient than _is_balanced()
        :param node: Current node/tree
        :return: False or True, in case node/tree is balanced
        """
        if node is None:
            return True
        left_height = self._height2(node.left)
        right_height = self._height2(node.right)
        if (abs(left_height - right_height) <= 1) and \
                self._is_balanced1(node.left) is True and \
                self._is_balanced1(node.right) is True:
            return True
        else:
            return False

    @staticmethod
    def is_instance_bool(obj):
        return isinstance(obj, bool)

    def balance_tree(self):
        if self.is_balanced:
            print('Tree is already balanced')
        else:
            self.tree = self._new_tree_balanced(self.tree)

    def _new_tree_balanced(self, node_to_balance):
        node_values_in_list = []
        self.from_nodes_to_list(node_to_balance, node_values_in_list)

        index_middle_point = int(len(node_values_in_list) / 2)
        middle_point_value = node_values_in_list[index_middle_point]
        new_tree = NodeBinaryTree(middle_point_value)

        left_list = node_values_in_list[:index_middle_point]
        right_list = node_values_in_list[index_middle_point + 1:]
        self._create_new_tree(new_tree, left_list)
        self._create_new_tree(new_tree, right_list)
        return new_tree

    def _create_new_tree(self, node, node_values_in_list):
        if len(node_values_in_list) <= 2:
            for element in node_values_in_list:
                self._add(node, element)
        else:
            index_middle_point = int(len(node_values_in_list) / 2)
            middle_value = node_values_in_list[index_middle_point]
            self._add(node, middle_value)
            left_list = node_values_in_list[:index_middle_point]
            right_list = node_values_in_list[index_middle_point + 1:]
            self._create_new_tree(node, left_list)
            self._create_new_tree(node, right_list)

    def from_nodes_to_list(self, node, node_values_in_list):
        if node is None:
            return
        self.from_nodes_to_list(node.left, node_values_in_list)
        node_values_in_list.append(node.value)
        self.from_nodes_to_list(node.right, node_values_in_list)


if __name__ == "__main__":
    bt = BinaryTree()
    bt.add(5)
    bt.add(10)
    bt.add(3)
    bt.add(1)
    bt.add(4)
    bt.add(7)
    bt.add(20)
    bt.add(30)
    bt.binary_search(30)
    bt.add(0)
    bt.add(-1)
    bt.add(0)
    bt.add(6)
    bt.add(8)
    bt.add(9)
    bt.add(21)
    bt.add(22)
    bt.add(23)
    bt.add(24)
    bt.add(25)
    bt.add(26)
    bt.add(27)
    bt.traverse()
    height = bt.height
    balance = bt.is_balanced
    print('Tree balance: ', balance)
    bt.balance_tree()
    bt.traverse()
    balance = bt.is_balanced
    print('Tree balance: ', balance)
