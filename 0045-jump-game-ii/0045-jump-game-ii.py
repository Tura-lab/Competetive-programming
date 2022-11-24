class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        q = deque([0])
        visited = set()
        
        dist = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                if node == n-1:
                    return dist
                
                if nums[node] == 0:continue
                
                for i in range(node + 1, min(n, node + nums[node] + 1)):
                    if i in visited:continue
                    visited.add(i)
                    q.append(i)
            dist += 1
            