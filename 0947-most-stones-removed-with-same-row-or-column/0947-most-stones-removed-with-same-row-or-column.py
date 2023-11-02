class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = [i for i in range(len(stones))]
        size = [1 for _ in range(len(stones))]
        
        def find(x):
            path = []
            while x != parent[x]:
                path.append(x)
                x = parent[x]
                
            for p in path:
                parent[p] = x
            
            return x
        
        
        def union(a, b):
            a, b = find(a), find(b)
            
            if a == b:
                return 
            
            if size[b] > size[a]:
                a, b = b, a
                
            parent[b] = a
            size[a] += size[b]
            
        
        for i, a in enumerate(stones):
            for j, b in enumerate(stones):
                if i == j:
                    continue
                    
                if i != j and (a[0] == b[0] or a[1] == b[1]):
                    union(i, j)
                    
        ans = 0
        for i, num in enumerate(parent):
            if num == i:
                ans += 1
                
        return len(stones) - ans