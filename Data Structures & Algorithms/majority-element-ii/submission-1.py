class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashh = {}
        res = []
        for i in nums :
            hashh[i] = hashh.get(i , 0) + 1
        for j in hashh :
            if hashh[j] > len(nums)//3:
                res.append(j)
        return res
            