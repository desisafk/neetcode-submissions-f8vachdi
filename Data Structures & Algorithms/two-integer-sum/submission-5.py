class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            key = target - num
            if key in nums[i+1:]:
                j = nums.index(key, i+1)
                return [i, j]