from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for s in strs:
            count = [0] * 26  # for a-z

            for ch in s:
                count[ord(ch) - ord('a')] += 1

            key = tuple(count)  # lists can't be dict keys
            mp[key].append(s)

        return list(mp.values())