import ctypes

class DynamicArray
    def __init__(self):
        self.capacity = 1
        self.n = 0
        self.A = self.make_array(self.capacity)

    def __len(self):
        return self.n

    def __append(self, element):
        if self.length == self.capacity
          self._resize(self.length * 2)

        self.A[self.n] = element 
        self.n += 1

    def __resize(self, new_cap):
        B = self.make_array(new_cap)

        for k in  range(self.n)
            B[k] = self.A[k]
            self.A = B
            self.capacity = new_cap

    def __make_array(self, new_cap)
        return (self.make_array * ctypes.py_object)()
