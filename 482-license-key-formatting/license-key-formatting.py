class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        a=''
        exp_string=[]
        for x in s[::-1]:
            if x!='-':
                a+=x
                if len(a)<k:
                    continue
                else:
                    exp_string.append(a)
                    a=''
        if a!= '':
            exp_string.append(a) 
            
        for y in range(len(exp_string)):
            exp_string[y]=exp_string[y][::-1].upper()
            
        return '-'.join(exp_string[::-1])