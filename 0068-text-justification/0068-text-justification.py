class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        
        line = []
        cur = 0
        for word in words:
            if cur + len(line) + len(word) <= maxWidth:
                line.append(word)
                cur += len(word)
            else:
                spaces = 0 if len(line) ==1 else (maxWidth - cur) // (len(line)-1)
                rem = 0 if len(line)==1 else (maxWidth - cur) % (len(line)-1)
                new = ''
                for i in range(len(line)):
                    new += line[i]
                    if i<len(line)-1:
                        new += ' ' * (spaces + (1 if rem else 0))
                    if rem:
                        rem-=1
                if len(new) < maxWidth:
                    new += ' '* (maxWidth - len(new))
                ans.append(new)
                cur = len(word)
                line = [word]
        
        new = ' '.join(line)
        new += ' ' * (maxWidth - len(new))
        ans.append(new)
        
        # for a in ans:print(a)
        return ans
        # for a in ans:print(a)