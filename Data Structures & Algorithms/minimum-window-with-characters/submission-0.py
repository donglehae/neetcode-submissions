class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        l = 0
        need, have = len(countT), 0
        res, resLen = [-1, -1], float("inf")
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if window[s[r]] == countT.get(s[r], 0):
                have += 1

            while need == have:
                if resLen > (r - l + 1):
                    res, resLen = [l, r], (r - l + 1)

                if window[s[l]] == countT.get(s[l], 0):
                    have -= 1

                window[s[l]] -= 1
                l += 1
        l, r = res
        return s[l:r + 1]