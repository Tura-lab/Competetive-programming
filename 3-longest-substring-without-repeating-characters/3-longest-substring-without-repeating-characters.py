class Solution:
    '''
    g1, y1, o1, h1
    a w g y g o h
          i
                j
    '''
    def lengthOfLongestSubstring(self, s):
        if s == '':
            return 0
        ans = 1
        counter = {}
        i=0
        j=0
        while j<len(s):
            if s[j] not in counter:
                counter[s[j]] = 1
            else:
                counter[s[j]] += 1
                
            if len(counter) != j-i+1:
                if counter[s[i]]==1:
                    del counter[s[i]]
                else:
                    counter[s[i]]-=1
                i+=1
            ans = max(ans, len(counter))
            j+=1
        return ans
        # a=''
        # longest=0
        # for i in range(len(s)):
        #     j=i
        #     while j<len(s) and s[j] not in a:
        #         a+=s[j]
        #         j+=1
        #     if len(a)>longest:
        #         longest = len(a)
        #     a=''
        # return longest