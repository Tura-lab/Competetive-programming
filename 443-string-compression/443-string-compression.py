class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        val = chars[0]
        i=1
        j=0
        count=1
        while i<len(chars):
            if chars[i]==val:
                count+=1
            else:
                chars[j]=val
                j+=1
                val=chars[i]
                if count>1:
                    for k in str(count):
                        chars[j]=k
                        j+=1
                count=1
            i+=1
        chars[j]=val
        j+=1
        if count>1:
            for k in str(count):
                chars[j]=k
                j+=1
        return j