from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = Counter(nums)      
        return [key for (key, freq) in ct.most_common(k)]