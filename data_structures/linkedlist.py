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
            self._add_right(self.current_day, new_node)

    def _add_right(self, node, new_node):
        if node.next is None:
            node_prev = node
            node.next = new_node
            node = node.next
            node.prev = node_prev
        else:
            self._add_right(node.next, new_node)

    def add_left(self, value):
        self.current_day = self._add_left(self.current_day, value)

    def _add_left(self, node, value):
        new_node = NodeLinkedList(value)
        if node is None:
            node = new_node
            return
        node.prev = new_node
        new_node.next = node
        return new_node

    def add_by_index(self, index, value):
        self._add_by_index(self.current_day, index, value)

    def _add_by_index(self, node, index, value):
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

    def traverse_forward(self):
        self._traverse_forward(self.current_day)

    def _traverse_forward(self, node):
        if node is None:
            return
        print(node.value)
        return self._traverse_forward(node.next)

    def traverse_backward(self):
        self._traverse_backward(self.current_day)

    def _traverse_backward(self, node):
        if node.next is None:
            self._print_backward(node)
            return
        self._traverse_backward(node.next)

    def _print_backward(self, node):
        if node is None:
            return
        print(node.value)
        return self._print_backward(node.prev)

    def search(self, value):
        return self._search(self.current_day, value, index=0)

    def _search(self, node, value, index):
        if node is None:
            print('False')
            print('index: ', index)
            return
        if node.value == value:
            print('True')
            print('index: ', index)
            return
        self._search(node.next, value, index+1)

    def pop_right(self):
        self._pop_right(self.current_day)

    def _pop_right(self, node):
        if node.next is None:
            node = node.prev
            node.next = None
        else:
            self._pop_right(node.next)

    def pop_left(self):
        self.current_day = self.current_day.next
        self.current_day.prev = None

    def delete_by_value(self, value):
        self._delete_by_value(self.current_day, value)

    def _delete_by_value(self, node, value):
        if node is None:
            print('Value not found')
            return
        if node.value == value:
            node_left = node.prev
            node_right = node.next
            node = node.next
            node.prev = node_left
            node = node.prev
            node.next = node_right
            return
        self._delete_by_value(node.next, value)

    def delete_by_index(self, index):
        self._delete_by_index(self.current_day, index=index)

    def _delete_by_index(self, node, index):
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
        if self.current_day is None:
            return
        new_node = NodeLinkedList(self.current_day.value)
        self.current_day = self._reverse(self.current_day.next, new_node)

    def _reverse(self, old_node, new_node):
        if old_node is None:
            return new_node
        new_node = self._add_left(new_node, old_node.value)
        return self._reverse(old_node.next, new_node)

    def round_up(self):
        linked_list = self.current_day
        first_node = self.current_day
        self._round_up(linked_list, first_node)

    def _round_up(self, linked_list, first_node):
        if linked_list.next is None:
            linked_list.next = first_node
            first_node.prev = linked_list
            return
        self._round_up(linked_list.next, first_node)


if __name__ == "__main__":
    wds = WeekDaysDouble()
    wds.add_right('tuesday')
    wds.add_right('wednesday')
    wds.add_right('thursday')
    wds.add_right('friday')
    wds.add_right('saturday')
    wds.add_left('monday')
    wds.add_left('sunday')
    print('############ Traverse Forward')
    wds.traverse_forward()
    print('############ Traverse Backward')
    wds.traverse_backward()
    wds.search('wed')
    wds.search('wednesday')
    print('############ Pop right')
    wds.pop_right()
    wds.traverse_forward()
    wds.add_right('saturday')
    wds.traverse_forward()
    print('############ Pop left')
    wds.pop_left()
    wds.traverse_forward()
    print("############ add left 'sunday'")
    wds.add_left('sunday')
    wds.traverse_forward()
    print("############ delete by value")
    wds.delete_by_value('wednesday')
    wds.traverse_forward()
    wds.add_by_index(3, 'wednesday')
    wds.traverse_forward()
    print("############ delete by index")
    wds.delete_by_index(3)
    wds.traverse_forward()
    wds.add_by_index(3, 'wednesday')
    wds.traverse_forward()
    print('############ Reverse')
    wds.reverse()
    wds.traverse_forward()
    wds.reverse()
    wds.traverse_forward()
    wds.round_up()
    wds.traverse_forward()
