class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        next_larger = [n for _ in range(len(arr))]
        
        stack = []
        
        for i, num in enumerate(arr):
            while stack and num > stack[-1][0]:
                val, idx = stack.pop()
                next_larger[idx] = i
            stack.append((num, i))
        mx = 0    
        for i in range(len(arr)):
            wins = next_larger[i] - i - 1 + (i > 0 and arr[i-1] < arr[i])
            
            if wins >= k:
                return arr[i]
            
            mx = max(mx, arr[i])
            
        return mx