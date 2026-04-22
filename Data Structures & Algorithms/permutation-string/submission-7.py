class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s2)
        s1 = sorted(s1)
        for i in range(size):
            for j in range(i, size, len(s1)):
                sub = s2[j:j+len(s1)]
                sub = sorted(sub)
                if sub == s1:
                    return True
        return False

