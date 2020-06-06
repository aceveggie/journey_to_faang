"""
My implementation of dynamic array
"""


class DynArray:
    def __init__(self, max_size=2):
        self.max_size = max_size
        self.array = [None]*self.max_size

    def insert(self, value, index):
        # check if inserting will exceed size
        # if not, copy the values to right
        # insert at given index, the value
        # if exceeds, double the size
        # copy the values appropriately
        # insert the values
        pass

    def remove(self, value):
        # remove the value
        pass

    def append(self):
        # check if appending will exceed size
        # if not, insert at end
        pass

    def get_max_size(self):
        return self.max_size

    def __check_if_full(self):
        # check if current size == max size of array
        pass

    def __change_size(self):
        # lets create a new array with double the max_size of current array
        # copy over the elements
        pass


if __name__ == "__main__":
    array = DynArray()
