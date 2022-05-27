class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = defaultdict(list)
        visited = set()
        
        for account in accounts:
            if len(account) == 2:
                emails[account[1]] = []
            for i in range(1,len(account)-1):
                emails[account[i]].append(account[i+1])
                emails[account[i+1]].append(account[i])
                
        # print(dict(emails))
        def dfs(em):
            for e in em:
                if e not in visited:
                    visited.add(e)
                    new.append(e)
                    dfs(emails[e])        
        
        ans = []
        i=0
        for account in accounts:
            
            new = collections.deque()
            for i in range(1, len(account)):
                if account[i] not in visited:
                    visited.add(account[i])
                    new.append(account[i])
                    dfs(emails[account[i]])
            if new:
                new = list(new)
                new.sort()
                ans.append([account[0]] + new)
                
        return ans