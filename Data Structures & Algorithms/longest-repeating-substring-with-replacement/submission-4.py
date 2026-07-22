class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxf = 0
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxf = max(maxf, count[s[right]])
            window = right - left + 1
            if window - maxf > k:
                count[s[left]] = count.get(s[left], 0) - 1
                left += 1
            res = max(res, right - left + 1)
                
        return res

        

