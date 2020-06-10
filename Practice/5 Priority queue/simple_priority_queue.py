'''
    Implement simple priority queue
'''


class Node:
    def __init__(self, data_val):
        self.data = data_val

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class SimplePriorityQueue:
    def __init__(self):
        self.size = 0


if __name__ == "__main__":
    q_obj = SimplePriorityQueue()
