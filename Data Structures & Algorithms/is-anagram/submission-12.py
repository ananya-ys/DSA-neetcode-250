
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sch = {}
        for c in s:
            sch[c] = sch.get(c, 0) + 1

        for c in t:
            if c not in sch:
                return False
            sch[c] -= 1

        for count in sch.values():
            if count != 0:
                return False

        return True