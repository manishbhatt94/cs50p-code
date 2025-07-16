class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if type(capacity) is not int or capacity < 0:
            raise ValueError("capacity must be a non-negative int")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0 or size > self.capacity:
            raise ValueError("size value invalid")
        self._size = size


def main():
    jar = Jar(capacity=4)
    print(f"jar.capacity = {jar.capacity}")
    jar.deposit(3)
    print(f"jar.size = {jar.size}")
    jar.withdraw(2)
    print(f"jar.size = {jar.size}")


if __name__ == "__main__":
    main()
