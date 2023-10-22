class WordDictionary:

    def __init__(self):
        self.trie = dict()
        

    def addWord(self, word: str) -> None:
        node = self.trie
        for i, l in enumerate(word):
            if l not in node:
                node[l] = dict()
            node = node[l]
            if i == len(word) - 1:
                node["end"] = True
                
            

    def search(self, word: str) -> bool:
        print
        def dfs(node, i):
            if i == len(word):
                return False
            
            if word[i] == '.':
                for v, vals in node.items():
                    if v == 'end':
                        continue
                        
                    if i == len(word) - 1:
                        if 'end' in vals:
                            return True
                    
                    if dfs(vals, i + 1):
                        return True
                    
                return False

            if word[i] not in node:
                return False
            
            node = node[word[i]]
            
            if i == len(word) - 1:
                if 'end' in node:
                    return True
                return False
            
            return dfs(node, i + 1)
            
        
        return dfs(self.trie, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)