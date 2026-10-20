class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, b - a)for a, b in zip(prices, prices[1:]))

    def maxProfit2(prices: list[int]) -> int:
        profit = 0 
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit