class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        found = defaultdict(list)
        
        for i, l in enumerate(s):
            found[l].append(i)
        
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for a in letters:
            for b in letters:
                cur = a + b + a
                # take the last
                if len(found[a]) == 0:
                    continue
                    
                idx = found[a][-1]
                
                # find the second
                idx2 = None
                l, r = 0, len(found[b]) - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    
                    if found[b][mid] >= idx:
                        r = mid - 1
                    else:
                        l = mid + 1
                        idx2 = found[b][mid]
                        
                if idx2 == None:
                    continue
                
                # find the third
                idx3 = None
                l, r = 0, len(found[a]) - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    
                    if found[a][mid] >= idx2:
                        r = mid - 1
                    else:
                        l = mid + 1
                        idx3 = found[a][mid]
                
                if idx3 == None:
                    continue
                    
                ans += 1
                # print(cur)
                
                
        return ans
                        
                