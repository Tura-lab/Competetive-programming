class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        problems = []         
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                problems.append(i)

        if len(problems) & 1:
            return -1
        
        @cache
        def dfs(i, flips):
            if i == len(problems) - 1:
                return 0 if flips == 0 else x/2
            if i == len(problems):
                return 0 if flips == 0 else float('inf')
            
            one = x / 2 + dfs(i + 1, 1 - flips)
            two = problems[i + 1] - problems[i] + dfs(i + 2, flips)

            return min(one, two)
                
        ans = dfs(0, 0)
        return int(ans) if ans != float('inf') else -1