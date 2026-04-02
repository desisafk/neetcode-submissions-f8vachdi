class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            elif num in s:
                return True
        return False
