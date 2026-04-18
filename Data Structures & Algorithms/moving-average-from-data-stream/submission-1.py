class MovingAverage:

    def __init__(self, size: int):
        self.capacity = size
        self.size = 0
        self.start = -1
        self.end = -1
        self.cir_arr = [None for _ in range(self.capacity)]

    def next(self, val: int) -> float:
        total = 0
        if self.start == self.end == -1:
            self.start = 0
        
        self.end = (self.start + self.size) % self.capacity
        if self.cir_arr[self.end] == None:
            self.size += 1
        else:
            self.start = (self.start + 1) % self.capacity
        self.cir_arr[self.end] = val
        for i in range(self.size):
            total += self.cir_arr[i]
        return (total/self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
