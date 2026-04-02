class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit_max=0
        min=0
        for i,val in enumerate(prices):
            if i==0:
                min=val
                profit_max=min-val
            else:
                if min>val:
                    min=val
                if profit_max<val-min:
                        profit_max=val-min
        return profit_max