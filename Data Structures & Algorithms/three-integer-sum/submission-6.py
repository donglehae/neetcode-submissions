class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        groups = set()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                if nums[left] + nums[right] < -nums[i]:
                    left += 1
                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
                else:
                    groups.add((nums[i], nums[left], nums[right]))
                    left, right = left + 1, right - 1
            
        return list(groups)