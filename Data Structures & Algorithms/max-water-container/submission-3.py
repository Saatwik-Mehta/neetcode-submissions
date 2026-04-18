class Solution:
    def calculateArea(self, heights, h1, h2):
        bar1 = min(heights[h1], heights[h2])
        return bar1 * (h2-h1)
    def maxArea(self, heights) -> int:
        # combo = []
        # n  = len(heights)
        # for ibar in range(n):
        #     for jbar in range(ibar+1, n):
        #         height = min(heights[ibar], heights[jbar])
        #         length = jbar - ibar
        #         combo.append(length * height)
        # return max(combo)      
        max_area = float("-inf") 
        l = 0
        r = len(heights)-1
        while l < r:
            area = self.calculateArea(heights, l, r)
            max_area = max(max_area, area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_area