class Solution:
    def maxArea(self, heights) -> int:
        combo = []
        n  = len(heights)
        for ibar in range(n):
            for jbar in range(ibar+1, n):
                height = min(heights[ibar], heights[jbar])
                length = jbar - ibar
                combo.append(length * height)
        return max(combo)       