class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        m_min = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        s = nums[i]+nums[j]+nums[k]
                        m_min.append(s)

        if m_min:
            return min(m_min)
        return -1
        