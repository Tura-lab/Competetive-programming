from collections import Counter

class Solution:
    '''
    ababcbacadefegdehijhklij
    '''
    def partitionLabels(self, s):
        ans=[]
        count = Counter(s)
        def isUniq(temp, count):
            for i,j in temp.items():
                if i in count and count[i]>0:
                    return False
            return True
        
        num=0
        temp={}
        for letter in s:
            count[letter]-=1
            if letter in temp:
                temp[letter]+=1
            else:
                temp[letter]=1
            num+=1
            if isUniq(temp, count):
                ans.append(num)
                temp = {}
                num=0
            
        return ans 