'''
    Implement simple priority queue using a heap
    Implementing a min heap with O(log N) removal (with constant lookup)
    Implementing a min heap using array (list in python)
    Added recursive check for heap invariance
    Added hash map to check contains or not
'''


class SimplePriorityQueue:

    def __init__(self):
        self.array = []
        self.heap_size = 0
        self.heap_capacity = 0
        self.hash_map = {}

    def bubble_up(self, index):
        # iteratively bubble up element at index
        # until we satisfy heap invariant property
        while self.check_recursive_heap_invariant() is False:
            parent_index = self.get_parent_index(index)
            if parent_index is None:
                break
            is_current_index_less_than_parent = self._less(index, parent_index)
            if is_current_index_less_than_parent:
                # swap elements and indices
                self.swap(index, parent_index)
                index = parent_index

    def bubble_down(self, index):
        # iteratively bubble down element at index
        # until we satisfy heap invariant property
        # To bubble down, swap current index element with smaller
        # of the 2 child nodes
        while self.check_recursive_heap_invariant() is False:
            left_child_index = self.get_left_child_index(index)
            right_child_index = self.get_right_child_index(index)
            left_child_val = self.get_left_child_value(index)
            right_child_val = self.get_right_child_value(index)
            # self._get(index) give cur node val
            if left_child_val <= right_child_val:
                self.swap(index, left_child_index)
                index = left_child_index
            else:
                self.swap(index, right_child_index)
                index = right_child_index

    def insert(self, value):
        # insert at leaf,
        # then bubble up
        # print('inserting', value, 'in', self.array)

        # if empty heap, insert at 0, return
        if self.heap_size == 0:
            self.array.append(value)
            self.heap_size = len(self.array)
            self.heap_capacity += 1
            self.hash_map_add(0, value)
            return True

        # else, inserting at leaf, bubble up
        self.array.append(value)
        self.hash_map_add(index=len(self.array)-1, val=value)

        cur_index = len(self.array) - 1
        self.heap_size = len(self.array)
        if self.heap_capacity < self.heap_size:
            self.heap_capacity += 1

        # now bubble up
        self.bubble_up(cur_index)

    def remove(self, value):
        # obtain index of given value
        # swap obtained value with leaf node
        # bubble down element at given index
        # until you satisfy heap invariant
        if self.heap_size <= 1:
            self.clear()
            return True
        try:
            # O(N) approach
            index = self.array.index(value)
            self.remove_at(index)
        except Exception:
            # couldn't find element
            return False
        return True

    def remove_at(self, index):
        # get element at given index
        # swap element with leaf node
        # bubble down element at given index
        # until you satisfy heap invariant
        if index == 0 and self.heap_size <= 1:
            self.clear()
        cur_val = self.array[index]
        # other cases
        # swap with leaf
        leaf_index = self.heap_size - 1
        self.swap(leaf_index, index)

        # remove last element
        # this is O(1) https://wiki.python.org/moin/TimeComplexity
        self.hash_map_remove(index=leaf_index, val=cur_val)
        self.array.pop()
        self.heap_size -= 1
        # bubble up and down as required
        # sometimes heap invariance may be already satisfied
        # in a given direction, so do it both ways as we don't know
        # which direction it doesn't satisfy
        self.bubble_down(index)
        self.bubble_up(index)

    def poll(self):
        # remove root element at index 0
        self.remove_at(0)

    def peek(self):
        # return element at root
        if self.heap_size != 0:
            return self._get(0)
        return None

    def get_parent_index(self, index):
        try:
            return (index-1)//2
        except Exception:
            return None

    def get_right_child_index(self, index):
        try:
            return (2*index)+2
        except Exception:
            return None

    def get_left_child_index(self, index):
        try:
            return (2*index)+1
        except Exception:
            return None

    def get_parent_value(self, index):
        try:
            return self._get((index-1)//2)
        except Exception:
            return None

    def get_right_child_value(self, index):
        try:
            return self._get((2*index)+2)
        except Exception:
            return None

    def get_left_child_value(self, index):
        try:
            return self._get((2*index)+1)
        except Exception:
            return None

    def swap(self, i, j):
        i_val = self.array[i]
        j_val = self.array[j]
        self.hash_map_update(i, i_val, j, j_val)

        self.array[i], self.array[j] = self.array[j], self.array[i]
        

    def contains(self, value):
        # check if element contains a specific value
        # O(N) or O(heap_capacity) implementation
        for i in range(self.heap_size):
            if self._get(i) == value:
                return True
        return False

    def disp(self):
        print(self.array)

    def is_empty(self):
        return self.heap_size == 0

    def clear(self):
        # iterate through elements, set them to None
        # set heap size = 0
        # O(N) operation
        self.array = []
        self.heap_capacity = 0
        self.heap_size = 0
        self.hash_map = {}

    def check_heap_invariant(self, index=0):
        # this does it iteratively
        # O(N) complexity
        # from given index check top to bottom
        # left to right
        # do we satisfy heap invariance?
        for i in range(self.heap_size):
            # print('checking at', i)

            c_val = self._get(i)
            l_val = self.get_left_child_value(i)
            r_val = self.get_right_child_value(i)
            # we have 2 children
            if (l_val is not None) and (r_val is not None):
                if c_val > l_val or c_val > r_val:
                    return False
            # we have only left child
            elif (l_val is not None) and (c_val > l_val):
                # print('in violation at index', i)
                return False
            # we have only right child
            elif (r_val is not None) and (c_val > r_val):
                # print('in violation at index', i)
                return False
        # we have successfully iterated from top to bottom
        # we haven't seen any violation of heap_invariant
        return True

    def check_recursive_heap_invariant(self, index=0):
        # this does it recursively O(2^depth_of_heap)
        # from given index check top to bottom
        # left to right
        # do we satisfy heap invariance?

        # we have moved out of bounds without violating the property
        if index >= self.heap_size:
            return True
        # parent is current node 'index'

        l_index = (2*index) + 1
        r_index = (2*index) + 2

        # if we are within range and current index is greater than child
        if l_index < self.heap_size and self._less(index, l_index) is False:
            return False
        # if we are within range and current index is greater than child
        if r_index < self.heap_size and self._less(index, r_index) is False:
            return False

        return self.check_recursive_heap_invariant(l_index) and\
            self.check_recursive_heap_invariant(r_index)

    def _get(self, i):
        # return element at index i
        return self.array[i]

    def _less(self, i, j):
        # To convert this min heap to a max heap
        # flip comparison signs (instead of checking if parent less than child,
        # check greater than child)
        # or while inserting elements, negate the signs

        # In this case, check if element[i] <= element[j]
        i_val = self._get(i)
        j_val = self._get(j)
        return i_val <= j_val

    def hash_map_add(self, index, val):
        '''
            index belongs to index in self.array
        '''
        try:
            self.hash_map[val].append(index)
        except Exception:
            # hash map for this value doesn't exist
            self.hash_map[val] = [index]

    def hash_map_remove(self, index, val):
        '''
            index belongs to index in self.array
        '''
        try:
            # identify specific list using 'val'
            self.hash_map[val].remove(index)  # remove value which is 'index'
        except Exception:
            print(self.hash_map)
            print(
                'tried to remove val', val, 'from index', index, 'in hashmap')
            raise

    def hash_map_update(self, i, i_val, j, j_val):
        '''
            indices i, j belongs to indices in self.array
        '''
        self.hash_map[i_val].remove(i)
        self.hash_map[j_val].remove(j)
        self.hash_map[i_val].append(j)
        self.hash_map[j_val].append(i)


if __name__ == "__main__":
    q_obj = SimplePriorityQueue()
    q_obj.insert(11)
    q_obj.insert(6)
    print('heap invariant', q_obj.check_recursive_heap_invariant())
    q_obj.disp()
    q_obj.insert(12)
    q_obj.insert(8)
    q_obj.check_heap_invariant()
    print('heap invariant', q_obj.check_recursive_heap_invariant())
    q_obj.disp()
    q_obj.insert(7)
    q_obj.insert(14)
    print('heap invariant', q_obj.check_recursive_heap_invariant())
    q_obj.insert(19)
    q_obj.insert(13)
    q_obj.insert(12)
    q_obj.insert(5)
    print('heap invariant', q_obj.check_recursive_heap_invariant())
    q_obj.disp()
    q_obj.remove(11)  # remove first found 10
    print('heap invariant', q_obj.check_recursive_heap_invariant())
    q_obj.disp()
    q_obj.poll()  # remove root element
    print('heap invariant', q_obj.check_recursive_heap_invariant())
    q_obj.disp()
    q_obj.remove(10)  # remove first found 10
    print('heap invariant', q_obj.check_recursive_heap_invariant())
    q_obj.poll()  # remove root element
    print('heap invariant', q_obj.check_recursive_heap_invariant())
    q_obj.disp()
    print('again inserting.....')
    q_obj.insert(1)
    q_obj.insert(20)
    print('heap invariant', q_obj.check_recursive_heap_invariant())
    q_obj.check_heap_invariant()
    q_obj.disp()
