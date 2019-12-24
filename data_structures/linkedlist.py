class NodeLinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class WeekDaysDouble():
    def __init__(self):
        self.current_day = None

    def add_right(self, value):
        new_node = NodeLinkedList(value)
        if self.current_day is None:
            self.current_day = new_node
        else:
            node = self.current_day
            while node.next is not None:
                node = node.next
            node_prev = node
            node.next = new_node
            node = node.next
            node.prev = node_prev

    def add_left(self, value):
        new_node = NodeLinkedList(value)
        if self.current_day is None:
            self.current_day = new_node
        else:
            self.current_day.prev = new_node
            new_node.next = self.current_day
            self.current_day = new_node

    def add_by_index(self, index, value):
        node = self.current_day
        add_status = None
        for token in range(index):
            try:
                add_status = True
                node = node.next
            except:
                add_status = False
                break
        if add_status is True:
            new_node = NodeLinkedList(value)
            node_left = node.prev
            node_right = node

            new_node.prev = node_left
            new_node.next = node_right

            node = new_node
            node = node.next
            node.prev = new_node
            node = node.prev
            node = node.prev
            node.next = new_node

        return add_status

    def traverse_forward(self, node=''):
        if node is '':
            node = self.current_day
        elif node is None:
            return
        print(node.value)
        return self.traverse(node.next)
    
    def traverse_backward(self):
        forward = self.current_day
        while forward is not None:
            backward = forward
            forward = forward.next
        while backward is not None:
            print('node value: ', backward.value)
            backward = backward.prev

    def search(self, value):
        node = self.current_day
        index = 0
        value_on_linked_list = False
        while node is not None:
            if node.value == value:
                value_on_linked_list = True
                break
            else:
                node = node.next
                index += 1
        return value_on_linked_list, index

    def pop_right(self):
        node = self.current_day
        while node.next is not None:
            node = node.next
        node = node.prev
        node.next = None

    def pop_left(self):
        node = self.current_day
        node = node.next
        node.prev = None
        self.current_day = node

    def delete_by_value(self, value):
        node = self.current_day
        delete_status = False
        while node is not None:
            if node.value == value:
                delete_status = True
                node_left = node.prev
                node_right = node.next
                node = node.next
                node.prev = node_left
                node = node.prev
                node.next = node_right
                break
            else:
                node = node.next
        return delete_status

    def delete_by_index(self, index):
        node = self.current_day
        delete_status = False
        for token in range(index):
            try:
                delete_status = True
                node = node.next
            except:
                delete_status = False
                break

        if delete_status is True:
            node_left = node.prev
            node_right = node.next
            node = node.next
            node.prev = node_left
            node = node.prev
            node.next = node_right
        return delete_status

    def reverse(self):
        node = self.current_day
        new_node = None
        while node is not None:
            if new_node is None:
                new_node = NodeLinkedList(node.value)
            else:
                current_node = NodeLinkedList(node.value)
                current_node.next = new_node
                new_node.prev = current_node
                new_node = current_node
            node = node.next
        self.current_day = new_node

    def round_up(self):
        node = self.current_day
        first_element = node
        while node.next is not None:
            node = node.next
        node.next = first_element
        first_element.prev = node


if __name__ == "__main__":
    wds = WeekDaysDouble()
    wds.add_right('tuesday')
    wds.add_right('wednesday')
    wds.add_right('thursday')
    wds.add_right('friday')
    wds.add_right('saturday')
    wds.add_left('monday')
    wds.add_left('sunday')
    wds.traverse_forward()
    result = wds.search('wed')
    print(result)
    result = wds.search('wednesday')
    print(result)
    wds.pop_right()
    wds.traverse_forward()
    wds.add_right('saturday')
    wds.traverse_forward()
    wds.pop_left()
    wds.traverse_forward()
    wds.add_left('sunday')
    wds.traverse_forward()
    result = wds.delete_by_value('wednesday')
    print(result)
    wds.traverse_forward()
    wds.add_by_index(3, 'wednesday')
    wds.traverse_forward()
    wds.delete_by_index(3)
    wds.traverse_forward()
    wds.add_by_index(3, 'wednesday')
    wds.traverse_forward()
    wds.round_up()
    wds.traverse_forward()
    wds.reverse()
    wds.traverse_forward()
