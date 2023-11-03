class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for a, b in tickets:
            graph[a].append(b)
        
        for item in graph:
            graph[item].sort(reverse = True)
        
        ans = []
        stack = []
        stack.append("JFK")
        while stack:
            cur_node = stack[-1]
            if graph[cur_node]:
                nxt_node = graph[cur_node].pop()
                stack.append(nxt_node)
            else:
                ans.append(cur_node)
                stack.pop()
                
        return ans[::-1]