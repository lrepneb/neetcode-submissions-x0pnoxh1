class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1
        while r < len(prices):
            # compare values at l and r
            price_r = prices[r]
            price_l = prices[l]
            if prices[r] >= prices[l]:
                profit = max(profit, price_r - price_l)
            else:
                l=r
            r+=1
        return profit

