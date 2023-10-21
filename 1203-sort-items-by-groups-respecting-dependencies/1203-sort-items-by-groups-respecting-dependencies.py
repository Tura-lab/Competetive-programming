class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i, g in enumerate(group):
            if g == -1:
                group[i] = m
                m += 1

        group_indeg = [0] * m
        item_indeg = [0] * n
        group_graph = [[] for _ in range(m)]
        item_graph = [[] for _ in range(n)]
        
        for i, items in enumerate(beforeItems):
            for node in items:
                if group[i] != group[node]:
                    group_graph[group[node]].append(group[i])
                    group_indeg[group[i]] += 1
                
                item_graph[node].append(i)
                item_indeg[i] += 1
                
        def top_sort(graph, indeg):
            q = deque()
            ans = []
            for node, ind in enumerate(indeg):
                if ind == 0:
                    q.append(node)
            
            while q:
                node = q.popleft()
                ans.append(node)
                
                for v in graph[node]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)
            
            if len(ans) < len(indeg):
                return []
            
            return ans
                
        item_order, group_order = top_sort(item_graph, item_indeg), top_sort(group_graph, group_indeg)
        
        
        if not item_order or not group_order:
            return []
        
        ordering = [[] for _ in range(m)]
        for node in item_order:
            ordering[group[node]].append(node)
            
        final = []
        for g in group_order:
            for node in ordering[g]:
                final.append(node)
                
        return final