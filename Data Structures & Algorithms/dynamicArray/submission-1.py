class DynamicArray:
    
    def __init__(self, capacity: int):
        self.current_capacity = capacity
        self.arr = [0] * self.current_capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.current_capacity:
            # arr is full
            self.resize()
        self.length += 1
        self.arr[self.length-1] = n

    def popback(self) -> int:
        pop_item = self.arr[self.length-1]
        self.arr[self.length-1] = 0
        self.length -= 1
        return pop_item

    def resize(self) -> None:
        self.current_capacity *= 2
        temp_arr = [0] * self.current_capacity
        for i in range(self.length):
            temp_arr[i] = self.arr[i]
        del self.arr
        self.arr = temp_arr
        del temp_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.current_capacity
