class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        m_min = min(nums)
        m_max = max(nums)
        
        cnt=0
        
        for i in nums:
            if m_min < i < m_max:
                cnt+=1
        return cnt