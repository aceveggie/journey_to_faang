import unittest
from union_find import UnionFind


class TestUnionFunctions(unittest.TestCase):
    def test_num_components(self):
        uf = UnionFind(5)
        self.assertEqual(uf.get_num_components(), 5)
        uf.union(0, 1)
        self.assertEqual(uf.get_num_components(), 4)
        uf.union(1, 0)
        self.assertEqual(uf.get_num_components(), 4)
        uf.union(1, 2)
        self.assertEqual(uf.get_num_components(), 3)
        uf.union(0, 2)
        self.assertEqual(uf.get_num_components(), 3)
        uf.union(2, 1)
        self.assertEqual(uf.get_num_components(), 3)
        uf.union(3, 4)
        self.assertEqual(uf.get_num_components(), 2)
        uf.union(4, 3)
        self.assertEqual(uf.get_num_components(), 2)
        uf.union(1, 3)
        self.assertEqual(uf.get_num_components(), 1)
        uf.union(4, 0)
        self.assertEqual(uf.get_num_components(), 1)

    def test_rank_or_component_size(self):
        uf = UnionFind(5)
        self.assertEqual(uf.get_rank(0), 1)
        self.assertEqual(uf.get_rank(1), 1)
        self.assertEqual(uf.get_rank(2), 1)
        self.assertEqual(uf.get_rank(3), 1)
        self.assertEqual(uf.get_rank(4), 1)

        uf.union(0, 1)
        self.assertEqual(uf.get_rank(0), 2)
        self.assertEqual(uf.get_rank(1), 2)
        self.assertEqual(uf.get_rank(2), 1)
        self.assertEqual(uf.get_rank(3), 1)
        self.assertEqual(uf.get_rank(4), 1)

        uf.union(1, 0)
        self.assertEqual(uf.get_rank(0), 2)
        self.assertEqual(uf.get_rank(1), 2)
        self.assertEqual(uf.get_rank(2), 1)
        self.assertEqual(uf.get_rank(3), 1)
        self.assertEqual(uf.get_rank(4), 1)

        uf.union(1, 2)
        self.assertEqual(uf.get_rank(0), 3)
        self.assertEqual(uf.get_rank(1), 3)
        self.assertEqual(uf.get_rank(2), 3)
        self.assertEqual(uf.get_rank(3), 1)
        self.assertEqual(uf.get_rank(4), 1)

        uf.union(0, 2)
        self.assertEqual(uf.get_rank(0), 3)
        self.assertEqual(uf.get_rank(1), 3)
        self.assertEqual(uf.get_rank(2), 3)
        self.assertEqual(uf.get_rank(3), 1)
        self.assertEqual(uf.get_rank(4), 1)

        uf.union(2, 1)
        self.assertEqual(uf.get_rank(0), 3)
        self.assertEqual(uf.get_rank(1), 3)
        self.assertEqual(uf.get_rank(2), 3)
        self.assertEqual(uf.get_rank(3), 1)
        self.assertEqual(uf.get_rank(4), 1)

        uf.union(3, 4)
        self.assertEqual(uf.get_rank(0), 3)
        self.assertEqual(uf.get_rank(1), 3)
        self.assertEqual(uf.get_rank(2), 3)
        self.assertEqual(uf.get_rank(3), 2)
        self.assertEqual(uf.get_rank(4), 2)

        uf.union(4, 3)
        self.assertEqual(uf.get_rank(0), 3)
        self.assertEqual(uf.get_rank(1), 3)
        self.assertEqual(uf.get_rank(2), 3)
        self.assertEqual(uf.get_rank(3), 2)
        self.assertEqual(uf.get_rank(4), 2)

        uf.union(1, 3)
        self.assertEqual(uf.get_rank(0), 5)
        self.assertEqual(uf.get_rank(1), 5)
        self.assertEqual(uf.get_rank(2), 5)
        self.assertEqual(uf.get_rank(3), 5)
        self.assertEqual(uf.get_rank(4), 5)

        uf.union(4, 0)
        self.assertEqual(uf.get_rank(0), 5)
        self.assertEqual(uf.get_rank(1), 5)
        self.assertEqual(uf.get_rank(2), 5)
        self.assertEqual(uf.get_rank(3), 5)
        self.assertEqual(uf.get_rank(4), 5)

    def test_size(self):
        uf = UnionFind(5)
        self.assertEqual(uf.get_size(), 5)
        uf.union(0, 1)
        uf.find(3)
        self.assertEqual(uf.get_size(), 5)
        uf.union(1, 2)
        self.assertEqual(uf.get_size(), 5)
        uf.union(0, 2)
        uf.find(1)
        self.assertEqual(uf.get_size(), 5)
        uf.union(2, 1)
        self.assertEqual(uf.get_size(), 5)
        uf.union(3, 4)
        uf.find(0)
        self.assertEqual(uf.get_size(), 5)
        uf.union(4, 3)
        uf.find(3)
        self.assertEqual(uf.get_size(), 5)
        uf.union(1, 3)
        self.assertEqual(uf.get_size(), 5)
        uf.find(2)
        uf.union(4, 0)
        self.assertEqual(uf.get_size(), 5)

    def test_connectivity(self):
        sz = 7
        uf = UnionFind(sz)

        for i in range(sz):
            self.assertTrue(uf.connected(i, i))

        uf.union(0, 2)

        self.assertTrue(uf.connected(0, 2))
        self.assertTrue(uf.connected(2, 0))

        self.assertFalse(uf.connected(0, 1))
        self.assertFalse(uf.connected(3, 1))
        self.assertFalse(uf.connected(6, 4))
        self.assertFalse(uf.connected(5, 0))

        for i in range(sz):
            self.assertTrue(uf.connected(i, i))

        uf.union(3, 1)

        self.assertTrue(uf.connected(0, 2))
        self.assertTrue(uf.connected(2, 0))
        self.assertTrue(uf.connected(1, 3))
        self.assertTrue(uf.connected(3, 1))

        self.assertFalse(uf.connected(0, 1))
        self.assertFalse(uf.connected(1, 2))
        self.assertFalse(uf.connected(2, 3))
        self.assertFalse(uf.connected(1, 0))
        self.assertFalse(uf.connected(2, 1))
        self.assertFalse(uf.connected(3, 2))

        self.assertFalse(uf.connected(1, 4))
        self.assertFalse(uf.connected(2, 5))
        self.assertFalse(uf.connected(3, 6))

        for i in range(sz):
            self.assertTrue(uf.connected(i, i))

        uf.union(2, 5)
        self.assertTrue(uf.connected(0, 2))
        self.assertTrue(uf.connected(2, 0))
        self.assertTrue(uf.connected(1, 3))
        self.assertTrue(uf.connected(3, 1))
        self.assertTrue(uf.connected(0, 5))
        self.assertTrue(uf.connected(5, 0))
        self.assertTrue(uf.connected(5, 2))
        self.assertTrue(uf.connected(2, 5))

        self.assertFalse(uf.connected(0, 1))
        self.assertFalse(uf.connected(1, 2))
        self.assertFalse(uf.connected(2, 3))
        self.assertFalse(uf.connected(1, 0))
        self.assertFalse(uf.connected(2, 1))
        self.assertFalse(uf.connected(3, 2))

        self.assertFalse(uf.connected(4, 6))
        self.assertFalse(uf.connected(4, 5))
        self.assertFalse(uf.connected(1, 6))

        for i in range(sz):
            self.assertTrue(uf.connected(i, i))

        # Connect everything
        uf.union(1, 2)
        uf.union(3, 4)
        uf.union(4, 6)

        for i in range(sz):
            for j in range(sz):
                # print(i, j, uf.connected(i, j))
                self.assertTrue(uf.connected(i, j))

    @unittest.expectedFailure
    def test_negative_sizes(self):
        uf = UnionFind(-1)
        uf.unify(1, 2)

    @unittest.expectedFailure
    def test_zero_size(self):
        uf = UnionFind(0)
        uf.unify(1, 2)


if __name__ == '__main__':
    unittest.main()
