class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        ["o","a","a","n"]
        ["e","t","a","e"]
        ["i","h","k","r"]
        ["i","f","l","v"]
        '''
        rows, cols = len(board), len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        trie = {}
        past = {}
        
        def in_bound(row, col):
            return -1<row<rows and -1<col<cols
        
        for word in words:
            node = trie
            for l in word:
                if l not in node:
                    node[l] = {}
                node = node[l]
            node[1] = 1
        
        ans = []
        def search(i, j, node):
            if 1 in node:
                ans.append(''.join(path))
                del node[1]
                # print(node)
                past = node
                k = len(nodes)-1
                while k >= 0 and len(node) == 0:
                    if path[k] in nodes[k]:
                        del nodes[k][path[k]]
                    node = nodes[k]
                    k-=1
                
                node = past
            
            for x,y in directions:
                nx, ny = i+x, j+y
                if in_bound(nx, ny) and board[nx][ny] in node:
                    l = board[nx][ny]
                    
                    nodes.append(node)
                    path.append(l)
                    
                    board[nx][ny] = '#'
                    
                    search(nx, ny, node[l])
                    
                    board[nx][ny] = l
                    nodes.pop()
                    path.pop()
            
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie:
                    t = board[i][j]
                    
                    path  = [t]
                    nodes = [trie]

                    board[i][j] = '#'

                    # start dfs
                    search(i, j, trie[t])
                    
                    board[i][j] = t
                
        return ans