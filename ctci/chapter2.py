""""
Chapter 1: Cracking the code interview
Author: Francisco Velazquez
"""
# region Problem 2.1
"""
Write code to remove duplicates from an unsorted linked list.
"""


# region Problem 2.1
def remove_duplicated_unsorted_linked_list_solution1(linked_list_sample):
    duplicated_values = []
    while linked_list_sample is not None:
        element_value = linked_list_sample.value
        if element_value in duplicated_values:
            print("duplicated")
        else:
            duplicated_values.append(element_value)
            linked_list_sample = linked_list_sample.next
    return duplicated_values


# endregion Problem 2.1
# region utilities
class NodeLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.element = None

    def traverse(self):
        node = self.element
        while node is not None:
            print(node.value)
            node = node.next

    def insert_right(self, value):
        new_node = NodeLinkedList(value)
        if self.element is None:
            self.element = new_node
        else:
            node = self.element
            while node.next is not None:
                node = node.next
            node.next = new_node


def create_linked_list():
    linked_list = LinkedList()
    linked_list.insert_right(1)
    linked_list.insert_right(2)
    linked_list.insert_right(3)
    linked_list.insert_right(1)
    linked_list.insert_right(5)
    linked_list.insert_right(4)
    linked_list.traverse()
    return linked_list.element
# endregion utilities


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 5, 2, 4, 1]
    linked_list_input = create_linked_list()
    print(remove_duplicated_unsorted_linked_list_solution1(linked_list_input))
