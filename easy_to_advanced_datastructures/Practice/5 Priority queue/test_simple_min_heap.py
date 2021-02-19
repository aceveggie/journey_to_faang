import heapq
import unittest
import random

from min_heap_practice import SimpleMinHeap

class TestSimplePriorityQueue(unittest.TestCase):
    def test_empty(self):
        '''
        check size
        '''
        min_heap = SimpleMinHeap()
        self.assertEqual(min_heap.get_size(), 0)
        self.assertEqual(min_heap.poll(), None)
        self.assertEqual(min_heap.peek(), None)

    def test_heap_property(self):
        '''
        check order in which we poll is always right
        '''
        min_heap = SimpleMinHeap()
        q_list = [9,8,7,6,5,4,3,2,1]
        for each in q_list:
            min_heap.insert(each)
        min_heap.disp()
        for each in q_list[::-1]:
            self.assertEqual(each, min_heap.poll())

    def test_heapify(self):
        '''
        check current custom pq/min heap with built-in python priority queue
        '''
        min_heap = SimpleMinHeap()
        q_list = [9,8,4,3,2,7,6,5,1]
        for each in q_list:
            min_heap.insert(each)
        min_heap.disp()
        import heapq
        hq_list = q_list.copy()
        heapq.heapify(hq_list)
        for i in range(9):
            x = heapq.heappop(hq_list)
            y = min_heap.poll()
            print(x, y)
        self.assertEqual(x, y)

    def test_clear(self):
        min_heap = SimpleMinHeap()
        q_list = ["aa", "bb", "cc", "dd", "ee"]
        for i in q_list:
            min_heap.insert(i)
        min_heap.disp()
        min_heap.clear()
        self.assertEqual(min_heap.get_size(), 0)

    def test_contains(self):
        min_heap = SimpleMinHeap()
        q_list = ["aa", "bb", "cc", "dd", "ee"]
        for i in q_list:
            min_heap.insert(i)
        min_heap.disp()
        min_heap.poll()
        self.assertEqual(min_heap.contains('aa'), False)
        min_heap.poll()
        self.assertEqual(min_heap.contains('bb'), False)
        min_heap.poll()
        self.assertEqual(min_heap.contains('cc'), False)
        min_heap.poll()
        self.assertEqual(min_heap.contains('dd'), False)
        min_heap.poll()
        self.assertEqual(min_heap.contains('ee'), False)
    def test_containment_randomized(self):
        for i in range(100):
            min_heap = SimpleMinHeap()
            q_list = list(range(100))
            random.shuffle(q_list)
            #q_list shuffled now
            # insert into custom heap
            for i in q_list:
                min_heap.insert(i)
            hq_list = q_list.copy()
            heapq.heapify(hq_list)
            for i in range(9):
                x = heapq.heappop(hq_list)
                y = min_heap.poll()
                y_exists_in_minheap = min_heap.contains(y)
                try:
                    x_exists_in_hqlist = hq_list.index(x)
                    x_exists_in_hqlist = True
                except:
                    x_exists_in_hqlist = False
                self.assertEqual(x_exists_in_hqlist, y_exists_in_minheap)


if __name__=='__main__':
    unittest.main()