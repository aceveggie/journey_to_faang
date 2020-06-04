class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.index = None

class BinarySearchTree:
    def __init__(self):
        self.root_node = None
        self.current_node = None
        self.node_array = []

    def insert(self, new_node):

        if self.root_node is None:
            new_node.index = 0
            self.root_node = new_node
            self.current_node = self.root_node
        else:

            while True:
                if self.current_node.data <= new_node.data:
                    if self.current_node.rightChild == None:
                        new_node.index = 2*int(self.current_node.index)+2
                        self.current_node.rightChild = new_node
                        break
                    else:
                        self.current_node = self.current_node.rightChild

                if self.current_node.data > new_node.data:
                    if self.current_node.leftChild == None:
                        new_node.index = 2*int(self.current_node.index)+1
                        self.current_node.leftChild = new_node
                        break
                    else:
                        self.current_node = self.current_node.leftChild

            self.current_node = self.root_node
        self.node_array.append([new_node.data, new_node.index])

    def remove(self, p):
        p_node = self.find(p)
        print(p_node.data)
        print(p_node.index)

    def find(self, p):

        self.current_node = self.root_node

        if self.root_node.data == p:
            return self.root_node

        else:
            while True:
                if self.current_node.data < p:
                    if self.current_node.rightChild.data == p:
                        return self.current_node.rightChild
                    else:
                        self.current_node = self.current_node.rightChild

                if self.current_node.data > p:
                    if self.current_node.leftChild.data == p:
                        return self.current_node.leftChild
                    else:
                        self.current_node = self.current_node.leftChild
                
                if self.current_node.data == p:
                    return self.current_node
            
            self.current_node = self.root_node
    
    def display_BST(self):
        length_exceeded = False
        tracker = 1
        last_queue_index = 0

        while True:
            for i in range(last_queue_index, tracker):
                if i == len(self.node_array):
                    length_exceeded = True
                    break
                else:
                    print(self.node_array[i], end=',')
            if length_exceeded:
                break
            else:
                last_queue_index=tracker
                tracker=tracker*2+1
                print("")

BST = BinarySearchTree()

print('Menu')
print('insert <data>')
print('remove <data>')
print('quit')

while True:
    print('The Queue: ')
    BST.display_BST()
    print()
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()

    if operation == 'insert':
        data = int(do[1])

        new_element = Node(data)
        BST.insert(new_element)

    if operation == 'remove':
        data = int(do[1])
        BST.remove(data)

    elif operation == 'quit':
        break