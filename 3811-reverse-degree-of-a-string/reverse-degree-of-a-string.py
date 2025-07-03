class Solution:
    def reverseDegree(self, s: str) -> int:
        alpha_dict = {ch: val for ch, val in zip(string.ascii_lowercase, range(26, 0, -1))}
        
        rev_degree=0
        prod=1
        
        for i in range(len(s)):
            
            st = alpha_dict[s[i]]
            prod = (i+1)*st
            rev_degree += prod
            
        return rev_degree