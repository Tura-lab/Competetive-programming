class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        q = deque()
        
        for num in range(lo, hi+1):
            q.append((num, num))
        
        count = 0
        
        while q:
            num, parent = q.popleft()
            
            if num == 1:
                count += 1
                if count == k:
                    return parent
                continue
            
            if num & 1:
                q.append((num * 3 + 1, parent))
            else:
                q.append((num // 2, parent))
        
        
            