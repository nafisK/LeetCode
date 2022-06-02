class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            l, r = 0, 1
            max_profit = 0
            
            while (r < len(prices)):
                
                # nornal iteration | testing/finding the new max_profit
                if prices[l] < prices[r]:
                    temp_max = prices[r] - prices[l]
                    max_profit = max(temp_max, max_profit)
                    
                # in case there is a lower l
                else:
                    l = r
                
                r += 1
                
            return max_profit