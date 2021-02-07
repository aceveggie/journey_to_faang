'''
Union find DS
'''

class UnionFind:
    def __init__(self, size):
        '''
        '''
        self.size = size
        self.num_components = size
        self.root_list = list(range(size))
        self.size_list = [1]*size

    def union(self, node1, node2):
        '''
        '''
        if self.connected(node1, node2):
            return
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        size1 = self.size_list[node1]
        size2 = self.size_list[node2]
        if size1 <= size2:
            # merge size1 into size2
            self.size_list[parent2] += self.size_list[parent1]
            self.root_list[parent1] = parent2
        else:
            self.size_list[parent1] += self.size_list[parent2]
            self.root_list[parent2] = parent1
        self.num_components -= 1

    def find(self, node):
        '''
        '''
        root_node = node
        while root_node != self.root_list[root_node]:
            root_node = self.root_list[root_node]
        # perform path compression
        while root_node != self.root_list[node]:
            cur_root = self.root_list[node]
            self.root_list[node] = root_node
            node = cur_root
        return root_node

    def get_num_components(self):
        '''
        returns number of unique roots
        '''
        return self.num_components

    def connected(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        return parent1 == parent2

    def get_rank(self, node):
        parent1 = self.find(node)
        return self.size_list[parent1]

    def get_size(self):
        return self.size
    


if __name__ == "__main__":
    print('done')
    uf = UnionFind(5)
    print(uf.get_num_components(), 5, uf.get_num_components() == 5)
    uf.union(0, 1)
    print(uf.get_num_components(), 4, uf.get_num_components() == 4)
    uf.union(1, 0)
    print(uf.get_num_components(), 4, uf.get_num_components() == 4)
    uf.union(1, 2)
    print(uf.get_num_components(), 3, uf.get_num_components() == 3)

    uf.union(0, 2)
    print(uf.get_num_components(), 3, uf.get_num_components() == 3)

    uf.union(2, 1)
    print(uf.get_num_components(), 3, uf.get_num_components() == 3)

    uf.union(3, 4)
    print(uf.get_num_components(), 2, uf.get_num_components() == 2)

    uf.union(4, 3)
    print(uf.get_num_components(), 2, uf.get_num_components() == 2)

    uf.union(1, 3)
    print(uf.get_num_components(), 1, uf.get_num_components() == 1)

    uf.union(4, 0)
    print(uf.get_num_components(), 1, uf.get_num_components() == 1)