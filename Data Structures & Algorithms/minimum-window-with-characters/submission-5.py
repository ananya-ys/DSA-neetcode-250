class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" :
            return ""
        
        countt = {}
        window = {}

        for c in t :
            countt[c] = countt.get(c,0) + 1
        
        have = 0
        need = len(countt)

        res = [-1,-1]
        reslen = float("infinity")

        left = 0
        for right in range(len(s)) :
            c = s[right]
            window[c] = window.get(c,0) + 1

            if c in countt and window[c] == countt[c] :
                have += 1

            while have == need :
                if (right - left + 1) < reslen :
                    res = [left , right]
                    reslen = right - left + 1
                
                window[s[left]] -= 1

                if s[left] in countt and window[s[left]] < countt[s[left]] :
                    have -= 1
                
                left += 1 

        left , right = res
        return s[left : right+1] if reslen != float('infinity') else ""