class Solution:
    def numSplits(self, s: str) -> int:
        distinct_right = {}
        dis_right = 0
        distict_left = {s[0]:1}
        dis_left = 1
        counter = 0

        for i in range(1, len(s)):
            if s[i] not in distinct_right:
                distinct_right[s[i]] = 1
                dis_right +=1
            else:
                distinct_right[s[i]] += 1
    
        for i in range(1, len(s)):
            if dis_left==dis_right:
                counter+=1
            if s[i] in distict_left:
                distict_left[s[i]] += 1
            else:
                distict_left[s[i]] = 1
                dis_left+=1
            if distinct_right[s[i]]>1:
                distinct_right[s[i]]-=1
            else:
                dis_right-=1
                distinct_right[s[i]]-=1
        
        
        return counter