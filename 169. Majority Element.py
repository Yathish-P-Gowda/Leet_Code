class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        new_dict={}
        for i in nums:
            if i  in new_dict:
                new_dict[i]+=1
            else:
                new_dict[i]=1
        new_list=sorted(new_dict.items(),key= lambda x:x[1])
        last_key,last_value=new_list[-1]
        return last_key
        