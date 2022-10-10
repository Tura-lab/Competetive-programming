class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        found = [-1]*len(nums)
        visited = set()
        
        def dfs(node):
            if node in visited:
                return 0
            if found[node] != -1:
                print(found[node],1111111)
                return found[node]
            
            visited.add(node)
            found[node] = dfs(nums[node])
            return 1 + found[node]
        
        for i in nums:
            visited = set()
            if found[i] == -1:
                found[i] = dfs(i)
                # break
                
        # print(found)
        return max(found)
        
        