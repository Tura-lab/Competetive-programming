class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        ans = []
        
        for log in logs:
            if log[-1].isalpha():
                ans.append(log)
        
        ans.sort(key = lambda log: (' '.join(log.split()[1:]), log.split()[0]))
        
        for log in logs:
            if not log[-1].isalpha():
                ans.append(log)
                
        return ans