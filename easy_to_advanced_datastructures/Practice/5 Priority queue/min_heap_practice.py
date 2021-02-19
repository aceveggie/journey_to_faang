'''
implementation of min heap
'''

class SimpleMinHeap:
    def __init__(self):
        self.array = []
        self.heap_size = self.heap_capacity = 0

    def remove(self, val):
        '''
        '''
        val_idx = None
        for idx, i in enumerate(self.array):
            if i == val:
                val_idx = idx
                break

        # if found, remove it
        if val_idx:
            self.remove_at(val_idx)

    def poll(self):
        '''
        remove root value, take leaf node, overwrite root_node, bubble down
        '''
        try:
            return self.remove_at(0)
        except:
            return None

    def peek(self):
        try:
            return self.array[0]
        except Exception:
            return None

    def clear(self):
        self.array = []
        self.heap_capacity = self.heap_size = 0
    def contains(self, val):
        '''
        O(N)
        '''
        try:
            idx = self.array.index(val)
            return True
        except Exception:
            return False


    def remove_at(self, k):
        if k == 0:
            # poll operation k=0, remove at root
            leaf_val = self.array[-1]
            removed_item = self.array[0]
            self.array[0] = leaf_val
            self.array.pop()
            self.heap_size = len(self.array)
            self.bubble_down(k)
            return removed_item
        elif k == self.heap_size -1:
            # remove at leaf
            removed_item =self.array.pop()
            self.heap_size = len(self.array)
            self.bubble_down(k)
            return removed_item
        else:
            # swap with leaf val, bubble up and bubble down
            leaf_val = self.array[-1]
            removed_item = self.array[k]
            self.array[k] = leaf_val
            self.array.pop()
            self.heap_size = len(self.array)
            self.bubble_down(k)
            self.bubble_up(k)
            return removed_item
    def insert(self, val):
        '''
        insert at leaf, bubble up.
        '''
        self.array.append(val)
        self.heap_size = len(self.array)
        if len(self.array) == 1:
            return True
        k = len(self.array) - 1
        self.bubble_up(k)

    def bubble_up(self, k=0):
        '''
        '''
        while self.check_heap_invariant() is False:
            par_idx = self.get_parent_index(k)
            cur_val = self.array[k]
            if par_idx is None:
                break
            if self.array[par_idx] > cur_val:
                self.swap_vals_using_indices(par_idx, k)
                k, par_idx = par_idx, k

    def bubble_down(self, k=0):
        while self.check_heap_invariant() is False:
            cur_val = self.array[k]
            l_idx = self.get_lchild_index(k)
            r_idx = self.get_rchild_index(k)
            try:
                l_val = self.array[l_idx]
                r_val = self.array[r_idx]
            except:
                if len(self.array) == 2:
                    self.swap_vals_using_indices(0, 1)
                    return
            if l_val <= r_val:
                self.swap_vals_using_indices(l_idx, k)
                k, l_idx = l_idx, k
            else:
                self.swap_vals_using_indices(r_idx, k)
                k, r_idx = r_idx, k


    def check_iterative_heap_invariant(self):
        for idx, cur_val in enumerate(self.array):
            l_idx = self.get_lchild_index(idx)
            r_idx = self.get_rchild_index(idx)
            if l_idx:
                l_val = self.array[l_idx]
                if l_val < cur_val:
                    return False
            if r_idx:
                r_val = self.array[r_idx]
                if r_val < cur_val:
                    return False
        return True

    def check_heap_invariant(self, idx=0):
        if idx >= self.heap_size:
            return True
        l_idx = (2*idx) + 1
        r_idx = (2*idx) + 2
        if (l_idx < self.heap_size) and (self.array[l_idx] < self.array[idx]):
            return False
        if (r_idx < self.heap_size) and (self.array[r_idx] < self.array[idx]):
            return False

        return self.check_heap_invariant(l_idx) and\
            self.check_heap_invariant(r_idx)

    def get_parent_index(self, k):
        idx = (k-1)//2
        if idx >= 0 and idx < len(self.array):
            return idx
        return None
    def get_lchild_index(self, k):
        l_idx = (2*k)+1
        if l_idx >= 0 and l_idx < len(self.array):
            return l_idx
        return None
    def get_rchild_index(self, k):
        r_idx = (2*k)+2
        if r_idx >= 0 and r_idx < len(self.array):
            return r_idx
        return None
    def swap_vals_using_indices(self, j, k):
        self.array[j], self.array[k] = self.array[k], self.array[j]

    def disp(self):
        for i in self.array:
            print(i, end=', ')
        print()

    def get_size(self):
        return self.heap_size



if __name__=='__main__':
    min_heap = SimpleMinHeap()
    min_heap.insert(11)
    min_heap.insert(6)
    print('heap invariant', min_heap.check_heap_invariant())
    min_heap.disp()
    min_heap.insert(12)
    min_heap.insert(8)
    min_heap.check_heap_invariant()
    print('heap invariant', min_heap.check_heap_invariant())
    min_heap.disp()
    min_heap.insert(7)
    min_heap.insert(14)
    print('heap invariant', min_heap.check_heap_invariant())
    min_heap.disp()
    min_heap.insert(19)
    min_heap.insert(13)
    min_heap.insert(12)
    min_heap.insert(5)
    print('heap invariant', min_heap.check_heap_invariant())
    min_heap.disp()
    min_heap.remove(11)  # remove first found 11
    print('heap invariant', min_heap.check_heap_invariant())
    min_heap.disp()
    min_heap.poll()  # remove root element
    print('heap invariant', min_heap.check_heap_invariant())
    min_heap.disp()
    min_heap.remove(10)  # remove first found 10
    print('heap invariant', min_heap.check_heap_invariant())
    min_heap.disp()
    min_heap.poll()  # remove root element
    print('heap invariant', min_heap.check_heap_invariant())
    min_heap.disp()
    print('again inserting.....')
    min_heap.insert(1)
    min_heap.insert(20)
    print('heap invariant', min_heap.check_heap_invariant())
    min_heap.check_heap_invariant()
    min_heap.disp()