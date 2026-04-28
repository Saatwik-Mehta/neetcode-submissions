import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)

        while l <= r:
            k = (l + r)//2
            if k == 0:
                l = k + 1
                continue
            total = 0
            for pile in piles:
                total += math.ceil(pile/(k if k > 0 else 1))
                if total > h:
                    break
            if total <= h:
                r = k - 1
            else:
                l = k + 1
        return l