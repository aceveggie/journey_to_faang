'''
Single linked list implementation
'''


class Node:
    '''
    basic definition of a singly linked list node
    '''
    def __init__(self, data):
        self.next = None
        self.data = data


class List:
    '''
    class definition for a singly linked list
    '''
    def __init__(self, head_val):
        # create an empty node
        # create head
        # create tail
        # track length
        node = Node(head_val)
        self.head = node
        self.tail = node
        self._length = 1

    def append(self, data_val):
        self._add_last(data_val)
        self._length += 1

    def _add_first(self, data_val):
        # create node
        # if empty, update head next
        # update tail.next to new node
        # update tail to new node
        new_head = Node(data_val)
        orig_head = self.head
        new_head.next = orig_head
        self.head = new_head

    def _add_last(self, data_val):
        # create node
        # if empty, update head next
        # update tail.next to new node
        # update tail to new node
        node = Node(data_val)
        if self._length == 1:
            self.head.next = node
        self.tail.next = node
        self.tail = node

    def insert(self, at_position, data_val):
        # check validity
        # special case when it is empty
        # special case when inserting at head
        # special case when inserting at tail
        if self.check_if_empty():
            return
        if at_position > self._length:
            return
        cur_node = self.head
        prev_node = None
        idd = 0
        while idd != at_position:
            prev_node = cur_node
            cur_node = cur_node.next
            idd += 1
        # if inserting at head
        if prev_node is None:
            self._add_first(data_val)
        # if inserting at tail
        elif at_position == self._length:
            self._add_last(data_val)
        # if inserting at rest
        else:
            new_node = Node(data_val)
            prev_node.next = new_node
            new_node.next = cur_node
        self._length += 1

    def get_index(self, data_val):
        cur_node = self.head
        idd = 0
        while cur_node.next is not None:
            if cur_node.data == data_val:
                return idd
            cur_node = cur_node.next
        # reached end
        return -1

    def get_first(self):
        return self.head.data

    def get_last(self):
        return self.tail.data

    def _remove_first(self):
        cur_head_next = self.head
        del self.head
        self.head = cur_head_next

    def _remove_last(self):
        # need to iterate till just before last
        cur_node = self.head
        while cur_node != self.tail:
            prev_node = cur_node
            cur_node = cur_node.next
        # del self.tail
        self.tail = prev_node
        self.tail.next = None

    def remove(self, at_position):
        # special case when it is empty
        if self._length <= 1:
            self.clear()
            return
        # special case when removing at head
        if at_position == 0:
            self._remove_first()
        # special case when removing at tail
        elif at_position == self._length - 1:
            self._remove_last()
        else:
            idd = 0
            cur_node = self.head
            while idd < at_position:
                prev_node = cur_node
                cur_node = cur_node.next
                idd += 1
            prev_node.next = cur_node.next
        self._length -= 1
        pass

    def print_all(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data, end=' ')
            cur_node = cur_node.next
        print()

    def get_length(self):
        return self._length

    def clear(self):
        cur_node = self.head
        while cur_node is not None:
            next_node = cur_node.next
            del cur_node
            cur_node = next_node
        self.head = None
        self.tail = None
        self._length = 0

    def check_if_empty(self):
        return self._length == 0


if __name__ == "__main__":
    print('done')
    list_obj = List(10)
    list_obj.append(20)
    list_obj.append(30)
    list_obj.append(40)
    list_obj.print_all()
    # list_obj.clear()
    list_obj.insert(4, 5)
    list_obj.insert(4, 50)
    list_obj.print_all()
    print(list_obj.get_first())
    print(list_obj.get_last())
    list_obj.print_all()
    list_obj.remove(1)
    list_obj.print_all()
    list_obj.remove(1)
    list_obj.print_all()
    list_obj.remove(1)
    list_obj.print_all()
    list_obj.remove(1)
    list_obj.print_all()
    list_obj.remove(1)
    list_obj.print_all()
    # list_obj.remove(1)
    list_obj.print_all()
    print(list_obj.get_first())
    print(list_obj.get_last())
