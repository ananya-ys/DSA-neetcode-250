from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()          # stores indices
        res = []
        l = 0

        for r in range(len(nums)):
            # Remove smaller elements from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # Add current index
            q.append(r)
            # Remove indices outside the window
            if q[0] < l:
                q.popleft()
            # Window has reached size k
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        return res