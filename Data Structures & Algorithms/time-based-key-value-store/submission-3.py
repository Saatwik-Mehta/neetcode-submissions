class TimeMap:

    def __init__(self):
        self.hash_ = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash_:
            self.hash_[key].append((value, timestamp))
        else:
            self.hash_[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        v = ""
        if key in self.hash_:
            l = 0
            r = len(self.hash_[key]) - 1
            v = ""
            while l <= r:
                mid = (l+r)//2
                if self.hash_[key][mid][1] <= timestamp:
                    v = self.hash_[key][mid][0]
                    l = mid + 1
                else:
                    r = mid - 1

            # for each in reversed(self.hash_[key]):
            #     if each[1] <= timestamp:
            #         return each[0]
        return v
                   
