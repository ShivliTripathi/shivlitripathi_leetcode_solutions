class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        a=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    a.append(nums1[i])
                else:
                    b=str(nums1[i])+str(nums2[j])
                    a.append(int(b))
                    #reversing the combination
                    c=str(nums2[j])+str(nums1[i])
                    a.append(int(c))

        return min(a)