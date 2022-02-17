class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def comb(arr, total, i):
            if total == target:
                return ans.append(arr[:])
            if total>target or i==len(candidates):
                return
            
            prev = -1
            for i in range(i, len(candidates)):
                if candidates[i] == prev:
                    # Since this is a duplicate element we don't want to work on it sice we have worked on                       the prev element
                    continue
                #CHOOSE
                arr.append(candidates[i])
                #EXPLORE
                comb(arr, total + candidates[i], i+1)
                #UNCHOOSE
                arr.pop()
                prev = candidates[i]
        
        comb([], 0, 0)
        return ans