class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels=['a','e','i','o','u']
        vow,con = {},{}
        x=Counter(s)

        for key,val in x.items():
            if key in vowels:
                vow[key]=val
            else:
                con[key]=val

        if vow:
            maxvow_key = max(vow, key=vow.get)
            maxvow_val = vow[maxvow_key]
        else:
            maxvow_val = 0
            
        if con:
            maxcon_key = max(con, key=con.get)
            maxcon_val = con[maxcon_key]
        else:
            maxcon_val = 0

        return maxvow_val+maxcon_val