class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        from collections import Counter

        x=Counter(s)
        print(x)
        cnt=0
        sorted_x = sorted(x.items(), key=lambda item: item[1])

        i=0
        while len(x) > k and i < len(sorted_x):
            char,freq = sorted_x[i]
            cnt+=freq
            del x[char]
            i+=1    
        return cnt