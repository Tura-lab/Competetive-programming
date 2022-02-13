class Solution:
    '''
    ADOBECODEBANC
    ACC
    '''
    def minWindow(self, s: str, t: str) -> str:
        def yes():
            for i,j in goal.items():
                if i not in d:
                    return False
                if j > d[i]:
                    return False
            return True
        
        if len(t)>len(s):
            return ''

        ans = ''
        goal = {}
        for letter in t:
            if letter in goal:
                goal[letter] +=1
            else:
                goal[letter] = 1
        i=j=0
        d = {}
        found=False
        # print(goal)
        while  j<len(s):
            if s[j] in goal:
                if s[j] not in d:
                    d[s[j]] = 1
                else:
                    d[s[j]] +=1
            
            # print(d,i,j)
            if found:
                if s[i] in d:
                    d[s[i]] -=1
                    if d[s[i]] == 0:
                        del d[s[i]]
                i+=1
            while yes():
                ans = s[i:j+1]
                found=True
                if s[i] in d:
                    d[s[i]] -=1
                    if d[s[i]] == 0:
                        del d[s[i]]
                i+=1
            j+=1
        
        return ans
            