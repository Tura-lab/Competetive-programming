class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def comb(arr, total, i):
            if total == target:
                return ans.append(arr)
            if i == len(candidates) or total>target:
                return            
        
            for i in range(i,len(candidates)):
                #Include
                comb(arr + [candidates[i]], total + candidates[i], i)

        comb([], 0, 0)
        return ans
            