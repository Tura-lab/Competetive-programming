class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        
        ans = 0
        for num, count in counter.items():
            if count < 2:
                return -1
            ans += ceil(count/3)
            
        return ans