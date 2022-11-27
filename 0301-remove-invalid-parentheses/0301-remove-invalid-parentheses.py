class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = [set() for _ in range(26)]
        
        def dfs(i, count, path):
            if i == len(s):
                if count == 0:
                    ans[len(path)].add(''.join(path))
                return
            
            if s[i].isalpha():
                path.append(s[i])
                dfs(i+1, count, path)
                path.pop()
                return 
            
            old_count = count
            path.append(s[i])
            
            count += 1 if s[i] == '(' else -1
            
            if count >= 0:
                # take
                dfs(i+1, count, path)
                
            # dont
            path.pop()
            dfs(i+1, old_count, path)
            
        dfs(0, 0, [])
        
        for i in range(len(ans)-1, -1, -1):
            if ans[i]:
                return ans[i]
        
        return [""]