class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        
        for i, n in enumerate(nums):
            need = target - n
            if need in prevMap:
                return [prevMap[need], i]
            prevMap[n] = i
        
        return []