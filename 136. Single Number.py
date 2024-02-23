class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new_dict={}
        for i in nums:
            if i  in new_dict:
                new_dict[i]+=1
            else:
                new_dict[i]=1
        for key,value in new_dict.items():
            if value==1:
                return key