class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        prep = set(nums)
        best = 0
        for n in prep:
            if n - 1 not in prep:
                length = 1
                while n + length in prep:
                    length += 1
                best = max(best, length)
        return best