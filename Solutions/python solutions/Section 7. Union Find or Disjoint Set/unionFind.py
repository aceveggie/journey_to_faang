class Element:
    def __init__(self, data = None):
        self.data = data
        self.root = data
        self.comp_index = 0
        self.comp_size = 1
        self.children = []

class Component: 
    def __init__(self, com):
        self.comp_array = []
        self.size = 0

class UnionFind:
    def __init__(self):
        self.superSet = []
        self.components = []
        self.numOfComp = 0

    def set_push(self, new_element):
        self.superSet.append(new_element)
        self.components.append(new_element.data)
        new_element.comp_index = len(self.components)-1
        new_element.children = [new_element]
        self.numOfComp += 1
    
    def find(self, el):
        for elem in self.superSet:
            print(elem.data)
            if elem.data == el:
                return elem
    
    def unify(self, p, q):
        el1 = self.find(p)
        el2 = self.find(q)

        if (el1.root == el1.data and el2.root == el2.data):
            if len(el1.children) > len(el2.children):
                el2.root = el1
                el1.children.append(el2)

                for i in range(len(el1.children)):
                    el1.children[i].comp_size = len(el1.children)
            elif len(el1.children) < len(el2.children):
                el1.root = el2
                el2.children.append(el1)

                for i in range(len(el2.children)):
                    el2.children[i].comp_size = len(el2.children)
            else:
                el2.root = el1
                el1.children.append(el2)

                for i in range(len(el1.children)):
                    el1.children[i].comp_size = len(el1.children)
            
            for child in el1.children:
                print(child.data)

        elif (el1.root == el1.data and el2.root != el2.data):
            if el2.root.root == el2.root.data:
                el1.root = el2.root
                el2.root.children.append(el1)

                for i in range(len(el2.root.children)):
                    el2.root.children[i].comp_size = len(el2.root.children)

            for child in el2.root.children:
                print(child.data)
        
        elif (el2.root == el2.data and el1.root != el1.data):
            if el1.root.root == el1.root.data:
                el2.root = el1.root

                # el2.comp_size += 2
                # el1.comp_size += 1
                # el1.root.comp_size += 1
                el1.root.children.append(el2)

                for i in range(len(el1.root.children)):
                    el1.root.children[i].comp_size = len(el1.root.children)
            
            for child in el1.root.children:
                print(child.data)

        elif (el1.root.root == el1.root.data and el2.root.root == el2.root.data):
            length1 = len(el1.root.children)
            length2 = len(el2.root.children)
            if length1 > length2:
                print(length1)
                        # for i in range(len(el2.root.children)):
                        #     el2.root.children[i].root = el1.root
                        #     el1.root.children.append(el2.root.children[i])
                        # for i in range(len(el1.root.children)):
                        #     el1.root.children[i].comp_size = length1 + length2
                    
                    # el2.root = el1.root

                    # el2.comp_size += 2
                    # el1.comp_size += 1
                    # el1.root.comp_size += 1
                    # el1.root.children.append(el2)

                    # for i in range(len(el1.root.children)):
                    #     el1.root.children[i].comp_size = len(el1.root.children)
            # for child in el1.root.children:
            #     print(child.data)

        self.numOfComp -= 1

    def display_superSet(self):
        for ele in self.superSet:
            print('data: '+str(ele.data), end = ', ')
            if isinstance(ele.root, int):
                print('root: '+str(ele.root), end=", ")
                print('comp_size: '+str(ele.comp_size))
            else:
                print('root: (data: '+str(ele.root.data), end = ', ')
                print('root: '+str(ele.root.root), end=", ")
                print('comp_size: '+str(ele.comp_size)+')')

        # print(self.components)

unionFind = UnionFind()

for i in range(10):
    new_element = Element(i)
    unionFind.set_push(new_element)

print('Menu')
print('push <element>')
print('unify <el1> and <el2>')
print('quit')

while True:
    print('The Queue: ')
    unionFind.display_superSet()
    print()
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()

    if operation == 'push':
        data = int(do[1])

        new_element = Element(data)
        unionFind.set_push(new_element)
    
    elif operation == 'unify':
        el1 = int(do[1])
        el2 = int(do[3])

        unionFind.unify(el1, el2)

    elif operation == 'quit':
        break