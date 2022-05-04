class Solution:
    '''
    5  3  3  3  5  6  2
       |     |
    '''
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        ans = set()
        
        after = [0]*len(security)
        before = [0]*len(security)
        
        for i in range(1, len(security)-1):
            if security[i] <= security[i-1]:
                before[i] = before[i-1]+1
            else:
                before[i] = 0
            
        for i in range(len(security)-2, -1, -1):
            if security[i+1] >= security[i]:
                after[i] = after[i+1]+1
            else:
                after[i] = 0
                
        ans = []
        for i in range(len(security)):
            if i>=time and len(security)-i-1 >= time and before[i]>=time and after[i] >= time:
                ans.append(i)
            
        # print(before)
        # print(after)
        return ans
        