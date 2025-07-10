class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
        for x in aliceSizes:
            y = x + (sum(bobSizes) - sum(aliceSizes))/2
            if y in bobSizes:
                return [x,y]