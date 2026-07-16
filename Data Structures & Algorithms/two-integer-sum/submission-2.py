class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        
        for i, n in enumerate(nums):
            need = target - n
            if need in count:
                return [count[need], i]
            count[n] = i