class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)):
            if i>=m:
                nums1[i]=nums2[i-m]
            else:
                continue
        nums1.sort()
        return nums1
        