class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        for i in accounts:
            x=0
            for j in i:
                x+=j
            m=max(m,x)
        
        return m