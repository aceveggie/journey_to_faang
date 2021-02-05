'''
implement as stack using doubly linked list
'''
import gc


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Stack:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        self.pointer = self.head

    def push(self, data):
        '''
            pushes to top of the stack O(1)
        '''
        new_node = Node(data)
        # if empty, make new node as head
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # take current head, update head and pointers
            if self.size == 0:
                self.tail = new_node
            cur_head = self.head
            cur_head.prev = new_node
            new_node.next = cur_head
            self.head = new_node
        self.size += 1

    def pop(self):
        '''
            pops the head of the stack O(1)
        '''
        # if empty, return
        if self.is_empty():
            return
        if self.size == 1:
            self.tail = None
        # get head
        # get next node
        # make next node the head
        cur_head = self.head
        next_node = cur_head.next
        if next_node is not None:
            next_node.prev = None
        self.head = next_node
        cur_head = None
        self.size -= 1

    def is_empty(self):
        '''
        checks currents size of the stack
        O(1)
        '''
        if self.size <= 0:
            return True
        return False

    def peek_head(self):
        '''
        returns top of the stack O(1)
        '''
        if self.is_empty():
            print('empty stack')
            return
        return self.head.data

    def peek_tail(self):
        '''
        returns bottom of the stack O(1)
        '''
        if self.is_empty():
            print('empty stack')
            return
        return self.tail.data

    def print_all_forward(self):
        '''
        prints the entire stack O(N)
        '''
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data, end=', ')
            cur_node = cur_node.next
        print('')

    def print_all_reverse(self):
        '''
        iterates using link nodes backwards O(N)
        '''
        # get tail, iterate backwards using link nodes
        cur_node = self.tail
        while cur_node is not None:
            print(cur_node.data, end=', ')
            cur_node = cur_node.prev
        print()


if __name__ == '__main__':
    stack_obj = Stack()
    stack_obj.push(1)
    stack_obj.print_all_forward()
    stack_obj.push(2)
    stack_obj.print_all_forward()
    stack_obj.push(3)
    stack_obj.print_all_forward()
    stack_obj.push(4)
    stack_obj.print_all_forward()
    stack_obj.push(5)
    stack_obj.print_all_forward()
    stack_obj.pop()
    stack_obj.print_all_forward()
    stack_obj.push(0)
    stack_obj.print_all_forward()
    stack_obj.print_all_reverse()
    stack_obj.pop()
    stack_obj.print_all_forward()
    stack_obj.pop()
    stack_obj.print_all_forward()
    print('head', stack_obj.peek_head())
    print('tail', stack_obj.peek_tail())
    stack_obj.print_all_reverse()
    stack_obj.pop()
    stack_obj.print_all_forward()
    stack_obj.print_all_reverse()
    stack_obj.pop()
    stack_obj.print_all_forward()
    stack_obj.print_all_reverse()
    stack_obj.pop()
    stack_obj.print_all_forward()
    stack_obj.pop()
    stack_obj.print_all_reverse()
    stack_obj.print_all_forward()
    stack_obj.print_all_reverse()
    stack_obj.push(10)
    stack_obj.print_all_forward()
    print('head', stack_obj.peek_head())
    print('tail', stack_obj.peek_tail())
    stack_obj.push(9)
    stack_obj.print_all_forward()
    print('head', stack_obj.peek_head())
    print('tail', stack_obj.peek_tail())
    gc.collect()
