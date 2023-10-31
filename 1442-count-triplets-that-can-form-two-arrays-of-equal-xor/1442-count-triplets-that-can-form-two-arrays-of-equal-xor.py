class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        p_xor = [0]
        for num in arr:
            p_xor.append(p_xor[-1] ^ num)
            
        count = 0
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    if p_xor[j] ^ p_xor[i] == p_xor[k + 1] ^ p_xor[j]:
                        count += 1
                        
        return count