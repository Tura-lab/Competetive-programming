class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        nums = list(map(int, list(str(n))))
        counts = Counter(nums)
        
        path = []
        self.ans = False
        
        
        def check(num):
            i = 1
            count = 0
            found = False
            while count < 33:
                if i<<count & num:
                    if found:
                        return False
                    found = True
                    
                count += 1
            return True
                
        
        def dfs():
            if len(path) == len(nums):
                if check(int(''.join(str(i) for i in path))):
                    self.ans = True
                    return
                
            if self.ans:
                return
            
            for num, count in counts.items():
                if num == 0 and not path:continue
                if count:
                    counts[num] -= 1
                    path.append(num)
                    dfs()
                    path.pop()
                    counts[num] += 1
        
        dfs()
        return self.ans