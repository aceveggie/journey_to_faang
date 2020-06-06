"""
My implementation of dynamic array
"""


class DynArray:
    '''
    Implements Dyamic Array using simple python list
    '''
    def __init__(self, max_size=4):
        '''
            max_size of the given array
            Keyword arguments:
            max_size -- the maximum size of the array (default 4)
        '''
        self._max_size = max_size
        self._cur_size = 0
        self._array = [None]*self._max_size
        self._new_array = None

    def insert(self, index, value):
        '''
        inserts given value at a given index

        Keyword arguments:
        index -- integer index at which you want to insert value
        value -- given value to be inserted (can be int, float, string)
        '''

        # if index >= cur_size + 1
        if index > self._cur_size:
            print('check size of cur array before inserting')
            raise IndexError
        # check if current size is max size?
        is_full = self.__check_if_full()
        # increase size if max size
        if is_full:
            self.__increase_size()

        # copy the values to right
        # copy from right to left, if we copy from left to right, we
        # overwrite the existing values
        for i in reversed(range(index, self._cur_size+1)):
            self._array[i] = self._array[i-1]
        self._array[index] = value
        self._cur_size += 1

    def remove(self, value):
        '''
        removes the given value from dynamic array

        Keyword arguments:
        value -- given value to be removed
        '''

        # remove the value
        # udpate current size
        # check if empty
        if self.__check_if_empty():
            print('empty, no operations need to be done')
            return
        self._new_array = [None]*(self._max_size)
        _new_idx = 0
        for each in self._array:
            if each != value:
                self._new_array[_new_idx] = each
                _new_idx += 1
        self._array = self._new_array
        del self._new_array
        self._cur_size -= 1

    def get_val_at_index(self, index):
        '''
        retreives the value at a given index

        Keyword arguments:
        index -- index at which we want values
        '''

        # check if empty, return
        if (self._cur_size == 0) or (index > self._cur_size) or (index < 0):
            # print('array empty')
            # print('index > cur_size, no value exists at this index')
            # print('index can't be negative)
            return
        return self._array[index]

    def set_val_at_index(self, index, value):
        '''
        sets the value at a given index

        Keyword arguments:
        index -- index at which we want to set the value
        value -- value to be assigned
        '''

        # check if empty, return
        if (self._cur_size == 0) or (index > self._cur_size) or (index < 0):
            # print('array empty')
            # print('index > cur_size, no value exists at this index')
            # print('index can't be negative)
            return
        self._array[index] = value

    def append(self, value):
        '''
        appends the given value at the end of the dynamic array

        Keyword arguments:
        value -- value to be appended at the end of the dynamic array
        '''

        # check if appending will exceed size
        # if not, insert at end
        # udpate current size
        is_full = self.__check_if_full()
        if is_full:
            # it will double the size
            self.__increase_size()
        # insert at end
        self._array[self._cur_size] = value
        # udpate size
        self._cur_size += 1

    def print_all(self):
        '''
        print the content of the dynamic array
        '''
        print('---dyn array contents---')
        for i in range(self._cur_size):
            print(self._array[i], end=', ')
        print('---')

    def clear(self):
        '''
        clear given array and sets size to zero.
        '''
        self._array = [None]*self._max_size
        self._cur_size = 0

    def __get_max_size(self):
        '''
        returns max size of the current dynamic array
        '''
        return self._max_size

    def __check_if_full(self):
        '''
        to check if the dynamic array is full
        '''
        # check if current size == max size of array
        return self._cur_size == self._max_size

    def __check_if_empty(self):
        '''
        to check if the dynamic array is empty
        '''
        # check if current size == 0
        return self._cur_size == 0

    def __increase_size(self):
        '''
        double the size of array when at capacity
        '''
        # lets create a new array with double the max_size of current array
        # copy over the elements

        # double max size
        self._max_size = self._max_size*2
        # create new array
        self._new_array = [None]*self._max_size
        # copy over the elements form old to new
        for i in range(self._cur_size):
            self._new_array[i] = self._array[i]
        self._array = self._new_array
        del self._new_array


if __name__ == "__main__":
    array_obj = DynArray()
    # for i in range(100):
    #     array_obj.append(i*10)
    #     if i % 20 == 0:
    #         print(i)
    #         time.sleep(1)
    array_obj.print_all()
    array_obj.append(10)
    array_obj.append(20)
    array_obj.append(30)
    array_obj.append(40)
    # array_obj.append(50)
    array_obj.print_all()
    array_obj.insert(1, 11)
    array_obj.insert(2, 12)
    array_obj.insert(3, 13)
    array_obj.insert(4, 18)
    array_obj.print_all()
    array_obj.remove(10)
    array_obj.insert(7, 41)
    array_obj.print_all()
    # print(array_obj.get_val_at_index(7))
    # print(array_obj.set_val_at_index(5, -1))
    array_obj.print_all()
    array_obj.clear()
    array_obj.print_all()
