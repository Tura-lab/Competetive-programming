class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        q = deque([0])
        visited = set([0])
        
        count = 0
        while q:
            for _ in range(len(q)):
                val = q.popleft()
                
                for coin in coins:
                    new = val + coin
                    if new == amount:
                        return count +1
                    elif new < amount and new not in visited:
                        q.append(new)
                        visited.add(new)
            count += 1
        return -1
                        