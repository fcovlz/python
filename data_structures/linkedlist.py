class NodeLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.day = None

    def print_list(self):
        node = self.day
        while node is not None:
            print(node.value)
            node = node.next

    def insert_right(self, value):
        new_node = NodeLinkedList(value)
        if self.day is None:
            self.day = new_node
        else:
            node = self.day
            while node.next is not None:
                node = node.next
            node.next = new_node


def linked_list_sample():
    # create nodes
    days_of_the_week = LinkedList()
    days_of_the_week.insert_right('monday')
    days_of_the_week.insert_right('tuesday')
    days_of_the_week.insert_right('wednesday')
    days_of_the_week.insert_right('thursday')
    days_of_the_week.insert_right('friday')
    days_of_the_week.insert_right('saturday')
    days_of_the_week.insert_right('sunday')
    days_of_the_week.print_list()
