class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.node_count = 0
        self.root = None

    def get_size(self):
        return self.node_count

    def is_empty(self):
        return self.get_size() == 0

    def get_height(self):
        return 0

    def get_node_height(self):
        pass

    def add(self, data):
        pass

    def _add_to_node(self, node, data):
        pass            

    def remove(self, data):
        pass

    def remove_from_node(self, node, data):
        pass

    def find_min(self):
        pass

    def find_max(self):
        pass

    def contains(self):
        return False

    def pre_order_traversal(self):
        pass

    def in_order_traversal(self):
        pass

    def post_order_traversal(self):
        pass

    def level_order_traversal(self):
        pass


if __name__=="__main__":
    pass
