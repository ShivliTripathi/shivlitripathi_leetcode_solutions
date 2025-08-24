class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        import string
        dic = {'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j':'9'}
        fw = int(''.join([dic[x] for x in firstWord]))
        sw = int(''.join([dic[y] for y in secondWord]))
        tw = int(''.join([dic[z] for z in targetWord]))
        return fw+sw == tw