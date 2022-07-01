class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(s)
        new_counts = {}
        
        for _,j in counts.items():
            if j in new_counts:
                new_counts[j] +=1
            else:
                new_counts[j] = 1
                
        new_counts = sorted(new_counts.items(), key = lambda x: x[0])
        possible = []
        tot = 0
        
        # print(new_counts)
        past = 0
        for i,j in new_counts:
            for k in range(past, i):
                possible.append(k)
            for _ in range(j-1):
                num = 0 if not possible else possible.pop()
                tot += i - num
            past = i+1
        return tot