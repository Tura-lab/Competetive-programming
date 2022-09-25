class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        

        parent = [i for i in range(len(edges)+1)]
        size = [1]*(len(edges)+1)
        
        def find(a):
            while a != parent[a]:
                a = parent[a]
            return a
        
        def union(a,b):
            a, b = find(a), find(b)
            if a == b:
                return
            
            if size[b] > size[a]:
                a,b = b,a
            
            parent[b] = a
            size[a] += size[b]
            
        got = [False]*len(vals)
        found = defaultdict(list)
        
        vals = sorted([(i, vals[i]) for i in range(len(vals))], key=lambda x: x[1])
        for i,val in vals:
            found[val].append(i)
        
        
        tot = len(vals)
        for num, vals in found.items():
            for node in vals:
                got[node] = True
                for v in graph[node]:
                    if got[v]:
                        union(v, node)
            
            counts = Counter()
            for node in vals:
                counts[find(node)] += 1
            for _, count in counts.items():
                tot += (count)*(count-1)//2
        
        return tot