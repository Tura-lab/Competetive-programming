class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = []
        
        for letter in s:
            if letter.isalnum():
                new.append(letter.upper())
        
        i, j = 0, len(new) - 1
        while i < j:
            if new[j] != new[i]:
                return False
            
            i += 1
            j -= 1
        
        return True