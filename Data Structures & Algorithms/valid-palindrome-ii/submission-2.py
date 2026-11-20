class Solution:
    def validPalindrome(self, s: str) -> bool: 
        def isPalindrom(s: str, start: int, end: int) -> bool:
            while start < end: 
                if s[start] != s[end]:
                    return False
                
                start += 1
                end -=1
            return True

        if len(s) <= 1:
            return True

        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            
            else: 
                #skip the left or right character. 
                return (isPalindrom(s, start + 1, end)) or (isPalindrom(s, start, end-1))

        return True 