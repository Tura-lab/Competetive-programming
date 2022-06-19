class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        mod = 10**9 + 7
        hashes = {}
        def hash(word):
            code = 0
            for i in range(len(word)):
                code += (26**i)*(ord(word[i])-ord('a') + 1)
                
            return code

        for word in dictionary:
            hashes[hash(word)] = word
            
            
        s = sentence.split()
        
        for i in range(len(s)):
            code = 0
            for j in range(0,len(s[i])):
                code += (26**j)*(ord(s[i][j])-ord('a') + 1)
                if code in hashes:
                    s[i] = hashes[code]
                    break
                    
        return ' '.join(s)
                    
                
        
        
        
        