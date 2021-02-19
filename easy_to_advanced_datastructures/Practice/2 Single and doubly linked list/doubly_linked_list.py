'''
Single linked list implementation
'''


class Node:
    '''
    basic definition of a doubly linked list node
    '''
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class DoubleList:
    '''
    basic definition of a doubly linked list
    '''
    def __init__(self, data_val):
        '''
        constructor
        '''
        new_node = Node(data_val)
        self.head = new_node
        self.tail = new_node
        self._length = 1

    def print_all(self):
        '''
        print all
        '''
        if self._length <= 0:
            return
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data, end=' ')
            cur_node = cur_node.next
        print()

    def clear(self):
        '''
        clear contents
        '''
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
        self._length = 0

    def _add_first(self, data_val):
        cur_head = self.head
        new_node = Node(data_val)
        cur_head.prev = new_node
        new_node.next = cur_head
        self.head = new_node

    def _add_last(self, data_val):
        cur_tail = self.tail
        new_node = Node(data_val)
        cur_tail.next = new_node
        new_node.prev = cur_tail
        self.tail = new_node

    def append(self, data_val):
        self._add_last(data_val)
        self._length += 1

    def insert(self, index, data_val):
        if index == 0:
            self._add_first(data_val)
        elif index == self._length:
            self._add_last(data_val)
        else:
            idd = 0
            prev_node = None
            cur_node = self.head
            while idd != index:
                prev_node = cur_node
                cur_node = cur_node.next
                idd += 1
            new_node = Node(data_val)
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = cur_node
        self._length += 1

    def _remove_first(self):
        cur_head = self.head
        if self._length <= 1:
            self.head = None
            self.tail = None
        else:
            self.head = cur_head.next
            self.head.prev = None

    def _remove_last(self):
        cur_tail = self.tail
        if self._length <= 1:
            self.tail = None
            self.head = None
        else:
            self.tail = cur_tail.prev
            self.tail.next = None

    def get_val(self, index):
        if self._length == 0:
            return
        idd = 0
        cur_node = self.head
        while idd != index and cur_node is not None:
            cur_node = cur_node.next
            idd += 1
        return cur_node

    def remove(self, index):
        # print('removing node at index', index, 'val:', self.get_val(index))
        if index == 0:
            self._remove_first()
        elif index == self._length - 1:
            self._remove_last()
        else:
            idd = 0
            prev_node = None
            cur_node = self.head
            while idd != index:
                prev_node = cur_node
                cur_node = cur_node.next
                idd += 1
            prev_node.next = cur_node.next
            cur_node.next.prev = prev_node
        self._length -= 1

    def get_length(self):
        return self._length

    def get_first(self):
        return self.head.data

    def get_last(self):
        return self.tail.data

    def _debug(self):
        cur_node = self.head
        print('---')
        self.print_all()
        print('--------')
        while cur_node is not None:
            print(
                'cur node: ', cur_node.prev, '<-->', cur_node.data, '<-->',
                cur_node.next)
            cur_node = cur_node.next
        print('--------------------')


if __name__ == "__main__":
    print('done')
    list_obj = DoubleList(10)
    list_obj.append(20)
    list_obj.append(30)
    list_obj.append(40)
    list_obj.insert(4, 5)
    list_obj.insert(5, 50)
    list_obj.insert(6, 60)
    list_obj.print_all()
    list_obj.remove(0)
    list_obj.remove(5)
    list_obj.remove(1)
    list_obj.remove(2)
    list_obj.print_all()
    list_obj.clear()
    print(list_obj.get_length())
