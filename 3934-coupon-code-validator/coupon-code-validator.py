class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        a=[]
        for x,y,z in zip(code,businessLine,isActive):
            if bool(re.fullmatch(r'\w+', x)) == True and y in ["electronics", "grocery", "pharmacy", "restaurant"] and z == True:
                a.append((y,x))

        return [c for _,c in sorted(a)]