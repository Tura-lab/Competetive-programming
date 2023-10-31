class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        xor = 0
        ans = []
        
        for num in pref:
            ans.append(xor ^ num)
            xor = num
            
        return ans