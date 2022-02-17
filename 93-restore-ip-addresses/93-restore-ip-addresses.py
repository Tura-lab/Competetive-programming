class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        
        def makeIP(cur, pos):
            if cur and (int(cur[-1])>255 or (cur[-1][0]=='0' and len(cur[-1])>1)):
                return
            if len(cur) == 4:
                ans.append(cur[:]) if cur not in ans else None
                return
            
            for i in range(pos+1, min(pos+4, len(s))+1):
                cur.append(s[pos:i] if len(cur)<3 else s[pos:])
                makeIP(cur, i)
                cur.pop()    
                
        makeIP([], 0)
        
        return ['.'.join(n) for n in ans]