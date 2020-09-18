'''
    Implement simple priority queue using a heap
    Implementing a min heap
'''


class Node:
    def __init__(self, data_val):
        self.data = data_val
        self.left = None
        self.right = None
        self.parent = None
        self.index = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class SimplePriorityQueue:
    '''
    implement simple priority queue using a binary heap
    '''
    def __init__(self, heap_size=0, hash_map={}):
        pass


if __name__ == "__main__":
    q_obj = SimplePriorityQueue()
