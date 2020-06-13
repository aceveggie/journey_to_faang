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
        self.hash_map = hash_map
        self.array = []
        self._heap_size = heap_size
        self._heap_capacity = 0

    def _update_hash_map(self, nodes, vals):
        '''
        update self.hash_map content
        '''
        pass

    def get_size(self):
        '''
        return size
        '''
        return self._heap_size

    def check(self):
        '''
        check heap invariant property
        '''
        return True

    def contains(self, val):
        # try O(1)
        if self.hash_map:
            try:
                if self.hash_map[val]:
                    return True
            except Exception:
                return False
        # use O(N) solution
        return val in self.array

    def find(self, val):
        '''
        iterate, find index
        '''
        if self.hash_map:
            try:
                # try fnding index
                return self.hash_map[val]
            except Exception:
                # exception in finding index
                return -1
        # use O(N) solution
        if val in self.array:
            return self.array.index(val)
        return -1

    def insert(self, val):
        '''
        insert at end, bubble down
        while heapify == False:
            bubbling parent, smaller smaller child up.
        '''
        if self.get_size() == 0:
            self.array.push(val)
        else:
            
        self._heap_size += 1
    def poll(self):
        '''
        swap root with leaf, remove original root,
        while heapify == False:
            bubble smaller child up
        '''
        # proceed if not empty
        if self.get_size() > 0:
            pass
        self.remove()

    def remove(self, index=0):
        '''
        find, swap element if leaf, remove original element,
        while heapify == False:
            bubble smaller child up
        '''
        # proceed if not empty
        if self.get_size() > 0:
            pass
        pass

    def peek(self):
        if self.get_size > 0:
            return self.array[0]


if __name__ == "__main__":
    q_obj = SimplePriorityQueue()
