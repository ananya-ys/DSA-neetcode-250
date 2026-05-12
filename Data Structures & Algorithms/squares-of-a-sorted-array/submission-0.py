class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left = 0
        right = n - 1
        pos = n - 1
        while left <= right:
            leftSquare = nums[left] ** 2
            rightSquare = nums[right] ** 2
            if leftSquare > rightSquare:
                res[pos] = leftSquare
                left += 1
            else:
                res[pos] = rightSquare
                right -= 1
            pos -= 1
        return res