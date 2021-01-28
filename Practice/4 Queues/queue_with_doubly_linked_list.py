'''
implementing a doubly linkedlist with a queue
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        node = Node(data)
        if self.size < 1:
            self.head = node
            self.tail = node
        else:
            # go to the tail, insert there
            last_node = self.tail
            last_node.next = node
            node.prev = last_node
            self.tail = node
        self.size += 1

    def add_first(self, data):
        node = Node(data)
        if self.size < 1:
            self.head = node
            self.tail = node
        else:
            cur_head = self.head
            cur_head.prev = node
            node.next = cur_head
            self.head = node
        self.size += 1

    def add_last(self, data):
        self.add(data)

    def peek_first(self):
        if self.size > 0:
            return self.head
        raise RuntimeError("check size")

    def peek_last(self):
        if self.size > 0:
            return self.last
        raise RuntimeError("check size")

    def remove_first(self):
        if self.size < 1:
            raise RuntimeError("check size")
        cur_head = self.head
        next_node = cur_head.next
        self.head = next_node
        next_node.prev = None
        self.size -= 1

    def remove_last(self):
        if self.size < 1:
            raise RuntimeError("check size")
        cur_tail = self.tail
        prev_node = cur_tail.prev
        self.tail = prev_node
        prev_node.next = None
        self.size -= 1

    def remove(self, data):
        cur_node = self.head
        cur_pointer = 0
        while cur_node is not None:
            if cur_node.data == data:
                if cur_pointer == 0:
                    # remoev first
                    self.remove_first()
                    break
                elif cur_pointer == self.size -1:
                    # remove last
                    self.remove_last()
                    break
                else:
                    # note down cur_node prev and next node
                    prev_node = cur_node.prev
                    next_node = cur_node.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    cur_node = None
                    break
            cur_node = cur_node.next
            cur_pointer += 1

    def remove_at(self, index):
        if index < 0:
            raise RuntimeError("check index")
        cur_pointer = 0
        cur_node = self.head
        while cur_node is not None:
            if index == cur_pointer:
                self.remove(cur_node.data)
                break
            cur_node = cur_node.next
            cur_pointer += 1

    def clear(self):
        cur_node = self.head
        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = None
            cur_node.prev = None
            cur_node = next_node
        self.size = 0
        self.head = None
        self.tail = None

    def get_index(self, data):
        cur_node = self.head
        index = -1
        while cur_node is not None:
            if cur_node.data == data:
                return index + 1
            index += 1
        return index

    def contains(self, data):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data == data:
                return True
            cur_node = cur_node.next
        return False

    def get_size(self):
        return self.size

    def print_all(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data, end=' ')
            cur_node = cur_node.next
        print()


if __name__=='__main__':
    dll = DoublyLinkedList()
    dll.add(1)
    dll.add(2)
    dll.add(3)
    dll.add(4)
    dll.add(5)
    dll.print_all()
    dll.add_first(3)
    dll.print_all()
    dll.remove_first()
    dll.print_all()
    dll.remove_at(2)
    dll.print_all()
    print(dll.get_size())
    print(dll.contains(5))
    print(dll.contains(10))
    dll.clear()
    dll.print_all()
    print(dll.get_size())
    print('---done---')