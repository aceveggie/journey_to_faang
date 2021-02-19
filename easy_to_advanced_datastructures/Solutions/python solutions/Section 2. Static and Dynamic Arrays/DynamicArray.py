import ctypes
class DynamicArray(object):
   #Initialize it
   def __init__(self):
      #We'll have three attributes
      self.n = 0 # by default
      self.capacity = 1 # by default
      self.A = self.make_array(self.capacity) # make_array will be defined later
   #Length method
   def __len__(self):
      #It will return number of elements in the array
      return self.n
   def __getitem__(self, k):
      #it will return the elements at the index k
      if not 0 <=k <self.n:
         return IndexError('k is out of bounds')
      return self.A[k]
   
   def _resize(self, new_cap): #new_cap is for new capacity
   #declare array B
      B = self.make_array(new_cap)
      for k in range(self.n):
         B[k] = self.A[k] # referencing the elements from array A to B
         #ones refered then
      self.A = B # A is now the array B
      self.capacity = new_cap # resets the capacity
      #making the make-array method using ctypes

   def append(self, element):
   #checking the capacity
      if self.n == self.capacity:
         #double the capacity for the new array i.e
         self._resize(2*self.capacity) # _resize is the method that is defined later
      # set the n indexes of array A to elements
      self.A[self.n] = element
      self.n += 1
   
   def make_array(self,new_cap):
      return (new_cap * ctypes.py_object)()

arr = DynamicArray()

# print(len(arr))

arr.append(1)

# print(len(arr))

arr.append(3)

# print(len(arr))

arr.append(3)
arr.append(3)
arr.append(3)
arr.append(3)
arr.append(5)

for i in range(len(arr)):
   print(arr[i])