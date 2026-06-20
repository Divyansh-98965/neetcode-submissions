class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_to_buy = prices[0]
        curr_profit = 0
        for i in prices:
            #compare curr_best_buy_price to i
            if best_to_buy > i:
                best_to_buy = i
            
            #calculate current profit and compare it with max_profit 
            curr_profit = i - best_to_buy 

            max_profit = max(curr_profit, max_profit)

        return max_profit