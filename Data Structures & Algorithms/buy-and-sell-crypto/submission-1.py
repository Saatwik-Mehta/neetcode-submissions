class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        l = 0
        r = l+1
        while r < n:
            if prices[l] > prices[r]:
                l = r

            else:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            r+=1
        return max_profit


