class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        rows = ['']*numRows
        rows[0] += s[0]
        
        zig = 1
        i=1
        while i<len(s):
            for j in range(1,numRows):
                if i==len(s):
                    break
                rows[j] += s[i]
                i+=1
            
            for j in range(numRows-2, -1, -1):
                if i==len(s):
                    break
                rows[j] += s[i]
                i+=1
        
        return (''.join(rows))