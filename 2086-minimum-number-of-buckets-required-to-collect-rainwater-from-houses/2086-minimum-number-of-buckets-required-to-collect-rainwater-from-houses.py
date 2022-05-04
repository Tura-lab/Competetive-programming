class Solution:
    def minimumBuckets(self, street: str) -> int:
        ans = 0
        seen = set()
        
        if street == 'H':
            return -1
        
        if len(street)>1 and (street[-1] == street[-2] == 'H' or street[0] == street[1] == 'H'):
            return -1
        
        for i in range(len(street)):
            if street[i] == 'H':
                if i-1>-1 and i+1<len(street) and street[i-1]==street[i+1]=='H':
                    return -1
                elif i+1<len(street) and street[i+1] == '.' and i-1 not in seen:
                    seen.add(i+1)
                    ans+=1
                elif i+1<len(street) and street[i+1] == 'H' and i-1 not in seen:
                    seen.add(i-1)
                    ans+=1
                elif i+1==len(street) and i-1 not in seen:
                    seen.add(i-1)
                    ans+=1
        
        return ans