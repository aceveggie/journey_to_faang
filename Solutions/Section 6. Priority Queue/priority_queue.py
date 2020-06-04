import math

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.index = None

class Heap:
    def __init__(self):
        self.lastNode = None
        self.firstNode = None
        self.queue = []
    
    def get_node(self, node):
        if self.lastNode == None:
            print('No data in queue!')

    # def swap(self):
    #     if self.lastNode.parent.data < self.lastNode.data:
    #         temp_node = self.lastNode
    #         self.lastNode = self.lastNode.parent
        
    #         temp_node = self.lastNode.parent
    #         temp_node.parent = self.lastNode
    #         self.lastNode.parent = self.lastNode.parent.parent
    #         self.lastNode = temp_node
            
        
    def heap_push(self, new_node):
        # print(new_node.data)
        self.queue.append(new_node.data)    
        if self.lastNode == None:
            self.lastNode = new_node
            self.firstNode = new_node
        else:
            if self.lastNode.left_child == None:
                self.lastNode.left_child = new_node
                self.lastNode.left_child.parent = self.lastNode
                self.lastNode = new_node
                
            else:
                self.lastNode.right_child = new_node
                self.lastNode.right_child.parent = self.lastNode
                self.lastNode = new_node
        # print(self.queue)

    def get_last_node(self):
        return self.lastNode

    def display_queue(self):
        length_exceeded = False
        tracker = 1
        last_queue_index = 0

        while True:
            for i in range(last_queue_index, tracker):
                if i == len(self.queue):
                    length_exceeded = True
                    break
                else:
                    print(self.queue[i], end=',')
            if length_exceeded:
                break
            else:
                last_queue_index=tracker
                tracker=tracker*2+1
                print("")

priority_queue = Heap()
# queue = []

print('Menu')
print('push <data>')
print('quit')

while True:
    print('The Queue: ')
    priority_queue.display_queue()
    print()
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()

    if operation == 'push':
        data = int(do[1])

        new_node = Node(data)
        priority_queue.heap_push(new_node)

    elif operation == 'quit':
        break