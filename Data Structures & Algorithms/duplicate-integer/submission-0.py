class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in range(1, len(nums)):
            if nums[x-1] in nums[x:]:
                return True
        return False