class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = []
        for num in nums:
            if num not in list:
                list.append(num)
            elif num in list:
                return True
        return False
