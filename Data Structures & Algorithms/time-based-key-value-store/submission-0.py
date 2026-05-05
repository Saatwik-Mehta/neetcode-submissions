class TimeMap:

    def __init__(self):
        self.hash_ = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash_:
            self.hash_[key].append((value, timestamp))
        else:
            self.hash_[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hash_:
            for each in reversed(list(self.hash_[key])):
                if each[1] <= timestamp:
                    return each[0]
        return ""
                   
