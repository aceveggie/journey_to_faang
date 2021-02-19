class Node:
    def __init__(self, data = None):
        self.data = data
        self.below = None

class Stack:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def push(self, node):
        current_head = self.get_head()
        self.head = node
        node.below = current_head
    
    def pop(self):
        current_head = self.get_head()
        self.head = current_head.below
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.below


newStack = Stack()

print('Menu')
print('push <data>')
print('pop')
print('quit')

while True:
    print('The Stack: ', end = '')
    newStack.display()

    print()
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()

    if operation == 'push':
        data = int(do[1])

        node = Node(data)

        newStack.push(node)
    
    if operation == 'pop':
        newStack.pop()
    
    if operation == 'quit':
        break
