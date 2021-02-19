'''
In this implementation, we don't store node itself.

Whenever, the class is instantiated, we create the data nodes (to be grouped)
with a given range.

E.g UnionFind(5), will create data nodes
from 0, 1, 2, 3, 4

NOTE: Index/Position in the list indicates the value itself.

We can certainly have a different implementation where we add custom
value
'''


class UnionFind:
    def __init__(self, size):
        if size == 0:
            raise ValueError("size cannot be zero", size)
        # assign size
        self.size = size

        # total number of components = total number of elements initially
        # later this number will reduce over time whenever there is merge/union
        # operation
        self.num_components = size

        # to store root node of every node
        # index/Position in the list indicates node value
        self.root_list = [0]*size

        # to store rank of each node
        # index/Position in the list indicates node value
        self.rank_list = [0]*size

        # list of indices
        self.rode_list = list(range(size))

        # instantiate the root_list and rank_list
        # index/position in the
        for i in range(self.size):
            # every node to itself initially. Later rank will be increased as
            # more nodes are added
            self.rank_list[i] = 1
            # every node points to itself initally.
            self.root_list[i] = i

    def find(self, node_a):
        '''
        Finds root node of A.
        After finding the root node, all the nodes in the path are
        compressed to point to root node (Path Compression)
        '''
        # while root_list item is not pointing to itself
        root_node = node_a

        while root_node != self.root_list[root_node]:
            root_node = self.root_list[root_node]

        # now do path compression, by re-tracing same path as above
        while self.root_list[node_a] != root_node:
            parent_node = self.root_list[node_a]
            # modify root node to obtained root_node (previously)
            self.root_list[node_a] = root_node
            node_a = parent_node
        return root_node

    def connected(self, node_a, node_b):
        return self.find(node_a) == self.find(node_b)

    def get_size(self):
        return self.size

    def get_num_components(self):
        return self.num_components

    def get_rank(self, node_a):
        root_node = self.find(node_a)
        return self.rank_list[root_node]

    def union(self, node_a, node_b):
        root_a = self.find(node_a)
        root_b = self.find(node_b)
        if root_a == root_b:
            # no merge required
            # if we merge, loop will be created
            return
        # one of the parents is different
        # merge lower ranked node into the bigger group
        # NOTE:  only check rank of root nodes, not given node
        if self.rank_list[root_a] < self.rank_list[root_b]:
            # merge node_a into node_b
            # i.e. make node_b, parent of node_a
            self.rank_list[root_b] += self.rank_list[root_a]
            self.root_list[root_a] = root_b

        else:
            # merge node_b into node_a
            # i.e. make node_a, parent of node_b
            self.rank_list[root_a] += self.rank_list[root_b]
            self.root_list[root_b] = root_a

        self.num_components -= 1


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
