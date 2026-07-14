class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')
        maxp = 0

        for i in prices :
            if i < minp :
                minp = i
            
            prof = i - minp

            if prof > maxp :
                maxp = prof
        return maxp

