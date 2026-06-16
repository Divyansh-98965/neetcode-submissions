class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            # Update the lowest price seen so far
            if price < min_price:
                min_price = price
                
            # Calculate potential profit if we sold today
            potential_profit = price - min_price
            
            # Update max_profit if this deal is better
            if potential_profit > max_profit:
                max_profit = potential_profit
                
        return max_profit