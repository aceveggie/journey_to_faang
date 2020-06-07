'''
Single linked list implementation
'''


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class List:
    def __init__(self, head_val):
        # create an empty node
        # create head
        # create tail
        # track length
        node = Node(head_val)
        self.head = node
        self.tail = node
        self._length = 1

    def add(self, data_val):
        # create node
        # if empty, update head next
        # update tail.next to new node
        # update tail to new node
        node = Node(data_val)
        if self._length == 1:
            self.head.next = node
        self.tail.next = node
        self.tail = node
        self._length += 1

    def insert(self, at_node_val, data_val):
        # special case when it is empty
        # special case when inserting at head
        # special case when inserting at tail
        cur_node = self.head
        while cur_node.next != 
        pass

    def remove(self):
        # special case when it is empty
        # special case when removing at head
        # special case when removing at tail
        pass

    def print_all(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data, end=' ')
            cur_node = cur_node.next
        print()

    def get_length(self):
        return self._length


if __name__ == "__main__":
    print('done')
    list_obj = List(10)
    list_obj.add(20)
    list_obj.add(30)
    list_obj.add(40)
    list_obj.print_all()
