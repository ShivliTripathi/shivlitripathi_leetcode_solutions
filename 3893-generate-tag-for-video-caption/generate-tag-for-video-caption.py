class Solution:
    def generateTag(self, caption: str) -> str:
        
        cap= caption.title().replace(' ','')
        if cap == "":
            cap="#"
            l=cap
        else:
            cap='#'+cap[0].lower()+cap[1:]
            l=''.join(cap.split(' '))

        if len(l)<=100:
            return l
        else:
            while len(l)>100:
                l=l[:-1]
            return l
            