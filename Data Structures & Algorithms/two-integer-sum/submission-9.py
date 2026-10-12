class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for index in range(len(nums)) :
            diff = target - nums[index]
            if diff in seen :
                return [seen[diff],index]
            seen[nums[index]] = index
        return [-1,-1]