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
    