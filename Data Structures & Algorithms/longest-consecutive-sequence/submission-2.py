class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        prep = sorted(set(nums))
        best = 0
        count = 0
        for i in range(len(prep) - 1):
            if prep[i] + 1 == prep[i + 1]:
                count += 1
                best = max(best, count)
            else:
                count = 0
        else:
            best += 1
        return min(best, len(prep))