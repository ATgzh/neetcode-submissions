class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num = prices[0]
        current_price = 0
        for x in range(len(prices)):
            if prices[x] < min_num:
                min_num = prices[x]
            elif prices[x] - min_num > current_price:
                current_price = prices[x] - min_num

        return current_price