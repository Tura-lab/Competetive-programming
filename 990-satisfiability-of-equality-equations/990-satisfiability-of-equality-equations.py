class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        size = {}
        new = []
        for e in equations:
            if e[1:-1] == '==':
                new.append(e)
        for e in equations:
            if e[1:-1] == '!=':
                new.append(e)
        equations = new
        
        def find(a):
            if a not in parent:return a
            while a != parent[a]:
                a = parent[a]
                
            return a
        def union(a,b):
            if a not in parent:
                parent[a] = a
                size[a] = 1
            if b not in parent:
                parent[b] = b
                size[b] = 1
            
            a,b = find(a), find(b)
            if a==b:
                return
            if size[b] > size[a]:
                a,b = b,a
            
            parent[b] = a
            size[a] += size[b]
            
        for e in equations:
            a, b = e[0], e[-1]
            
            if e[1:-1] == '==':
                union(a,b)
            else:
                if find(a) == find(b):
                    return False
        return True