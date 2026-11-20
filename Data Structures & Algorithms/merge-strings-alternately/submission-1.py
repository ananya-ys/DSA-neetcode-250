class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = 0
        w2 = 0
        res = ""

        while w1 < len(word1) and w2 < len(word2):
            res += word1[w1]
            res += word2[w2]
            w1 += 1
            w2 += 1

        if len(word1) > len(word2):
            for s in word1[w1:]:
                res += s
        elif len(word2) > len(word1):
            for s in word2[w2:]:
                res += s

        return res