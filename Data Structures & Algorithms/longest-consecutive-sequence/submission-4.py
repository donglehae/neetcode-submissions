class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        prep = set(nums)
        res = 0

        for n in prep:
            if n - 1 not in prep:
                strike = 0
                while (n + strike) in prep:
                    strike += 1
                res = max(res, strike)
        
        return res