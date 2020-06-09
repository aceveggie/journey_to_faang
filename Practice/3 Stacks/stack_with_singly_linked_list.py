'''
implement a stack with a singly linked list
'''


class Node:
    '''
    simple singly node
    '''
    def __init__(self, data_val):
        self.data = data_val
        self.prev = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class SinglyLinkedListStack:
    '''
    Stack based on singly lnked list
    '''
    def __init__(self, data_val):
        self.head = Node(data_val)
        self.size = 0

    def push(self, data_val):
        new_node = Node(data_val)
        new_node.prev = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception("size is zero")
        cur_head = self.head
        del self.head
        self.head = cur_head.prev
        self.size -= 1
        return cur_head

    def peek(self):
        if self.size < 1:
            raise Exception("size is zero")
        return self.head

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    def print_all(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node, end=' ')
            cur_node = cur_node.prev
        print()

    def __iter__(self):
        '''
        make it iterable
        '''
        return self

    def __next__(self):
        '''
        make it iterable
        '''
        if self.head is None:
            raise StopIteration
        else:
            ret_node = self.head
            self.head = self.head.prev
            return ret_node


if __name__ == "__main__":
    stack_obj = SinglyLinkedListStack(10)
    stack_obj.push(20)
    stack_obj.push(30)
    stack_obj.push(40)
    #print(stack_obj.peek())
    stack_obj.print_all()
    # print('popping', stack_obj.pop())
    # stack_obj.print_all()
    # print('popping', stack_obj.pop())
    # stack_obj.print_all()
    # print('popping', stack_obj.pop())
    # stack_obj.print_all()
    # print('popping', stack_obj.pop())
    # stack_obj.print_all()
    # print(list(stack_obj))
    for each in stack_obj:
        print(each)
