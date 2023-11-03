class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
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
            if outdeg[cur_node] > 0:
                nxt_node = graph[cur_node].pop()
                stack.append(nxt_node)
                outdeg[cur_node] -= 1
                cur_node = nxt_node
            else:
                ans.append(cur_node)
                stack.pop()
                
        ans.reverse()
        # print(ans)
        return [[ans[i - 1], ans[i]] for i in range(1, len(ans))]