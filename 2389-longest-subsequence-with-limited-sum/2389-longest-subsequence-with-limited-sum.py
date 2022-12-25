class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        ps = [0]
        
        for num in nums:
            ps.append(num + ps[-1])
        
        answer = []
        for query in queries:
            l, r = 0, n
            
            ans = 0
            while l <= r:
                mid = l + (r-l)//2
                
                if ps[mid] <= query:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
                    
            answer.append(ans)
            
        return answer