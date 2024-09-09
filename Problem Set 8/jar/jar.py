class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError
        else:
            self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if not (isinstance(value, int) and value >= 0):
            raise ValueError
        self._capacity = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not (isinstance(value, int) and value >= 0):
            raise ValueError
        self._size = value
