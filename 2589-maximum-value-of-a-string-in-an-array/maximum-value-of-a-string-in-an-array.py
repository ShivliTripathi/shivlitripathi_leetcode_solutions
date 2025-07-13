class Solution:
    def maximumValue(self, strs: List[str]) -> int:

        l=[]
        
        for st in strs:

            if st.isalpha():
                
                l.append(len(st))

            elif st.isdigit():
                
                if st.startswith=='0':
                    while '0' in st:
                        st=st.replace('0','')
                
                if st=='':
                    l.append(0)
                else:
                    l.append(int(st))

            else:
                
                digit,letter = [],[]
                for c in st:
                    if c.isdigit():
                        digit.append(c)
                    elif c.isalpha():
                        letter.append(c)
                
                if digit and letter:
                    l.append(len(digit)+len(letter))

        return max(l)