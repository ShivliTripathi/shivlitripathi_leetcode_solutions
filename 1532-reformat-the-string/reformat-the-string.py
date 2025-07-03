class Solution:
    def reformat(self, s: str) -> str:
        digit,char = [],[]

        for i in s:
            if i.isdigit():
                digit.append(i)
            else:
                char.append(i)

        final=''

        if len(s)==1:
            return s
        if not digit or not char:
            return ""
        else:
            if len(digit) - len(char) == 1:
                for x,y in zip(digit,char):
                    final+=x
                    final+=y 
                final+=digit[-1]
                    
            elif len(char) - len(digit) == 1:
                for x,y in zip(char,digit):
                    final+=x
                    final+=y
                final+=char[-1]

            elif len(digit) == len(char):
                for x,y in zip(digit,char):
                    final+=x
                    final+=y 
            
            else:
                return ""

        return final