class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        found = []
        for num in nums:
            if not found:
                found.append(num)
                continue
            if found[-1]<num:
                found.append(num)
                if len(found)>=3:
                    return True
                continue
                
            
            for i in range(len(found)):
                if found[i] >= num :
                    found[i] = num
                    break
            if len(found)>=3:
                return True
        
        return False