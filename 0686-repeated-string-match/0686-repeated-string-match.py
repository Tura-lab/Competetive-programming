class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = len(b)
        
        pref_arr = [0]
        i, j = 0, 1
        while j < len(b):
            if b[i] == b[j]:
                i += 1
            elif i > 0:
                i = pref_arr[i - 1]
                continue
                
            j += 1
            pref_arr.append(i)
        
        # now find a match
        start = 0
        ok = False
        count = 0
        i, j = 0, 0
        while j < n:
            if a[i] == b[j]:
                if j == n - 1:
                    start = (len(a) + (i - j % len(a))) % len(a)
                j += 1
            elif j > 0:
                j = pref_arr[j - 1]
                start = 1
                continue
            else:
                start = 1
            
            i += 1
            i %= len(a)
            
            count += 1
            if count > 2 * max(len(a), len(b)) :
                break

        if j < n:
            return -1
        
        tot_len = ceil((start + len(b)) / len(a))
        # print(start)
        
        return tot_len