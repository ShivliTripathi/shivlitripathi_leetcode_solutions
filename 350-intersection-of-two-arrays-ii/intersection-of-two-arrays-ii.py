class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        from collections import Counter
        if len(nums1) <= len(nums2):
            x = Counter(nums1)
            l = nums2
        else:
            x = Counter(nums2)
            l = nums1

        a=[]
        for y in l:
            if x[y] > 0:
                a.append(y)
                x[y] -=1
            
        return a