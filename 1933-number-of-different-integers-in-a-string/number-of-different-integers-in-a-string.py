class Solution:
    def numDifferentIntegers(self, word: str) -> int:

        a=''
        b=set()
        for char in word:
            if char.isdigit():
                a+=char
            else:
                if a!="":b.add(int(a))
                a=""
                continue
                
        if a!="":b.add(int(a)) 
        return len(b)