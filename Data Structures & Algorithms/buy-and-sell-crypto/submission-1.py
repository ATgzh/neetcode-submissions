class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxnumber = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[left] < prices[right]:
                maxnumber = max(maxnumber, prices[right] - prices[left])
            else:
                left = right

            right += 1
        return maxnumber
