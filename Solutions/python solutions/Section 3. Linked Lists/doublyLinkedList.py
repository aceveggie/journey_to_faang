class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def get_node(self, index):
        current = self.first
        i=0
        while i<index:
            if current is None: 
                return None
            current = current.next
            i = i+1

        return current

    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node

        if ref_node.next is None:
            self.last = new_node
        else:
            new_node.next = ref_node.next
            new_node.next.prev = new_node
        
        ref_node.next = new_node

    def insert_before(self, ref_node, new_node):
        new_node.next = ref_node

        if ref_node.prev is None:
            self.first = new_node
        else:
            new_node.prev = ref_node.prev
            new_node.prev.next = new_node
        
        ref_node.prev = new_node

    def insert_at_beg(self, new_node):
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.insert_before(self.first, new_node)

    def insert_at_end(self, new_node):
        if self.last is None:
            self.first = new_node
            self.last = new_node
        else:
            self.insert_after(self.last, new_node)

    def remove(self, node):
        if node.prev is None:
            self.first = node.next
        else:
            node.prev.next = node.next
        
        if node.next is None:
            self.last = node.prev
        else:
            node.next.prev = node.prev
    
    def display(self):
        current = self.first
        while current:
            print(current.data, end = ' ')
            current = current.next

dlList = doublyLinkedList()

print('Menu')
print('insert <data> after <index>')
print('insert <data> before <index>')
print('insert <data> at beg')
print('insert <data> at end')
print('remove <index>') 
print('quit')

while True:
    print('The list: ', end = '')
    dlList.display()

    print()
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()

    if operation == 'insert':
        data = int(do[1])
        position = do[3].strip().lower()

        new_node = Node(data)

        suboperation = do[2].strip().lower()

        if suboperation == 'at':
            if position == 'beg':
                dlList.insert_at_beg(new_node)
            if position == 'end':
                dlList.insert_at_end(new_node)
        else:
            index = int(position)
            ref_node = dlList.get_node(index)
            if ref_node is None:
                print('No such index...')
                continue
            if suboperation == 'after':
                dlList.insert_after(ref_node, new_node)
            if suboperation == 'before':
                dlList.insert_before(ref_node, new_node)

    elif operation == 'remove':
        index = int(do[1])
        node = dlList.get_node(index)
        if node is None:
            print("No such index...")
            continue
        dlList.remove(node)

    elif operation == 'quit':
        break