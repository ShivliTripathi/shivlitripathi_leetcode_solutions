class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        x=Counter(stones)
        cnt=0
        for i in jewels:
            if i in x.keys():
                cnt+=x[i]

        return cnt