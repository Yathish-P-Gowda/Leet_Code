class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l1=[]
        l=[l1.extend([i,j]) for i in range(len(nums)) for j in range(i+1,len(nums)) if nums[i] +nums[j]==target]
        return l1