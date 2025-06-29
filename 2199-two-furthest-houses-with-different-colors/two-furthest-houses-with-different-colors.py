class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        m_col=0
        for i in range(len(colors)):
            for j in range(i+1,len(colors)):
                if colors[i]!=colors[j]:
                    x = abs(i-j)
                    m_col=max(m_col,x)

        return m_col