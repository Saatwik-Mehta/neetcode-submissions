class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        l = 0
        r = l+1
        while r < n:
            if prices[l] > prices[r]:
                # if the selling price is less than the buying price, then l will be shifted to the selling point
                # like we have purchased the stocks at that day itself.

                l = r
            else:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            r+=1
        return max_profit


