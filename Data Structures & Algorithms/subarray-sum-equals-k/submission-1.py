class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        hashmap = {0: 1}

        for num in nums:
            prefix_sum += num
            diff = prefix_sum - k

            if diff in hashmap:
                count += hashmap[diff]

            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
        return count