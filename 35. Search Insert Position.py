class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        while target not in nums:
            nums.append(target)
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                return i
                        