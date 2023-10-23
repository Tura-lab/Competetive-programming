class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(reverse = True)
        heap = []
        categories = defaultdict(int)
        tot_profit = 0
        for i in range(k):
            profit, category = items[i]
            categories[category] += 1 
            
            heappush(heap, (1 if categories[category] == 1 else 0, profit, category))
            tot_profit += profit
            
        ans = tot_profit + len(categories) ** 2
        for i in range(k, len(items)):
            profit, category = items[i]
            if category not in categories and heap[0][0] == 0:
                _, prof, cat = heappop(heap)
                categories[cat] -= 1
                if categories[cat] == 0:
                    del categories[cat]
                
                categories[category] += 1
                heappush(heap, (1 if categories[category] == 1 else 0, profit, category))
                
                tot_profit += profit - prof
                                
            ans = max(ans, tot_profit + len(categories) ** 2)
            
        return ans