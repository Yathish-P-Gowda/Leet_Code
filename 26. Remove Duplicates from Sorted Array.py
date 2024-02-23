class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums.sort()
        # new_list=[]
        # length=len(nums)
        # for i in range(length):
        #     dupli=False
        #     for j in range(i+1,length):
        #         if nums[i]==nums[j]:
        #             dupli=True
        #     if dupli==False:
        #         new_list.append(nums[i])
        #     for i in range(len(new_list)):
        #         nums[i]=new_list[i]        
        # return len(new_list)
        nums[:]=sorted(set(nums))
        return len(nums)
        