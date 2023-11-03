class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # count indeg and outdeg to check if graph is eulerian
        graph = defaultdict(list)
        outdeg = defaultdict(int)
        indeg = defaultdict(int)
        
        for a, b in pairs:
            indeg[b] += 1
            outdeg[a] += 1
            graph[a].append(b)

        ans = []
        start = pairs[0][0]
        for a in outdeg:
            if outdeg[a] == 1 + indeg[a]:
                start = a
                break

        stack = []
        cur_node = start
        stack.append(start)
        while stack:
            cur_node = stack[-1]
            if graph[cur_node]:
                nxt_node = graph[cur_node].pop()
                stack.append(nxt_node)
                cur_node = nxt_node
            else:
                ans.append(cur_node)
                stack.pop()
                
        ans.reverse()
        return [[ans[i - 1], ans[i]] for i in range(1, len(ans))]