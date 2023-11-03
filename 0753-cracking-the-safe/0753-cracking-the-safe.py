class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        
        def search(size):
            found = []
            temp = []
            def dfs():
                nonlocal temp
                if len(temp) == size:
                    found.append("".join(temp))
                    return
                for i in range(k):
                    temp.append(str(i))
                    dfs()
                    temp.pop()
        
            dfs()
            return found

        graph = defaultdict(list)
        
        # generate all n sized passwords
        perms = set(search(n))
        
        ans = []
        def dfs(node):
            for i in range(k):
                new = node + str(i)
                if new in perms:
                    perms.remove(new)
                    dfs(new[1:])
                    ans.append(str(i))
                
        cur = "0" * (n - 1)
        dfs(cur)
        return "".join(ans) + cur
    
    
    