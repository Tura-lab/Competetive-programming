class Solution:
    def reverseWords(self, s: str) -> str:
        new = s.split()
        
        new_new = []
        for word in new:
            if word != ' ':
                new_new.append(word.strip())
                
        i, j = 0, len(new_new) - 1
        while i < j:
            new_new[i], new_new[j] = new_new[j], new_new[i]
            i += 1
            j -= 1
            
        return " ".join(new_new)
        