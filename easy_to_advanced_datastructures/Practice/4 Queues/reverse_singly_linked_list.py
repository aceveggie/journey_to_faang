'''
implement a queue with singly linked list
'''


from typing import Counter


class Node:
    '''
        Simple node
    '''
    def __init__(self, data_val):
        self.data = data_val
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class SinglyLinkedListQueue:
    '''
        implements singly linked list queue
        enqueue adds at tail
        deque removes from head
    '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.pointer = self.head

    def _add_first(self, data_val):
        '''
            to be called when size = 0
        '''
        new_node = Node(data_val)
        self.head = new_node
        self.tail = new_node

    def enque(self, data_val):
        '''
        insert new node at tail
        update tail
        '''
        if self.size < 1:
            self._add_first(data_val)
        else:
            cur_tail = self.tail
            new_node = Node(data_val)
            cur_tail.next = new_node
            self.tail = new_node
        self.size += 1

    def deque(self):
        if self.size <= 1:
            self.head = None
            self.tail = None
            self.size = 0
            return
        else:
            ret_node = self.head
            self.head = self.head.next
            self.size -= 1
            return ret_node

    def get_size(self):
        return self.size

    def get_first(self):
        return self.head

    def get_last(self):
        return self.tail

    def print_all(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node, end=' ')
            cur_node = cur_node.next
        print()

    def iterative_reverse_list(self):
        # no need to reverse if size <= 1
        if self.size <= 1:
            return
        prev_node = None
        cur_node = self.head
        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head, self.tail = self.tail, self.head



if __name__ == "__main__":
    q_obj = SinglyLinkedListQueue()
    q_obj.enque(10)
    q_obj.enque(20)
    q_obj.enque(30)
    q_obj.enque(40)
    q_obj.enque(50)
    q_obj.print_all()
    # print(q_obj.deque())
    q_obj.print_all()
    # print(q_obj.deque())
    # print(q_obj.deque())
    # print(q_obj.deque())
    # print(q_obj.deque())
    print('done all opeartions:')
    q_obj.print_all()
    print('------------------')
    print('now reversing.......')
    q_obj.reverse_list()
    q_obj.print_all()
    print('----------done------------')
