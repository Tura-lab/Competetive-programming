class Solution:
    def minimumDistance(self, word: str) -> int:
        location = {
            'A': (0, 0),
            'B': (0, 1),
            'C': (0, 2),
            'D': (0, 3),
            'E': (0, 4),
            'F': (0, 5),
            'G': (1, 0),
            'H': (1, 1),
            'I': (1, 2),
            'J': (1, 3),
            'K': (1, 4),
            'L': (1, 5),
            'M': (2, 0),
            'N': (2, 1),
            'O': (2, 2),
            'P': (2, 3),
            'Q': (2, 4),
            'R': (2, 5),
            'S': (3, 0),
            'T': (3, 1),
            'U': (3, 2),
            'V': (3, 3),
            'W': (3, 4),
            'X': (3, 5),
            'Y': (4, 0),
            'Z': (4, 1),
        }
        
        def dist(a, b):
            if a == -1:
                return 0
            
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        @cache
        def dfs(i, left, right):
            if i == len(word):
                return 0
            
            # hit it with left
            l = dfs(i + 1, location[word[i]], right) + dist(left, location[word[i]])
            
            # hit with right
            r = dfs(i + 1, left, location[word[i]]) + dist(right, location[word[i]])
            
            return min(l, r)
        
        return dfs(0, -1, -1)