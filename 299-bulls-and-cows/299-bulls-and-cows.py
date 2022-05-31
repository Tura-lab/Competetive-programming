class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        reps = Counter(secret)
        repss = Counter(guess)
        s = set(secret)
        pos = 0
        count = 0
        
        for i in range(len(guess)):
            if guess[i] == secret[i] and reps[guess[i]]>0 and repss[guess[i]]>0:
                pos+=1
                reps[guess[i]]-=1
                repss[guess[i]]-=1
        
        # print(reps)
        for i in range(len(guess)):
            if guess[i] in s and reps[guess[i]]>0 and repss[guess[i]]>0:
                count+=1
                repss[guess[i]]-=1
                reps[guess[i]]-=1
            
        return f'{pos}A{count}B'