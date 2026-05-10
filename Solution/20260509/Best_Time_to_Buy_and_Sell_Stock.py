# Version 1 Brute Force
## Enumerate all profit and find max profit
## Time complexity: O(n^2), where n is the length of input list.
## Space complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        for i in range(len(prices)):
            j = len(prices) - 1
            while(i < j):
                if prices[j] - prices[i] > mp:
                    mp = prices[j] - prices[i]
                j-=1
        return mp

prices = [10,8,7,5,2]
s = Solution()
result = s.maxProfit(prices)
print(result)

# Version 2 Two pointers
## The goal is to maximize profit by buying at the lowest price and selling at a higher price that occurs after the buy day.
## We use two pointers:
## l: tracks the lowest price seen so far (best buying point)
## r: scans through the array as the selling day
## If prices[r] > prices[l], we calculate the potential profit and update the maximum result.
## Otherwise, we update l to r because we found a lower buying price.
## This ensures that l always points to the minimum price before r, allowing us to efficiently compute the best possible profit in one pass.
## Time complexity: O(n), where n is the length of input list.
## Space complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return res

# Version 3 Dynamic Programming
## As we scan through the prices, we keep track of two things:
### 1. The lowest price so far
### 2. The best profit so far
## At each price, we imagine selling on that day.
### The profit would be: current price - lowest price seen so far
## We then update
### the maximum profit.
### and the lowest price if we find a cheaper one.
## Time complexity: O(n), where n is the length of input list.
## Space complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        maxP = 0
        for sell in prices:
            maxP = max(maxP, sell - minbuy)
            minbuy = min(minbuy, sell)
        return maxP