class Solution:
    def minJumps(self, nums: List[int]) -> int:
        found, n = defaultdict(list), len(nums)
        
        for i in range(n):
            found[nums[i]].append(i)
                
        q = deque([0])
        visited = set([0])
        jumped = set()
        
        steps = 0
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                
                if i == n-1:
                    return steps
                
                if i+1 < n and i+1 not in visited:
                    visited.add(i+1)
                    q.append(i+1)
                
                if i-1 >= 0 and i-1 not in visited:
                    visited.add(i-1)
                    q.append(i-1)
                    
                if nums[i] in jumped:continue
                
                for idx in found[nums[i]]:
                    if idx in visited:continue
                    
                    visited.add(idx)
                    q.append(idx)
                
                jumped.add(nums[i])
            steps += 1