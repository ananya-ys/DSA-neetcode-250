from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k) :
            ho = 0
            for p in piles :
                ho += ceil(p / k)
            return ho <= h
        
        l = 1 
        r = max(piles)

        while l < r :
            k = (l+r) // 2
            if k_works(k) :
                r = k
            else :
                l = k+1
        return r