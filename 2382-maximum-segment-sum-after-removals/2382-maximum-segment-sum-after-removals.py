from heapq import heappush, heappop

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        heap = []
        heappush(heap, 0)
        found = {}
        
        tot = nums[:]
        parent = [i for i in range(len(nums))]
        size = [1]*(len(nums))
        
        def find(a):
            while a != parent[a]:
                a = parent[a]
            return a
        
        def union(a,b):
            a, b = find(a), find(b)
            if a == b:
                return tot[a]
            
            if size[b] > size[a]:
                a,b = b,a
            
            parent[b] = a
            size[a] += size[b]
            #Extra
            tot[a] += tot[b]
            return tot[a]
            
        ans = [0]*len(nums)
        cur_max = 0
        
        found = [False]*len(nums)
        for i in range(len(removeQueries)-1, -1, -1):
            ans[i] = cur_max
            cur = removeQueries[i]
            found[cur] = True
            if cur-1>-1 and cur+1<len(nums) and (found[cur-1] and found[cur+1]):
                union(cur-1,cur+1)
                cur_max = max(cur_max, union(cur-1,cur))
            elif cur-1>-1 and found[cur-1]:
                cur_max = max(cur_max, union(cur, cur-1))
            elif cur+1<len(nums) and found[cur+1]:
                cur_max = max(cur_max, union(cur, cur+1))
            else:
                cur_max = max(cur_max, union(cur, cur))
                
            
        return ans     
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                