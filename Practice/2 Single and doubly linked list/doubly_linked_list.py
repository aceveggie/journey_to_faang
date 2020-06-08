'''
Single linked list implementation
'''


class Node:
    '''
    basic definition of a singly linked list node
    '''
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoubleList:

    def __init__(self):
        self._length = 0
        self.head = None
        self.tail = None

    def print_all(self):
        if self._length <= 0:
            return
        cur_node = self.head
        while cur_node.data is not None:
            print(cur_node.data, end=' ')
            cur_node = cur_node.next

    def clear(self):
        if self._length <= 0:
            return
        cur_node = self.head
        while cur_node is not None:
            cur_node.data = None
            cur_node.prev = None
            # get pointer to next node
            next_node = cur_node.next
            # reset cur node next pointer
            cur_node.next = None
            cur_node = next_node
        # reset head and tail
        self.head = None
        self.tail = None

    def _add_first(self, data_val):
        cur_head = self.head
        new_node = Node(data_val)
        pass

    def _add_last(self, data_val):
        cur_tail = self.tail
        pass

    def append(self, data_val):
        pass

    def insert_at(self, index, data_val):
        pass

    def _remove_first(self):
        pass

    def _remove_last(self):
        pass

    def remove_at(self, index):
        pass

    def get_length(self, index):
        pass
    
    def get_first(self):
        return self.head.data

    def get_last(self):
        return self.tail.data