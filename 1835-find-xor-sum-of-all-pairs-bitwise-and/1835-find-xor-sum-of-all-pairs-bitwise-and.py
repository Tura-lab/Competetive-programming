class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xor = 0
        for num in arr2:
            xor = xor ^ num
            
        xor2 = 0
        for num in arr1:
            xor2 = xor2 ^ (num & xor) 
        
        return xor2