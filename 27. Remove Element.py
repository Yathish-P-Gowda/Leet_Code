class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_list=[]
        for i in range(len(nums)):
            if val!=nums[i]:
                new_list.append(nums[i])
        for i in range(len(new_list)):
            nums[i]=new_list[i]
        return len(new_list)
                